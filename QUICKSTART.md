# 🚀 快速啟動指南

## ✅ 已完成設置

環境已經配置完成！所有依賴套件已使用 `uv` 安裝在虛擬環境中。

## 📦 已安裝的套件

核心套件：
- ✅ FastAPI 0.109.0
- ✅ Uvicorn 0.27.0
- ✅ Jinja2 3.1.2
- ✅ SQLAlchemy 2.0.23
- ✅ Pydantic 2.5.3

完整套件列表請查看 `requirements.txt`

## 🎯 啟動方式

### 方法 1：使用快速啟動腳本（推薦）

```bash
./start.sh
```

### 方法 2：手動啟動

```bash
# 啟動虛擬環境
source .venv/bin/activate

# 啟動伺服器
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 方法 3：使用 uv 直接運行

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🌐 訪問網站

伺服器啟動後，在瀏覽器中訪問以下網址：

- **主頁**: http://localhost:8000/
- **紀錄**: http://localhost:8000/record
- **靈修**: http://localhost:8000/devotion
- **個人**: http://localhost:8000/profile

## 📱 功能展示

### 主頁 (/)
- 顯示當前聚會資訊（主理、司會、司琴等）
- 參加/不參加按鈕
- 待辦事項列表（含完成狀態）

### 紀錄 (/record)
- 過去聚會卡片列表
- 每個卡片包含標題、日期和佔位圖片
- 從新到舊排序

### 靈修 (/devotion)
- YouTube 影片佔位區（16:9 比例）
- 本日金句顯示
- 靈修筆記輸入區

### 個人 (/profile)
- 使用者頭像和基本資訊
- 暱稱列表
- Google 帳號綁定列表

## 🛠️ 開發工具

### 重新安裝依賴

```bash
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 更新虛擬環境

```bash
# 刪除舊環境
rm -rf .venv

# 建立新環境
uv venv

# 安裝依賴
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 檢查程式碼

```bash
source .venv/bin/activate

# 格式化程式碼
black app/

# 檢查語法
flake8 app/

# 型別檢查
mypy app/
```

## 🔧 常見問題

### 端口被佔用

```bash
# 終止佔用 8000 端口的進程
lsof -ti:8000 | xargs kill -9
```

### 虛擬環境未啟動

確保每次執行前都啟動虛擬環境：
```bash
source .venv/bin/activate
```

### 套件未找到

重新安裝依賴：
```bash
uv pip install -r requirements.txt
```

## 📝 目前狀態

✅ **已完成**：
- 基礎 UI 骨架
- 4 個主要頁面（主頁、紀錄、靈修、個人）
- 底部導航列
- 響應式設計（手機優先）
- 假資料展示

❌ **未實作**：
- 資料庫連接
- 使用者認證
- NFC/QR Code 簽到
- YouTube API 整合
- Google OAuth
- 表單提交功能
- 資料持久化

## 🎨 技術堆疊

- **後端**: FastAPI + Python 3.12
- **模板引擎**: Jinja2
- **樣式**: Tailwind CSS (CDN)
- **套件管理**: uv
- **開發伺服器**: Uvicorn

## 📚 相關文件

- `SYSTEM_REQUIREMENTS.md` - 系統需求完整文件
- `UI_SKELETON_README.md` - UI 骨架詳細說明
- `README.md` - 專案總覽

---

**版本**: 0.1.0  
**狀態**: ✅ 開發環境已就緒  
**最後更新**: 2025-12-06
