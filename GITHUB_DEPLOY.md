# 📤 GitHub 部署指南

如何將這個專案發布到 GitHub 並開始使用。

## 🚀 快速部署步驟

### 步驟 1: 在 GitHub 建立新倉庫

1. 前往 https://github.com/new
2. 填寫資訊：
   - Repository name: `fdkc-monitor` （或其他名稱）
   - Description: `基隆市消防局案件監控系統 - 自動監控車禍和火警並透過 Telegram 通知`
   - 選擇 **Public** 或 **Private**
   - **不要**勾選 "Add a README file"
   - **不要**勾選 "Add .gitignore"
   - **不要**選擇 License（我們已經有了）
3. 點擊 "Create repository"

### 步驟 2: 上傳專案檔案

#### 方法 A: 使用 Git 指令（推薦）

```bash
# 1. 進入專案目錄
cd fdkc-monitor

# 2. 初始化 Git
git init

# 3. 加入所有檔案
git add .

# 4. 建立第一次提交
git commit -m "Initial commit: FDKC Monitor System"

# 5. 設定遠端倉庫（替換成你的 GitHub 帳號和倉庫名稱）
git remote add origin https://github.com/你的帳號/fdkc-monitor.git

# 6. 推送到 GitHub
git branch -M main
git push -u origin main
```

#### 方法 B: 使用 GitHub Desktop

1. 開啟 GitHub Desktop
2. File → Add Local Repository
3. 選擇專案資料夾
4. 初始化倉庫
5. Commit to main
6. Publish repository

#### 方法 C: 直接上傳（最簡單但不推薦）

1. 在 GitHub 倉庫頁面點擊 "uploading an existing file"
2. 拖曳所有檔案（除了 config.json）
3. 填寫 commit message
4. 點擊 "Commit changes"

### 步驟 3: 驗證上傳

檢查 GitHub 倉庫頁面應該看到：
- ✅ README.md 自動顯示在首頁
- ✅ 所有程式檔案
- ✅ LICENSE 檔案
- ❌ **確認沒有** `config.json`（這個包含敏感資訊）

### 步驟 4: 美化倉庫（可選）

#### 加入 Topics 標籤
在倉庫頁面點擊 ⚙️ About → Add topics:
- `telegram-bot`
- `monitoring`
- `python`
- `web-scraping`
- `notification`
- `taiwan`

#### 加入 Description
```
🚒 基隆市消防局案件即時監控 - 自動偵測車禍和火警案件，透過 Telegram 即時通知
```

#### 設定 README 徽章（可選）
在 README.md 最上方加入：

```markdown
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)
```

## 📥 其他人如何使用你的專案

### 克隆倉庫
```bash
git clone https://github.com/你的帳號/fdkc-monitor.git
cd fdkc-monitor
```

### 安裝並執行
```bash
# 安裝套件
pip install -r requirements.txt

# 設定
cp config.example.json config.json
# 編輯 config.json 填入 Telegram 資訊

# 測試
python test_telegram.py

# 執行
python fdkc_monitor.py
```

## 🔒 安全性提醒

### ⚠️ 絕對不要上傳的檔案：
- ❌ `config.json` - 包含你的 Telegram Token 和 Chat ID
- ❌ `notified_cases.json` - 個人使用快取
- ❌ `*.log` - 日誌檔案

這些已經在 `.gitignore` 中設定好了。

### 🛡️ 如果不小心上傳了敏感資訊：

**立即採取行動：**

1. **撤銷 Telegram Bot Token**
   ```
   - 在 Telegram 找 @BotFather
   - 發送 /revoke
   - 選擇你的 Bot
   - 取得新的 Token
   ```

2. **從 GitHub 移除**
   ```bash
   # 從 Git 歷史移除檔案
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch config.json" \
     --prune-empty --tag-name-filter cat -- --all
   
   # 強制推送
   git push origin --force --all
   ```

3. **更新 config.json**
   - 使用新的 Token
   - 確認檔案在 .gitignore 中

## 🌟 專案維護

### 更新專案
```bash
# 修改檔案後
git add .
git commit -m "描述你的改動"
git push
```

### 加入新功能
```bash
# 建立新分支
git checkout -b feature/新功能名稱

# 開發...

# 提交更改
git commit -am "加入新功能：XXX"

# 推送分支
git push origin feature/新功能名稱

# 在 GitHub 建立 Pull Request
```

### 發布版本
```bash
# 建立標籤
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0

# 在 GitHub 建立 Release
# 到 Releases → Draft a new release
# 選擇標籤 v1.0.0
# 填寫更新說明
# 發布
```

## 📊 GitHub Actions（進階）

可以加入自動化測試：

建立 `.github/workflows/test.yml`:

```yaml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: python -m py_compile fdkc_monitor.py
```

## 🤝 接受貢獻

在 README.md 加入：

```markdown
## 🤝 貢獻

歡迎 Pull Request！

1. Fork 這個專案
2. 建立你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改動 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request
```

## 📝 授權

這個專案使用 MIT License，意味著：
- ✅ 可以商用
- ✅ 可以修改
- ✅ 可以分發
- ✅ 可以私人使用
- ⚠️ 需要保留版權聲明

## 🎉 完成！

你的專案現在已經在 GitHub 上了！分享連結：
```
https://github.com/你的帳號/fdkc-monitor
```

---

**需要協助？** 查看 [GitHub Docs](https://docs.github.com/)
