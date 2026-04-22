#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram 通知測試腳本
用於測試 Bot Token 和 Chat ID 是否正確設定
"""

import json
import asyncio
from telegram import Bot
from telegram.error import TelegramError

def load_config():
    """載入設定"""
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ 找不到 config.json 檔案")
        print("請先複製 config.example.json 為 config.json 並填入資訊")
        return None
    except json.JSONDecodeError:
        print("❌ config.json 格式錯誤")
        return None

async def test_telegram(token, chat_id):
    """測試 Telegram 連線"""
    try:
        bot = Bot(token=token)
        
        # 取得 Bot 資訊
        print("📱 正在測試 Telegram Bot...")
        bot_info = await bot.get_me()
        print(f"✅ Bot 名稱: {bot_info.first_name} (@{bot_info.username})")
        
        # 發送測試訊息
        print(f"📤 發送測試訊息到 Chat ID: {chat_id}...")
        test_message = """
🧪 <b>基隆消防局監控系統測試訊息</b>

如果您收到這則訊息，表示設定成功！ ✅

程式將會在偵測到新的車禍或火警案件時，
自動發送通知到這個對話。

⏰ 測試時間: 現在
🔧 系統狀態: 正常運作
        """
        
        await bot.send_message(
            chat_id=chat_id,
            text=test_message.strip(),
            parse_mode='HTML'
        )
        
        print("✅ 測試訊息已成功發送！")
        print("請檢查您的 Telegram 是否收到訊息")
        return True
        
    except TelegramError as e:
        print(f"❌ Telegram 錯誤: {e}")
        print("\n可能的問題：")
        print("1. Bot Token 不正確")
        print("2. Chat ID 不正確")
        print("3. 您尚未對 Bot 發送過訊息（請先在 Telegram 對 Bot 說句話）")
        return False
    except Exception as e:
        print(f"❌ 未預期的錯誤: {e}")
        return False

def main():
    print("=" * 60)
    print("基隆消防局監控系統 - Telegram 連線測試")
    print("=" * 60)
    print()
    
    # 載入設定
    config = load_config()
    if not config:
        return
    
    token = config.get('telegram_token', '')
    chat_id = config.get('chat_id', '')
    
    # 檢查設定值
    if not token or token == 'YOUR_TELEGRAM_BOT_TOKEN':
        print("❌ 請在 config.json 中設定正確的 telegram_token")
        return
    
    if not chat_id or chat_id == 'YOUR_TELEGRAM_CHAT_ID':
        print("❌ 請在 config.json 中設定正確的 chat_id")
        return
    
    # 執行測試
    success = asyncio.run(test_telegram(token, chat_id))
    
    print()
    if success:
        print("🎉 測試完成！您可以開始執行監控程式了：")
        print("   python fdkc_monitor.py")
    else:
        print("❌ 測試失敗，請檢查設定後再試一次")
    print()

if __name__ == "__main__":
    main()
