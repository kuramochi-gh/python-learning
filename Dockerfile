# ベースイメージとして公式のPythonイメージを使用
FROM python:3.13

# 作業ディレクトリを設定
WORKDIR /app

# パッケージインストール
RUN apt update &&\
    apt install -y  --no-install-recommends \
    tree && \
    rm -rf /var/lib/apt/lists/*

# 依存関係インストール
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# コンテナ起動時のデフォルトコマンド
CMD ["python", "--version"]
