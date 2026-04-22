# 🚀 GitHub 完整上傳和執行指南

## 📦 你需要上傳的檔案清單

```
✅ fdkc_monitor.py          （主程式 - 已修改支援 GitHub Actions）
✅ test_telegram.py          （測試工具）
✅ requirements.txt          （套件清單）
✅ config.example.json       （設定檔範例）
✅ .gitignore                （Git 忽略檔案）
✅ README.md                 （說明文件）
✅ LICENSE                   （授權）
✅ .github/workflows/monitor.yml  （GitHub Actions 設定）

❌ config.json               （不要上傳！包含你的 Token）
```

---

## 📤 步驟 1: 上傳到 GitHub

### 方法 A：網頁上傳（最簡單）

1. **建立倉庫**
   - 前往 https://github.com/new
   - Repository name: `fdkc-monitor`
   - 選擇 Public 或 Private
   - ✅ 勾選 "Add a README file"
   - 點擊 **Create repository**

2. **上傳主要檔案**
   - 點擊 **Add file** → **Upload files**
   - 拖曳這些檔案：
     - `fdkc_monitor.py`
     - `test_telegram.py`
     - `requirements.txt`
     - `config.example.json`
     - `.gitignore`
     - `LICENSE`
   - Commit message: `Add main project files`
   - 點擊 **Commit changes**

3. **建立 GitHub Actions 檔案**
   - 回到倉庫首頁
   - 點擊 **Add file** → **Create new file**
   - 檔名輸入：`.github/workflows/monitor.yml`
   - 複製 `monitor.yml` 的內容貼上
   - Commit message: `Add GitHub Actions workflow`
   - 點擊 **Commit new file**

---

## 🔑 步驟 2: 設定 GitHub Secrets

**這一步非常重要！** 用來安全地儲存你的 Telegram Token 和 Chat ID。

1. **進入 Settings**
   - 在你的倉庫頁面，點擊 **Settings**

2. **找到 Secrets**
   - 左側選單：**Secrets and variables** → **Actions**

3. **新增第一個 Secret**
   - 點擊 **New repository secret**
   - Name: `TELEGRAM_TOKEN`
   - Secret: 貼上你的 Telegram Bot Token
     ```
     例如: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
     ```
   - 點擊 **Add secret**

4. **新增第二個 Secret**
   - 再次點擊 **New repository secret**
   - Name: `TELEGRAM_CHAT_ID`
   - Secret: 貼上你的 Chat ID
     ```
     例如: 987654321
     ```
   - 點擊 **Add secret**

5. **確認 Secrets**
   - 你應該看到兩個 Secret：
     - ✅ TELEGRAM_TOKEN
     - ✅ TELEGRAM_CHAT_ID

---

## ▶️ 步驟 3: 執行監控

### 手動執行測試

1. **前往 Actions 頁面**
   - 在倉庫頁面點擊 **Actions** 標籤

2. **手動執行**
   - 左側選擇 "基隆消防局監控"
   - 點擊 **Run workflow** 下拉選單
   - 點擊綠色的 **Run workflow** 按鈕

3. **查看執行狀況**
   - 會出現一個新的工作流程執行
   - 點擊進去查看詳細日誌
   - 等待執行完成（約 1-2 分鐘）

4. **檢查 Telegram**
   - 如果有新案件，你會收到通知
   - 如果沒有新案件，日誌會顯示 "沒有新案件"

### 自動執行

設定完成後，程式會：
- ✅ 每 10 分鐘自動執行一次
- ✅ 發現新案件自動發送 Telegram 通知
- ✅ 自動保存已通知的案件，避免重複通知

---

## 📊 步驟 4: 查看執行記錄

### 在 Actions 頁面

1. 點擊 **Actions** 標籤
2. 查看執行歷史：
   - ✅ 綠色勾勾 = 執行成功
   - ❌ 紅色叉叉 = 執行失敗
   - 🟡 黃色點 = 執行中

3. 點擊任何一次執行可以看到：
   - 📊 詳細日誌
   - ⏱️ 執行時間
   - 📝 執行步驟

### 查看日誌

點擊執行記錄 → 點擊 "monitor" job → 查看各步驟：
- 📥 下載程式碼
- 🐍 設定 Python
- 📦 安裝套件
- 💾 載入快取
- 🚀 執行監控
- 📊 顯示日誌

---

## ⚙️ 步驟 5: 自訂設定（可選）

### 修改檢查頻率

編輯 `.github/workflows/monitor.yml`：

```yaml
# 每 5 分鐘（最小間隔）
- cron: '*/5 * * * *'

# 每 15 分鐘
- cron: '*/15 * * * *'

# 每 30 分鐘
- cron: '*/30 * * * *'

# 每小時
- cron: '0 * * * *'
```

**注意：** 時間是 UTC，比台灣時間慢 8 小時

### 修改監控案件類型

編輯 `fdkc_monitor.py`，找到 `is_target_case` 方法：

```python
# 只監控火警
keywords = ['火警', '火災']

# 只監控車禍
keywords = ['車禍', '交通事故', 'a1', 'a2']

# 全部都監控
keywords = ['車禍', '火警', '火災', 'a1', 'a2', 'a3', '交通事故']
```

---

## 🔧 故障排除

### 問題 1: Actions 執行失敗（紅色叉叉）

**檢查步驟：**
1. 點擊失敗的執行
2. 查看錯誤訊息
3. 常見原因：
   - Secret 沒設定或設定錯誤
   - Token 或 Chat ID 不正確
   - 網路問題

**解決方法：**
- 重新檢查 Secrets 設定
- 確認 Token 和 Chat ID 正確
- 手動重新執行

---

### 問題 2: 沒有收到 Telegram 通知

**可能原因：**
1. 目前沒有新案件
2. Token 或 Chat ID 錯誤
3. 你還沒對 Bot 發送過訊息

**解決方法：**
1. 查看執行日誌確認是否真的有新案件
2. 重新確認 Secrets 設定
3. 在 Telegram 對 Bot 發送 `/start`

---

### 問題 3: Secret 設定後還是失敗

**檢查：**
- Secret 名稱是否正確：
  - ✅ `TELEGRAM_TOKEN`
  - ✅ `TELEGRAM_CHAT_ID`
  - ❌ `telegram_token`（錯誤，區分大小寫）
- Secret 值是否包含多餘的空格

**重新設定：**
1. Settings → Secrets → Actions
2. 點擊 Secret 名稱
3. 點擊 **Update secret**
4. 重新貼上正確的值

---

## 💰 GitHub Actions 免費額度

**免費帳號：**
- 每月 2000 分鐘執行時間
- 公開倉庫無限制

**使用量計算：**
- 每次執行約 1-2 分鐘
- 每 10 分鐘執行一次
- 每天約 144 次 × 2 分鐘 = 288 分鐘/天
- 每月約 8640 分鐘

**建議：**
- 設定為每 15-30 分鐘執行一次
- 或只在上班時間執行（修改 cron）

---

## ✅ 完成檢查清單

- [ ] 所有檔案已上傳到 GitHub
- [ ] `.github/workflows/monitor.yml` 已建立
- [ ] TELEGRAM_TOKEN Secret 已設定
- [ ] TELEGRAM_CHAT_ID Secret 已設定
- [ ] 已手動執行測試
- [ ] 測試執行成功（綠色勾勾）
- [ ] Telegram 收到測試通知（如果有案件）
- [ ] 已確認自動執行正常運作

全部打勾就大功告成了！🎉

---

## 📞 需要幫助？

**常見問題：**
1. 查看本文件的故障排除章節
2. 檢查 Actions 頁面的執行日誌
3. 確認 Secrets 設定正確

**還是有問題？**
- 在 GitHub 倉庫開 Issue
- 貼上錯誤訊息和日誌
- 說明你已經嘗試過的解決方法

---

## 🎉 成功範例

執行成功後，你會看到：

**在 Actions 頁面：**
```
✅ 基隆消防局監控 #1
   執行成功 - 2 分鐘前
```

**在執行日誌：**
```
🌐 GitHub Actions 模式：執行單次檢查
開始檢查新案件...
成功抓取 15 筆案件
發現 2 筆新案件
Telegram 訊息已發送
✅ 檢查完成
```

**在 Telegram：**
```
🚗 基隆消防局新案件通報

📋 案件類別: A1類交通事故
🕒 受理時間: 2024/04/22 14:30
📍 發生地點: 基隆市中正區中正路100號
🚒 派遣分隊: 中正分隊
⚡ 執行狀況: 處理中
```

完美！🎊
