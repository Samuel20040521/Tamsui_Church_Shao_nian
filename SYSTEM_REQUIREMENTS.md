# SYSTEM_REQUIREMENTS.md

*Version 0.1 – Draft*
此文件為系統之初始規格文件，後續將依實際開發與需求變更持續更新。

---

# 1. 產品與功能需求（Product Requirements）

## 1.1 目標與背景

本系統旨在提供教會或團契聚會使用，整合：

* 聚會點名（NFC 刷卡 / 動態 QRCode）
* 聚會紀錄（每週聚會內容 + 圖片）
* 靈修內容整合（每日 YouTube 影片 + 筆記 + 金句）
* 個人設定（暱稱、頭像、多 Google 帳號綁定）
* 活動模式（如 KTV 點歌與播放管理）

系統需支援手機優先版面，並可部署於 Raspberry Pi（4/5）上運行。

## 1.2 使用者角色

* **一般成員**：

  * 回覆本次聚會是否參加
  * 查看聚會紀錄
  * 使用靈修功能
  * 修改個人資料
  * 點歌（活動模式）

* **幹部 / 管理者 / 小組長**：

  * 編輯聚會內容
  * 管理出席紀錄
  * 管理週次記錄與照片
  * 管理活動（如 KTV）排程與佇列

* **系統管理員（選配）**：

  * 系統層級設定、資料備份、權限管理

---

## 1.3 導覽結構（底部 Tab）

系統採 Spotify 類似的底部四個選單：

1. **主頁**
2. **紀錄**
3. **靈修**
4. **個人**

---

## 1.4 主頁（Home）

### 版面結構

1. **聚會內容 Block（畫面前 1/3）**

   * 顯示欄位：

     * 主理
     * 司會
     * 司琴
     * 聚會時間、地點（可選）
   * 互動：

     * **勾勾（參加）**
     * **叉叉（不參加）**
   * 狀態切換後需立即更新 UI（可用 htmx）

2. **TODO 區域（畫面後 2/3）**

   * 目前為 template
   * 可用於顯示：

     * 聚會前提醒
     * 服事提醒
     * 代禱事項
     * 任務列表

---

## 1.5 紀錄（Record）

### 功能描述

* 以「由近到遠」排序顯示過去聚會
* 每週一個「聚會紀錄卡」，包含：

  * 聚會主題
  * 日期
  * 聚會照片（取代原本主頁的勾勾 / 叉叉）
* 點擊可展開完整紀錄（之後可加入更多資訊）

### UI 行為

* 無限捲動或分頁顯示
* 卡片風格需統一（類似主頁 block）

---

## 1.6 靈修（Devotion）

### 內容來源

* 每天固定抓取 YouTube 頻道「JAM 愛的影響力」最新影片
* 預計影片出現時間範圍：早上 6:00–7:00
* 嵌入影片於頁面最上方

### 其他內容

* **本日金句**（可由管理端編輯或自動抓取來源 TBD）
* **個人靈修筆記**

  * 文字輸入區
  * 可即時儲存（AJAX / htmx）

---

## 1.7 個人（Profile）

### 功能描述

* 編輯個人資料：

  * 暱稱（多個）
  * 頭像（上傳或自動生成）
* Google 帳號綁定：

  * 可綁定多個 Google 帳號
  * 採 OAuth 2.0（待選）

---

# 2. UI / UX 規格

## 2.1 整體風格

* 主色系：柔和、避免過亮
* 字體：系統字體（San-serif）
* 手機版優先
* 清楚、簡潔、類 Spotify / LINE 清爽風格

## 2.2 底部導覽列

* 四個按鈕：主頁、紀錄、靈修、個人
* icon + 文字
* 點擊後切換頁面，不必整頁重整（建議使用 htmx）

## 2.3 主頁 UI 要求

* 聚會 block 高度約佔上半區域
* 勾 / 叉按鈕需清晰可見
* TODO 列表用卡片方式呈現

## 2.4 紀錄 UI 要求

* 每週卡片高度一致
* 圖片比例與邊距固定
* 排序由最新到最舊

## 2.5 靈修 UI

* YouTube 區塊固定在頂部
* 金句區為明顯的文字框
* 下方為筆記輸入區

## 2.6 個人 UI

* 頭像置頂
* 暱稱列表可編輯
* Google 帳號以列表呈現，支援新增 / 移除

---

# 3. 技術與工具（Tech Stack）

## 3.1 後端

* **Python 3.10+**
* **FastAPI**
* **Jinja2**（頁面模板）
* **htmx**（前端互動）
* **SQLAlchemy**（資料庫 ORM）
* Optional：Alembic（schema migration）

## 3.2 前端

* **Tailwind CSS**
* Optional：Alpine.js（處理 modal / dropdown 等小互動）
* Icon 套件：Heroicons / Lucide（待選）

## 3.3 資料庫

* 預設：**SQLite**
* 之後可切換：PostgreSQL

## 3.4 外部服務 / API

* YouTube Data API（抓取影片）
* Google OAuth（綁定多帳號）

## 3.5 硬體整合（若與 NFC / KTV 合併）

* **Raspberry Pi 4 / 5**
* **ACR122U NFC 讀卡機**（ISO14443A）
* Mixer + 麥克風（KTV）
* 相關 Python 套件：

  * `nfcpy` / `pyscard`
  * `qrcode`

---

# 4. 程式架構與 Code Style

## 4.1 專案檔案架構（建議）

```
app/
  main.py
  routers/
    home.py
    record.py
    devotion.py
    profile.py
    ktv.py
    attendance.py
  templates/
    home.html
    record.html
    devotion.html
    profile.html
    components/
  static/
    css/
    js/
  models/
    user.py
    gathering.py
    record.py
    devotion.py
    profile.py
    ktv.py
  schemas/
    user.py
    ...
```

## 4.2 後端程式風格

* 遵守 PEP 8
* 分離 router / service / model
* 個別功能獨立為模組（例如 attendance、ktv）

## 4.3 前端程式風格

* 多使用 Tailwind utility classes
* 避免大量自定義 CSS
* htmx 應回傳 partial HTML 做 UI 更新

  * 如 `hx-target="#queue"`
  * `hx-swap="innerHTML"`

## 4.4 錯誤處理

* 使用 FastAPI exception handler
* 重要行為記錄 log（出席、點歌、登入）

---

# 5. 資料模型（Data Model / ERD 草案）

## 5.1 主要資料實體（高階列表）

### 使用者相關

* **User**（使用者）
* **UserProfile**（暱稱、頭像）
* **UserGoogleBinding**（多 Google 帳號）

### 聚會點名

* **Gathering**（聚會內容）
* **Attendance**（出席狀態：參加 / 不參加 / 未回覆）

### 聚會紀錄

* **RecordPost**（每週一張圖片）
* **RecordComment**
* **RecordLike**

### 靈修

* **DevotionVideo**（抓取自 YouTube）
* **DevotionNote**（使用者筆記）
* **DevotionVerse**（本日金句）

### 活動（KTV）

* **KtvSong**（歌曲資訊）
* **KtvQueue**（播放順序）

之後可以依你的進一步需求產生 ERD 圖。

---

# 6. 非功能需求（NFR）

## 6.1 效能

* 預期同時在線：< 50 人
* 樹莓派運作下仍需保持回應 < 500ms

## 6.2 安全

* Token 驗證（動態 QRCode）：有效期 10 秒
* Google OAuth 保護個人資料
* 出席資料需具備基本存取控制（僅管理者可修改）

## 6.3 備份與維運

* SQLite 定期備份（每日或每週）
* 若日後換 PostgreSQL，需行 migration
* 樹莓派需 systemd 自動啟動 API

---

# 7. 待確認項目（需你回答）

### 聚會 / 主頁

1. 勾 / 叉是否會影響後台出席資料？
2. 出席是否允許「稍後再決定」第三狀態？

### 靈修

3. 本日金句是自動取得還是後台人工輸入？
4. 靈修筆記是否需要版本紀錄？

### 個人

5. 頭像是否支援相簿上傳？尺寸限制？
6. 多 Google 帳號綁定是否會影響登入方式？

### 紀錄

7. 每週照片由誰上傳？（管理者 / 自動來源）
8. 是否允許多張照片？

### KTV（若保留此功能）

9. 點歌是否需要登入？
10. 點歌可否匿名？
11. 是否要記錄「誰唱這首」？

---

# 8. 版本紀錄（Changelog）

* v0.1 – 初稿生成（依照目前所有需求整理）
