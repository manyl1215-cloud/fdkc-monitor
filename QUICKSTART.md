# 快速設定指南 ⚡

## 5 分鐘完成設定

### 步驟 1: 建立 Telegram Bot (2 分鐘)

1. 開啟 Telegram，搜尋 `@BotFather`
2. 發送指令: `/newbot`
3. 設定機器人名稱（例如：FDKC Monitor）
4. 設定使用者名稱（例如：fdkc_monitor_bot）
5. **複製 Bot Token** （像這樣: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`）

### 步驟 2: 取得 Chat ID (1 分鐘)

**方法 A - 使用 Bot（簡單）:**
1. 搜尋 `@userinfobot`
2. 點擊開始
3. **複製顯示的 ID** （純數字，例如：123456789）

**方法 B - 使用 API（進階）:**
1. 先對你的 Bot 發送一則訊息（任何內容）
2. 在瀏覽器打開：
   ```
   https://api.telegram.org/bot你的BOT_TOKEN/getUpdates
   ```
3. 找到 `"chat":{"id":123456789}`，複製這個數字

### 步驟 3: 安裝程式 (1 分鐘)

```bash
# 下載專案
git clone https://github.com/你的帳號/fdkc-monitor.git
cd fdkc-monitor

# 安裝套件
pip install -r requirements.txt
```

### 步驟 4: 設定 (30 秒)

```bash
# 複製範例設定檔
cp config.example.json config.json

# 編輯設定檔
nano config.json  # 或用任何文字編輯器
```

填入你的資訊：
```json
{
  "telegram_token": "貼上步驟1的Token",
  "chat_id": "貼上步驟2的ID"
}
```

### 步驟 5: 測試 (30 秒)

```bash
# 測試 Telegram 連線
python test_telegram.py
```

如果看到 ✅ 就成功了！

### 步驟 6: 啟動 (10 秒)

```bash
# 啟動監控
python fdkc_monitor.py
```

完成！程式現在會每 10 分鐘檢查一次，有新案件會自動通知你 🎉

---

## 常見問題

### Q: 我沒有收到測試訊息？
A: 確認你已經對 Bot 發送過至少一則訊息（點擊「開始」或隨便說句話）

### Q: 顯示 "Unauthorized" 錯誤？
A: Bot Token 錯誤，請重新從 BotFather 取得

### Q: 顯示 "Chat not found" 錯誤？
A: Chat ID 錯誤，或你還沒對 Bot 說過話

### Q: 如何在背景執行？
A: 
- Linux/Mac: 使用 `screen` 或 `nohup`
- Windows: 使用 `pythonw` 或工作排程器
- 建議: 使用 Docker Compose（見主 README）

### Q: 如何停止程式？
A: 按 `Ctrl + C`

---

## 需要幫助？

查看完整文件: [README.md](README.md)
