# MCPサーバー用Dockerfile (get_weather.py)
FROM python:3.13-slim

# 作業ディレクトリ設定
WORKDIR /app

# 依存関係インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションファイルをコピー
COPY get_weather.py .

# コンテナ起動時にMCPサーバー実行
CMD ["sh", "-c", "python get_weather.py"]
