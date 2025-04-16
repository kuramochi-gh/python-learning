# ベースイメージとして公式のPythonイメージを使用
FROM python:3.13

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係インストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# コンテナ起動時のデフォルトコマンド
CMD ["python", "--version"]
