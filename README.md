# Python Learning Repository

![Python](https://img.shields.io/badge/Python-3.10%2B%20(3.13%20recommended)-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)

## リポジトリの目的

このリポジトリは、Pythonを用いた学習成果物をまとめたポートフォリオです。
Python学習を通じて実務で役立つスキルを磨くことを目的としています。
特に、以下を重点的に学びました：

- **最新技術の活用**: Model Context Protocol(MCP)を使用した、LLMアプリケーションと外部システムの連携。
- **データ処理と可視化**: 数式解析やグラフ生成によるデータ表現。
- **開発環境のモダン化**: Dockerによる再現可能な仮想環境の構築。

## セットアップ

全プロジェクトを動かすには、以下を準備してください：

- Python 3.10以上（Docker環境では3.13を使用）
- Docker（get_weather.py用）
- 必要ライブラリ：requirements.txtを参照

  ```bash
  pip install -r requirements.txt
  ```

---

## プロジェクト一覧

### 1. ニューラルネットワーク分類プログラム (`neural_network.py`, `external_data.py`, `single_neuron.py`)

**概要**:
Irisデータセットを用いたニューラルネットワークによる分類プログラム群です。以下3つのプログラムで構成されています：

- `single_neuron.py`: 単一ニューロン（パーセプトロン＋シグモイド活性化）による基本的なフィードフォワード処理を実装。コマンドラインから3つの数値を入力として受け取り、ニューロンの出力を計算します。
- `external_data.py`: 単一ニューロンモデルを拡張し、Irisデータセットの分類を行い、予測結果と元データの散布図を2ページのPDFとして出力します。
- `neural_network.py`: 2-2-1構造のフィードフォワードニューラルネットワークを構築し、IrisデータセットのSetosaとVersicolorを分類。分類結果を散布図としてPDFに保存します。

これらのプログラムを通じて、ニューラルネットワークの基礎、データ前処理、分類モデルの実装、結果の可視化を学習しました。

**技術スタック**:

- Python 3.10
- numpy
- matplotlib
- scikit-learn

**使用方法（Claude Desktopを使用する場合）**:

1. リポジトリをクローン：

   ```bash
   git clone <リポジトリURL>
   ```

2. 依存関係をインストール：

   ```bash
   cd python-learning/src/neural_network
   pip install -r requirements.txt
   ```

3. 各プログラムを実行：
   - `single_neuron.py`の実行例：

   ```bash
   python single_neuron.py 1 2 3
   # 3つの数値を引数として与えることで、演算結果が返却される
   ```

   - `external_data.py`の実行：

   ```bash
   python external_data.py
   # 予測結果と元データの散布図がPDFとしてoutputs/neural_network/に保存される
   ```

   - `neural_network.py`の実行：

   ```bash
   python neural_network.py
   # 分類結果の散布図がPDFとしてoutputs/neural_network/に保存
   ```

**実務での応用例**:

- 機械学習モデルの構築
- データ分類や予測モデルの構築
- 分析結果の可視化とレポート生成

### 2. 天気 API サーバー (`get_weather.py`)

**概要**:
Model Context Protocol(MCP)を用いた天気情報取得サーバーです。
OpenWeatherMap APIを使用し、LLMアプリケーションが都市名からリアルタイムの天気情報（気温、天気状況）を取得可能にします。
Docker環境で動作し、AIと外部システムの標準化されたデータ連携を実現します。

**技術スタック**:

- Python 3.10
- MCP
- httpx
- Docker
- OpenWeatherMap API

**使用方法（Claude Desktopを使用する場合）**:

1. リポジトリをクローン：

   ```bash
   git clone <リポジトリURL>
   ```

2. Dockerイメージをビルド：

   ```bash
   cd python-learning/src/get_weather
   docker build -t mcp-weather-server .
   ```

3. OpenWeatherMap API キーを取得（[公式サイト](https://openweathermap.org/)）。
4. Claude Desktopをインストール（[公式サイト](https://claude.ai/download)）。
5. Claude Desktopを起動し、 ファイル > 設定 > 開発者 > 構成を編集 を選択して設定フォルダを開く。
6. 開いたフォルダ内のclaude_desktop_config.jsonを編集：

   ```json
   {
      "mcpServers": {
         "get_weather": {
               "command": "docker",
               "args": [
                  "run",
                  "-i",
                  "--rm",
                  "-e",
                  "OPENWEATHER_API_KEY=ここにAPIキーを記載してください",
                  "mcp-weather-server"
               ]
         }
      }
   }
   ```

7. Claude Desktopを再起動。（バックグラウンドで動作している場合があるためタスクキル推奨）
8. 天気を質問するプロンプトを入力する。
   ![ClaudeDesktopImage](https://github.com/user-attachments/assets/aa9542b8-fa28-4581-97da-e4c85fe6dbbf)

**実務での応用例**:

- LLMアプリケーションと外部API（例: ニュース、DB）の統合
- 業務システムのリアルタイムデータ処理基盤

### 3. 関数グラフ描画ツール (`draw_functions.py`)

**概要**:
ユーザーが指定した数式に基づいて、関数のグラフをPDF形式で出力するツールです。複数の数式を同時に描画できます。データ可視化の基礎を学習しました。

**技術スタック**:

- Python 3.10
- matplotlib
- numpy

**使用方法**:

1. リポジトリをクローン：

   ```bash
   git clone <リポジトリURL>
   ```

2. 依存関係をインストール：

   ```bash
   cd python-learning/src/draw_function
   pip install -r requirements.txt
   ```

3. プログラムを実行（例）：

   ```bash
   cd python-learning/src/draw_function
   python draw_functions.py -5 5 "2*x + 1"
   python draw_functions.py -4 4 "2*x + 1" "x**2 -4" "0.5*x**3 - 6*x"
   ```

4. 出力されたPDFを確認。

**実務での応用例**:

- データ分析結果の可視化
- 教育ツールやレポート生成の自動化

### 4. 月日推測プログラム (`guess_date.py`)

**概要**:
ユーザーが想像した月日を、二分探索を用いて推測するプログラムです。Python文法の基礎とアルゴリズム設計・実装を学習しました。

**技術スタック**:

- Python 3.10

**使用方法**:

1. リポジトリをクローン：

   ```bash
   git clone <リポジトリURL>
   ```

2. プログラムを実行：

   ```bash
   cd python-learning/src/guess_date
   python guess_date.py
   ```

3. 画面の指示に従ってヒントを入力。二分探索を用いて月日が推測されます。

**実務での応用例**:

- 対話型システムへの応用
- 効率的なアルゴリズム設計・実装スキル

---

## ディレクトリ構成

```text
python-learning/
├── .devcontainer/             # 開発環境定義ファイル
├── .git/                      # git管理用
├── outputs/                   # 出力物（PDFなど）
│   ├── draw_functions/        # draw_functionsの出力先
│       ├── draw_functions20250327T235651.pdf # draw_functionsの出力例
│   ├── newral_network/        # newral_networkの出力先
│       ├── external-data_20250419T232548.pdf # external_dataの出力例
├── src/                       # ソースコードディレクトリ
│   ├── draw_functions/        # 関数グラフ描画
│   │   ├── draw_functions.py  # 関数グラフ描画コード
│   │   ├── requirements.txt   # draw_functions用の依存パッケージ
│   ├── get_weather/           # 天気取得APIサーバー
│   │   ├── get_weather.py     # 天気取得APIサーバーコード
│   │   ├── requirements.txt   # get_weather用の依存パッケージ
│   │   ├── Dockerfile         # get_weather用のDockerfile
│   ├── guess_date/            # 月日推測プログラム
│   │   ├── guess_date.py      # 月日推測プログラムコード
│   ├── newral_network/        # ニューラルネットワークプログラム
│   │   ├── external_data.py   # 外部データ追加プログラムコード
│   │   ├── neural_network.py  # ニューラルネットワークのプログラムコード
│   │   ├── requirements.txt   # newral_network用の依存パッケージ
│   │   ├── single_neuron.py   # 単一ニューロンプログラムコード
├── .gitignore                 # Git管理外の指定
├── Dockerfile                 # 全プロジェクトをカバーする開発用Dockerfile
├── README.md                  # リポジトリ説明（本ファイル）
├── requirements.txt           # 全プロジェクトの依存をまとめた開発用
```
