# 高雄市消防局案件監控系統 🚒🚗

自動監控 [高雄市消防局案件系統](https://119dts.fdkc.gov.tw/DTS/caselist/html)，當有新的**車禍**或**火警**案件時，立即透過 Telegram 發送通知。

## ✨ 功能特色

- 🔍 每 10 分鐘自動檢查新案件
- 🚨 只通知車禍和火警案件
- 📱 透過 Telegram 即時推送通知
- 💾 避免重複通知已處理的案件
- 📝 完整的執行日誌記錄
- 🔄 自動重試機制，確保穩定運行

## 📋 通知內容

每則通知包含以下資訊：
- 📋 案件類別
- 🕒 受理時間
- 📍 發生地點
- 🚒 派遣分隊
- ⚡ 執行狀況

## 🚀 快速開始

### 1. 建立 Telegram Bot

1. 在 Telegram 中搜尋 `@BotFather`
2. 發送 `/newbot` 指令建立新機器人
3. 依照指示設定機器人名稱
4. 取得 **Bot Token**（格式：`123456789:ABCdefGHIjklMNOpqrsTUVwxyz`）

### 2. 取得 Chat ID

有兩種方式：

**方式一：使用 @userinfobot**
1. 在 Telegram 搜尋 `@userinfobot`
2. 啟動對話，它會顯示你的 Chat ID

**方式二：使用 API**
1. 先對你的 Bot 發送一則訊息（任意內容）
2. 開啟瀏覽器訪問：
   ```
   https://api.telegram.org/bot你的BOT_TOKEN/getUpdates
   ```
3. 在回傳的 JSON 中找到 `"chat":{"id":123456789}` 的數字

### 3. 安裝程式

```bash
# 克隆專案
git clone https://github.com/你的帳號/fdkc-monitor.git
cd fdkc-monitor

# 安裝依賴套件
pip install -r requirements.txt
```

### 4. 設定

首次執行程式會自動建立 `config.json` 範本：

```bash
python fdkc_monitor.py
```

編輯 `config.json`，填入你的資訊：

```json
{
  "telegram_token": "123456789:ABCdefGHIjklMNOpqrsTUVwxyz",
  "chat_id": "123456789"
}
```

### 5. 執行

```bash
python fdkc_monitor.py
```

程式會：
1. 立即執行一次檢查
2. 每 10 分鐘自動檢查一次
3. 持續運行直到手動停止（Ctrl+C）

## 📦 檔案說明

```
fdkc-monitor/
├── fdkc_monitor.py      # 主程式
├── requirements.txt     # Python 套件需求
├── config.json          # 設定檔（需自行建立）
├── notified_cases.json  # 已通知案件快取（自動產生）
├── fdkc_monitor.log     # 執行日誌（自動產生）
└── README.md            # 說明文件
```

## 🐳 使用 Docker 運行（進階）

### 建立映像

```bash
docker build -t fdkc-monitor .
```

### 運行容器

```bash
docker run -d \
  --name fdkc-monitor \
  -v $(pwd)/config.json:/app/config.json \
  -v $(pwd)/notified_cases.json:/app/notified_cases.json \
  -v $(pwd)/fdkc_monitor.log:/app/fdkc_monitor.log \
  fdkc-monitor
```

### 查看日誌

```bash
docker logs -f fdkc-monitor
```

## 🔧 進階設定

### 修改檢查頻率

在 `fdkc_monitor.py` 中找到這一行：

```python
schedule.every(10).minutes.do(monitor.run_check)
```

可改為：
- `schedule.every(5).minutes.do(...)` - 每 5 分鐘
- `schedule.every(1).hours.do(...)` - 每 1 小時
- `schedule.every().hour.at(":30").do(...)` - 每小時的 30 分

### 修改監控案件類型

在 `is_target_case` 方法中修改關鍵字：

```python
keywords = ['車禍', '火警', '火災', 'a1', 'a2', 'a3', '交通事故']
```

例如，只監控火警：
```python
keywords = ['火警', '火災']
```

## 📊 運行建議

### Linux/macOS 背景執行

使用 `screen` 或 `tmux`：

```bash
# 使用 screen
screen -S fdkc
python fdkc_monitor.py
# 按 Ctrl+A 再按 D 離開（程式繼續運行）

# 重新連接
screen -r fdkc
```

### 使用 systemd（Linux）

建立服務檔 `/etc/systemd/system/fdkc-monitor.service`：

```ini
[Unit]
Description=FDKC Case Monitor
After=network.target

[Service]
Type=simple
User=你的使用者名稱
WorkingDirectory=/path/to/fdkc-monitor
ExecStart=/usr/bin/python3 /path/to/fdkc-monitor/fdkc_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

啟動服務：

```bash
sudo systemctl enable fdkc-monitor
sudo systemctl start fdkc-monitor
sudo systemctl status fdkc-monitor
```

### Windows 背景執行

使用工作排程器或 `pythonw`：

```batch
pythonw fdkc_monitor.py
```

## 🐛 故障排除

### 無法連線到網站

- 檢查網路連線
- 確認網站 URL 是否正確
- 查看 `fdkc_monitor.log` 日誌

### Telegram 訊息無法發送

- 確認 Bot Token 正確
- 確認 Chat ID 正確
- 確認已對 Bot 發送過至少一則訊息

### 程式自動停止

- 檢查 `fdkc_monitor.log` 查看錯誤訊息
- 建議使用 systemd 或 Docker 確保自動重啟

## 📝 日誌範例

```
2024-01-15 10:00:00 - __main__ - INFO - 基隆消防局案件監控系統啟動
2024-01-15 10:00:05 - __main__ - INFO - 成功抓取 15 筆案件
2024-01-15 10:00:06 - __main__ - INFO - 發現 2 筆新案件
2024-01-15 10:00:07 - __main__ - INFO - Telegram 訊息已發送
2024-01-15 10:10:00 - __main__ - INFO - 開始檢查新案件...
```

## ⚠️ 注意事項

1. **穩定性**：建議在穩定的伺服器或電腦上運行
2. **網路**：需要穩定的網路連線
3. **資源**：程式佔用資源極少，適合長期運行
4. **隱私**：Bot Token 和 Chat ID 請勿公開分享
5. **合法使用**：僅供個人通知使用，請勿濫用

## 📄 授權

MIT License - 自由使用和修改

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📧 聯絡

如有問題或建議，歡迎開 Issue 討論。

---

**⭐ 如果這個專案對你有幫助，請給個星星支持！**
