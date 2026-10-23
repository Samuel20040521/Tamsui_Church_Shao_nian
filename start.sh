#!/bin/bash
# 快速啟動腳本

echo "================================"
echo "淡水教會少年聚會系統"
echo "================================"
echo ""

# 切換到專案目錄
cd /Users/dengensheng/Developer/Tamsui_Church_Shao_nian

# 啟動虛擬環境
source .venv/bin/activate

# 啟動伺服器
echo "正在啟動伺服器..."
echo "訪問: http://localhost:8000"
echo ""
echo "頁面："
echo "  • 主頁:   http://localhost:8000/"
echo "  • 紀錄:   http://localhost:8000/record"
echo "  • 靈修:   http://localhost:8000/devotion"
echo "  • 個人:   http://localhost:8000/profile"
echo ""
echo "按 Ctrl+C 停止伺服器"
echo "================================"
echo ""

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
