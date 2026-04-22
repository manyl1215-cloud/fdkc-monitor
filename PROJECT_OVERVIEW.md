# 🎯 專案總覽

## 基隆市消防局案件監控系統

**完整的 Python 自動化監控程式，隨時掌握基隆消防局的車禍和火警案件。**

---

## 📦 專案包含的檔案

### 🔧 核心程式
| 檔案 | 說明 | 大小 |
|------|------|------|
| `fdkc_monitor.py` | 主程式 - 監控和通知邏輯 | 10KB |
| `test_telegram.py` | Telegram 連線測試工具 | 3KB |
| `start.sh` | 自動啟動腳本（Linux/Mac） | 1KB |

### 📋 設定檔
| 檔案 | 說明 |
|------|------|
| `requirements.txt` | Python 套件依賴 |
| `config.example.json` | 設定檔範例 |
| `.gitignore` | Git 忽略檔案 |

### 🐳 容器化部署
| 檔案 | 說明 |
|------|------|
| `Dockerfile` | Docker 映像建置檔 |
| `docker-compose.yml` | Docker Compose 配置 |

### 📖 文件
| 檔案 | 說明 |
|------|------|
| `README.md` | 完整使用說明（5.4KB） |
| `QUICKSTART.md` | 5 分鐘快速上手指南 |
| `PROJECT_STRUCTURE.md` | 專案結構說明 |
| `GITHUB_DEPLOY.md` | GitHub 部署指南 |
| `LICENSE` | MIT 開源授權 |

---

## ✨ 核心功能

### 🔍 智慧監控
- ✅ 每 10 分鐘自動檢查基隆消防局網站
- ✅ 精準篩選車禍和火警案件
- ✅ 智慧去重避免重複通知
- ✅ 完整的錯誤處理機制

### 📱 即時通知
- ✅ 透過 Telegram 即時推送
- ✅ 格式化的訊息內容（包含時間、地點、分隊、狀況）
- ✅ 支援圖示區分案件類型（🚗 車禍 / 🔥 火警）

### 💾 資料管理
- ✅ 本地快取已通知案件
- ✅ 完整的執行日誌
- ✅ 自動清理舊資料

### 🚀 多種部署方式
- ✅ 直接執行（Python）
- ✅ Docker 容器化
- ✅ Docker Compose 一鍵部署
- ✅ Systemd 服務（Linux）

---

## 🎯 使用場景

### 👤 個人使用
- 關注家人通勤路段的交通事故
- 即時掌握住家附近的緊急事件
- 新聞工作者追蹤突發新聞

### 🏢 專業應用
- 保險公司快速反應理賠案件
- 道路救援公司即時出勤
- 媒體記者掌握第一手新聞

### 🎓 學習研究
- Python 網頁爬蟲實作範例
- Telegram Bot 開發教學
- 自動化監控系統架構

---

## 🛠️ 技術棧

| 技術 | 用途 |
|------|------|
| **Python 3.8+** | 主要程式語言 |
| **requests** | HTTP 請求 |
| **BeautifulSoup4** | HTML 解析 |
| **python-telegram-bot** | Telegram Bot API |
| **schedule** | 任務排程 |
| **Docker** | 容器化部署 |

---

## ⚡ 快速開始（3 步驟）

### 1️⃣ 取得程式
```bash
git clone https://github.com/你的帳號/fdkc-monitor.git
cd fdkc-monitor
```

### 2️⃣ 安裝設定
```bash
pip install -r requirements.txt
cp config.example.json config.json
# 編輯 config.json 填入 Telegram 資訊
```

### 3️⃣ 執行
```bash
python fdkc_monitor.py
```

完成！🎉

詳細步驟請參考 [QUICKSTART.md](QUICKSTART.md)

---

## 📚 文件導讀

### 新手入門
1. 先看 **QUICKSTART.md** - 5 分鐘快速上手
2. 遇到問題查 **README.md** - 完整說明和故障排除

### 進階使用
1. **PROJECT_STRUCTURE.md** - 了解專案架構
2. **GITHUB_DEPLOY.md** - 發布到 GitHub
3. 直接看程式碼 - 程式碼有詳細註解

### 部署相關
- Docker 使用者 → 看 `docker-compose.yml`
- Linux 伺服器 → 看 README.md 的 systemd 章節
- Windows 使用者 → 看 README.md 的背景執行章節

---

## 🎁 特色亮點

### ✅ 開箱即用
- 無需複雜設定
- 完整的範例檔案
- 詳細的說明文件

### ✅ 穩定可靠
- 完整的錯誤處理
- 自動重試機制
- 詳細的日誌記錄

### ✅ 易於擴展
- 模組化設計
- 清晰的程式碼結構
- 豐富的註解說明

### ✅ 多平台支援
- Windows / Linux / macOS
- Docker 容器
- 雲端伺服器

---

## 📊 系統需求

### 最低需求
- Python 3.8 或更高版本
- 穩定的網路連線
- 約 50MB 硬碟空間

### 建議配置
- Python 3.11+
- 長期運行的伺服器或電腦
- Telegram 帳號和 Bot

---

## 🔐 安全性

- ✅ 不儲存敏感資料
- ✅ 本地執行，無需雲端服務
- ✅ 開源程式碼，可自行審查
- ✅ MIT 授權，自由使用

**注意：**
- ❌ 切勿分享你的 Telegram Bot Token
- ❌ 不要將 config.json 上傳到公開倉庫
- ✅ 定期更新依賴套件

---

## 📈 專案統計

- 📝 總程式碼行數：~300 行
- 📄 文件字數：~8000 字
- 🐍 Python 檔案：3 個
- 📋 設定檔：4 個
- 🐳 Docker 檔案：2 個
- 📖 說明文件：5 個

---

## 🤝 貢獻指南

歡迎貢獻！你可以：
- 🐛 回報 Bug
- 💡 提出新功能建議
- 📝 改善文件
- 🔧 提交 Pull Request

詳見 [README.md](README.md) 的貢獻章節。

---

## 📞 支援與協助

### 遇到問題？
1. 查看 **README.md** 故障排除章節
2. 檢查 `fdkc_monitor.log` 日誌
3. 在 GitHub 開 Issue

### 需要功能？
- 在 GitHub Issues 提出建議
- Fork 專案自行開發
- 提交 Pull Request

---

## 🌟 專案亮點總結

| 特點 | 說明 |
|------|------|
| 🎯 **目標明確** | 專注於車禍和火警監控 |
| 🚀 **易於使用** | 5 分鐘完成設定 |
| 📱 **即時通知** | Telegram 推送不漏訊 |
| 🔧 **高度自訂** | 可調整監控頻率和案件類型 |
| 🐳 **容器化** | 支援 Docker 部署 |
| 📝 **文件完整** | 從入門到進階全覆蓋 |
| 🔓 **開源免費** | MIT License |

---

## 📜 版本歷程

### v1.0.0 (2024)
- ✨ 首次發布
- 🚗 支援車禍監控
- 🔥 支援火警監控
- 📱 Telegram 通知整合
- 🐳 Docker 支援
- 📖 完整文件

---

## 📄 授權

MIT License - 可自由使用、修改、分發

詳見 [LICENSE](LICENSE) 檔案

---

## 🎉 開始使用

準備好了嗎？從 **QUICKSTART.md** 開始你的監控之旅！

```bash
# 克隆專案
git clone https://github.com/你的帳號/fdkc-monitor.git

# 開始設定
cd fdkc-monitor
cat QUICKSTART.md
```

**祝使用愉快！** 🚒🚗📱

---

*最後更新：2024 年 4 月*
