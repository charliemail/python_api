# 使用官方 Python 映像作為基礎映像
FROM python:3.9-slim

# 在容器裡建立目錄資料夾
RUN mkdir /python_api

# 將本地端資料複製到指定目錄資料夾位置
COPY . /python_api

# 指定容器預設工作位置
WORKDIR /python_api

# pip 將目前版本更至最新
RUN python -m pip install --no-cache-dir --upgrade pip

# 在 Image 中執行的指令：安裝 requirements.txt 中所指定的 dependencies
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

# 定義啟用命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]