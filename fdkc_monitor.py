#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基隆市消防局案件監控系統
監控 https://119dts.fdkc.gov.tw/DTS/caselist/html 的新案件並透過 Telegram 通知
支援本地執行和 GitHub Actions 雲端執行
"""

import os
import time
import json
import logging
from datetime import datetime
from typing import List, Dict, Set
import requests
from bs4 import BeautifulSoup
import schedule
import asyncio
from telegram import Bot
from telegram.error import TelegramError

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fdkc_monitor.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 設定檔路徑
CONFIG_FILE = 'config.json'
CACHE_FILE = 'notified_cases.json'

class FDKCMonitor:
    """基隆消防局案件監控器"""
    
    def __init__(self, telegram_token: str, chat_id: str):
        self.url = "https://119dts.fdkc.gov.tw/DTS/caselist/html"
        self.telegram_token = telegram_token
        self.chat_id = chat_id
        self.bot = Bot(token=telegram_token)
        self.notified_cases: Set[str] = self.load_notified_cases()
        
    def load_notified_cases(self) -> Set[str]:
        """載入已通知的案件 ID"""
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return set(data.get('notified_cases', []))
            except Exception as e:
                logger.error(f"載入快取檔案失敗: {e}")
        return set()
    
    def save_notified_cases(self):
        """儲存已通知的案件 ID"""
        try:
            # 只保留最近 1000 筆記錄，避免檔案過大
            cases_list = list(self.notified_cases)[-1000:]
            self.notified_cases = set(cases_list)
            
            with open(CACHE_FILE, 'w', encoding='utf-8') as f:
                json.dump({
                    'notified_cases': cases_list,
                    'last_update': datetime.now().isoformat()
                }, f, ensure_ascii=False, indent=2)
        except Exception as e:
            logger.error(f"儲存快取檔案失敗: {e}")
    
    def fetch_cases(self) -> List[Dict[str, str]]:
        """抓取案件列表"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(self.url, headers=headers, timeout=30)
            response.encoding = 'utf-8'
            
            if response.status_code != 200:
                logger.error(f"HTTP 請求失敗: {response.status_code}")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            cases = []
            
            # 尋找案件表格（根據一般消防局網站結構）
            tables = soup.find_all('table')
            
            for table in tables:
                rows = table.find_all('tr')
                
                # 找出表頭，確認欄位位置
                headers = []
                for row in rows:
                    ths = row.find_all('th')
                    if ths:
                        headers = [th.get_text(strip=True) for th in ths]
                        break
                
                # 如果沒有找到表頭，使用預設欄位名稱
                if not headers and rows:
                    headers = ['受理時間', '案件類別', '發生地點', '派遣分隊', '執行狀況']
                
                # 解析資料列
                for row in rows[1:] if headers else rows:
                    cols = row.find_all('td')
                    if len(cols) >= 4:
                        case_data = {}
                        
                        for i, col in enumerate(cols):
                            text = col.get_text(strip=True)
                            if i < len(headers):
                                case_data[headers[i]] = text
                            else:
                                case_data[f'欄位{i+1}'] = text
                        
                        if case_data:
                            cases.append(case_data)
            
            logger.info(f"成功抓取 {len(cases)} 筆案件")
            return cases
            
        except requests.RequestException as e:
            logger.error(f"網路請求失敗: {e}")
            return []
        except Exception as e:
            logger.error(f"解析網頁失敗: {e}")
            return []
    
    def generate_case_id(self, case: Dict[str, str]) -> str:
        """產生案件唯一 ID"""
        time_str = case.get('受理時間', '')
        location = case.get('發生地點', '')
        case_type = case.get('案件類別', '')
        return f"{time_str}_{location}_{case_type}"
    
    def is_target_case(self, case: Dict[str, str]) -> bool:
        """判斷是否為目標案件（車禍或火警）"""
        case_type = case.get('案件類別', '').lower()
        keywords = ['車禍', '火警', '火災', 'a1', 'a2', 'a3', '交通事故']
        return any(keyword in case_type for keyword in keywords)
    
    async def send_telegram_message(self, message: str):
        """發送 Telegram 訊息"""
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode='HTML'
            )
            logger.info("Telegram 訊息已發送")
        except TelegramError as e:
            logger.error(f"Telegram 發送失敗: {e}")
    
    def format_case_message(self, case: Dict[str, str]) -> str:
        """格式化案件訊息"""
        case_type = case.get('案件類別', '未知')
        time_str = case.get('受理時間', '未知')
        location = case.get('發生地點', '未知')
        team = case.get('派遣分隊', '未知')
        status = case.get('執行狀況', '未知')
        
        icon = '🚗' if '車禍' in case_type or '交通' in case_type else '🔥'
        
        message = f"{icon} <b>基隆消防局新案件通報</b>\n\n"
        message += f"📋 <b>案件類別:</b> {case_type}\n"
        message += f"🕒 <b>受理時間:</b> {time_str}\n"
        message += f"📍 <b>發生地點:</b> {location}\n"
        message += f"🚒 <b>派遣分隊:</b> {team}\n"
        message += f"⚡ <b>執行狀況:</b> {status}\n"
        message += f"\n⏰ 通知時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        return message
    
    async def check_and_notify(self):
        """檢查並通知新案件"""
        logger.info("開始檢查新案件...")
        
        cases = self.fetch_cases()
        new_cases = []
        
        for case in cases:
            if not self.is_target_case(case):
                continue
            
            case_id = self.generate_case_id(case)
            
            if case_id not in self.notified_cases:
                new_cases.append(case)
                self.notified_cases.add(case_id)
        
        if new_cases:
            logger.info(f"發現 {len(new_cases)} 筆新案件")
            for case in new_cases:
                message = self.format_case_message(case)
                await self.send_telegram_message(message)
                await asyncio.sleep(1)
            
            self.save_notified_cases()
        else:
            logger.info("沒有新案件")
    
    def run_check(self):
        """執行檢查（同步包裝）"""
        asyncio.run(self.check_and_notify())


def load_config() -> Dict[str, str]:
    """載入設定檔（支援環境變數和本地設定檔）"""
    
    # 優先從環境變數讀取（用於 GitHub Actions）
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if token and chat_id:
        logger.info("從環境變數載入設定")
        return {
            'telegram_token': token,
            'chat_id': chat_id
        }
    
    # 否則從設定檔讀取（本地執行）
    if not os.path.exists(CONFIG_FILE):
        example_config = {
            "telegram_token": "YOUR_TELEGRAM_BOT_TOKEN",
            "chat_id": "YOUR_TELEGRAM_CHAT_ID"
        }
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(example_config, f, ensure_ascii=False, indent=2)
        logger.error(f"請編輯 {CONFIG_FILE} 填入您的 Telegram 資訊")
        exit(1)
    
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    if config.get('telegram_token') == 'YOUR_TELEGRAM_BOT_TOKEN':
        logger.error(f"請編輯 {CONFIG_FILE} 填入正確的 Telegram 資訊")
        exit(1)
    
    return config


def main():
    """主程式"""
    logger.info("=" * 50)
    logger.info("基隆消防局案件監控系統啟動")
    logger.info("=" * 50)
    
    # 載入設定
    config = load_config()
    
    # 建立監控器
    monitor = FDKCMonitor(
        telegram_token=config['telegram_token'],
        chat_id=config['chat_id']
    )
    
    # 檢查是否在 GitHub Actions 環境中
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    
    if is_github_actions:
        # GitHub Actions 模式：只執行一次
        logger.info("🌐 GitHub Actions 模式：執行單次檢查")
        monitor.run_check()
        logger.info("✅ 檢查完成")
    else:
        # 本地模式：持續運行
        logger.info("💻 本地模式：持續運行")
        logger.info("執行首次檢查...")
        monitor.run_check()
        
        # 設定排程：每 10 分鐘執行一次
        schedule.every(10).minutes.do(monitor.run_check)
        
        logger.info("排程已設定：每 10 分鐘檢查一次")
        logger.info("程式運行中... (按 Ctrl+C 停止)")
        
        # 持續運行
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("\n程式已停止")


if __name__ == "__main__":
    main()
