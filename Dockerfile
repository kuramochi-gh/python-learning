# ベースイメージとして公式のPythonイメージを使用
FROM python:3.13

# 作業ディレクトリを設定
WORKDIR /app

# 必要に応じてPythonのライブラリを先にインストール
RUN pip install --no-cache-dir numpy matplotlib inflect sympy

# コンテナ起動時のデフォルトコマンド
CMD ["python", "--version"]
