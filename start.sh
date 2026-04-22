#!/bin/bash

echo "========================================"
echo "基隆消防局案件監控系統"
echo "========================================"

# 檢查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 錯誤: 未安裝 Python 3"
    echo "請先安裝 Python 3.8 或更高版本"
    exit 1
fi

# 檢查 config.json
if [ ! -f "config.json" ]; then
    echo "📝 首次運行，建立設定檔..."
    cp config.example.json config.json
    echo "⚠️  請編輯 config.json 填入您的 Telegram Bot Token 和 Chat ID"
    echo ""
    echo "如何取得資訊："
    echo "1. Bot Token: 在 Telegram 搜尋 @BotFather 建立機器人"
    echo "2. Chat ID: 在 Telegram 搜尋 @userinfobot 取得您的 ID"
    echo ""
    exit 1
fi

# 檢查套件
echo "📦 檢查依賴套件..."
if [ ! -d "venv" ]; then
    echo "建立虛擬環境..."
    python3 -m venv venv
fi

source venv/bin/activate
pip install -q -r requirements.txt

# 啟動程式
echo "🚀 啟動監控系統..."
python fdkc_monitor.py
