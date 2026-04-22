FROM python:3.11-slim

WORKDIR /app

# 安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式
COPY fdkc_monitor.py .

# 建立資料目錄
RUN mkdir -p /app/data

# 設定時區（台北時間）
ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 運行程式
CMD ["python", "-u", "fdkc_monitor.py"]
