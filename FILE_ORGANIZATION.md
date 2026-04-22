# 📁 如何組織和上傳檔案

## 📂 檔案結構

上傳到 GitHub 時，檔案應該這樣組織：

```
你的倉庫根目錄/
│
├── .github/
│   └── workflows/
│       └── monitor.yml          ← GitHub Actions 設定檔
│
├── fdkc_monitor.py              ← 主程式
├── test_telegram.py             ← 測試工具
├── requirements.txt             ← Python 套件清單
├── config.example.json          ← 設定檔範例
├── .gitignore                   ← Git 忽略檔案
├── LICENSE                      ← 授權
├── README.md                    ← 說明文件
├── QUICKSTART.md                ← 快速指南
├── GITHUB_UPLOAD_GUIDE.md       ← GitHub 上傳指南
└── PROJECT_OVERVIEW.md          ← 專案概覽
```

---

## 🎯 重點：.github/workflows/monitor.yml

這個檔案的位置很重要！必須放在：
```
.github/workflows/monitor.yml
```

**在 GitHub 網頁上建立：**

1. 點擊 **Add file** → **Create new file**

2. 在檔名欄位輸入（注意是斜線，會自動建立資料夾）：
   ```
   .github/workflows/monitor.yml
   ```

3. 複製 `monitor.yml` 的內容貼上

4. Commit

**或者分步驟建立：**

1. 建立 `.github` 資料夾（新增檔案時輸入 `.github/temp.txt`）
2. 建立 `workflows` 資料夾（新增檔案時輸入 `.github/workflows/temp.txt`）
3. 建立 `monitor.yml`（新增檔案時輸入 `.github/workflows/monitor.yml`）
4. 刪除 temp.txt

---

## ✅ 上傳順序建議

### 第 1 批：主要檔案
```
fdkc_monitor.py
test_telegram.py
requirements.txt
config.example.json
.gitignore
LICENSE
README.md
```

### 第 2 批：文件
```
QUICKSTART.md
GITHUB_UPLOAD_GUIDE.md
PROJECT_OVERVIEW.md
PROJECT_STRUCTURE.md
```

### 第 3 批：GitHub Actions
```
.github/workflows/monitor.yml
```

---

## 📝 各檔案說明

### 核心檔案（必須）

**fdkc_monitor.py**
- 主程式
- 已修改支援 GitHub Actions
- 可本地執行或雲端執行

**requirements.txt**
- Python 套件清單
- GitHub Actions 會自動安裝

**monitor.yml**
- GitHub Actions 工作流程設定
- 定時執行監控

**.gitignore**
- 防止上傳 config.json
- 保護你的 Token 安全

### 設定檔

**config.example.json**
- 設定檔範例
- 上傳到 GitHub
- 使用者下載後複製成 config.json

**config.json**
- 你的真實設定
- ❌ 不要上傳到 GitHub
- 只存在本地電腦

### 文件檔案（建議）

**README.md**
- 專案說明
- 安裝和使用指南

**GITHUB_UPLOAD_GUIDE.md** ⭐
- GitHub 上傳和執行完整教學
- 一步步帶你完成設定

**QUICKSTART.md**
- 5 分鐘快速上手

**PROJECT_OVERVIEW.md**
- 專案概覽

---

## 🚫 不要上傳的檔案

```
❌ config.json           （包含你的 Token）
❌ notified_cases.json   （本地快取）
❌ fdkc_monitor.log      （日誌檔案）
❌ __pycache__/          （Python 快取）
```

這些已經在 `.gitignore` 中設定好，Git 會自動忽略。

---

## 🔍 檢查清單

上傳前確認：

- [ ] ✅ fdkc_monitor.py 已上傳
- [ ] ✅ requirements.txt 已上傳
- [ ] ✅ config.example.json 已上傳（不是 config.json）
- [ ] ✅ .gitignore 已上傳
- [ ] ✅ .github/workflows/monitor.yml 已建立
- [ ] ❌ config.json 沒有上傳（確認！）
- [ ] ✅ 可以在倉庫看到所有檔案

---

## 💡 快速檢查方法

**在你的 GitHub 倉庫頁面：**

1. 看到 `.github` 資料夾嗎？
   - 點進去 → workflows → 應該有 monitor.yml

2. 看到 `config.json` 嗎？
   - ❌ 如果看到 = 立即刪除！（包含機密資訊）
   - ✅ 只應該看到 config.example.json

3. 看到這些檔案嗎？
   - ✅ fdkc_monitor.py
   - ✅ requirements.txt
   - ✅ README.md

全部確認後就可以進行下一步：設定 GitHub Secrets！

---

## 🎬 下一步

檔案上傳完成後：

1. **設定 GitHub Secrets**（存放 Token 和 Chat ID）
2. **手動執行測試**（Actions 頁面）
3. **檢查執行日誌**
4. **等待 Telegram 通知**

詳細步驟請看 **GITHUB_UPLOAD_GUIDE.md**！

---

## ❓ 常見問題

**Q: monitor.yml 要放在哪裡？**  
A: `.github/workflows/monitor.yml`（路徑很重要）

**Q: 為什麼我的 Actions 頁面是空的？**  
A: 可能 monitor.yml 路徑不對，確認是否在 `.github/workflows/` 下

**Q: 可以用 ZIP 上傳嗎？**  
A: 建議個別上傳檔案，這樣結構更清楚

**Q: 我改了檔案怎麼更新？**  
A: 點擊檔案 → 鉛筆圖示編輯 → Commit changes

祝上傳順利！🎉
