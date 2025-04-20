"""
ファイル名: external_data.py
概要:
    Iris（あやめ）データセットの先頭 100サンプルを読み込み、
    単一ニューロンモデル（feedforward）で
    SetosaとVersicolor（品種名）の 2 クラス分類を実行します。
    分類結果と元データの散布図をMatplotlibで描画し、
    PdfPagesを使って同一PDFに
    「Predicted」「Original」の2ページを出力します。
    single_neuron.pyのNeuronクラスを基に
    サブクラスとしてResettableNeuronクラスを定義しています。

使用方法:
    コマンドラインから実行してください。
    例) python external_data.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from datetime import datetime
from zoneinfo import ZoneInfo
from matplotlib.backends.backend_pdf import PdfPages
import os
from pathlib import Path
from single_neuron import Neuron

iris = datasets.load_iris()
iris_data = iris.data
sl_data = iris_data[:100, 0]
sw_data = iris_data[:100, 1]

# 平均値を0に
sl_ave = np.average(sl_data)
sl_data -= sl_ave
sw_ave = np.average(sw_data)
sw_data -= sw_ave

# 入力をリストに格納
input_data = []
for i in range(100):
    input_data.append([sl_data[i], sw_data[i]])


# シグモイド関数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


class ResettableNeuron(Neuron):
    def reset(self):
        self.input_sum = 0
        self.output = 0


class NeuralNetwork:
    def __init__(self):
        self.neuron = ResettableNeuron()

        # 重みを定義
        self.w = [0.5, -0.2]

        # バイアスを設定
        self.bias = 0.0

    def commit(self, input_data):
        self.neuron.reset()

        for i in range(len(input_data)):
            self.neuron.set_input(input_data[i] * self.w[i])
        self.neuron.set_input(self.bias)
        return self.neuron.get_output()


neural_network = NeuralNetwork()

st_predicted = [[], []]
vc_predicted = [[], []]

# ニューラルネットワークによる分類
for data in input_data:
    if neural_network.commit(data) < 0.5:
        st_predicted[0].append(data[0] + sl_ave)
        st_predicted[1].append(data[1] + sw_ave)
    else:
        vc_predicted[0].append(data[0] + sl_ave)
        vc_predicted[1].append(data[1] + sw_ave)

# 元データ（分類済み）
st_data = iris_data[:50]
vc_data = iris_data[50:100]

# ファイルパス定義
SCRIPT_DIR = Path(__file__).resolve().parent
dir = SCRIPT_DIR.parents[1] / "outputs" / "neural_network"
os.makedirs(dir, exist_ok=True)
now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%dT%H%M%S")
file_name = "external-data_" + str(now) + ".pdf"
file_path = dir / file_name

with PdfPages(file_path) as pdf:
    # ニューラルネットワークによる分類結果をPDFに保存
    fig1 = plt.figure()
    plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
    plt.scatter(vc_predicted[0], vc_predicted[1], label="Versicolor")
    plt.legend()
    plt.xlabel("Sepal length (cm)")
    plt.xlabel("Sepal width (cm)")
    plt.title("Predicted")
    pdf.savefig(fig1)
    plt.close(fig1)

    # 比較用に元データ（分類済み）の散布図もPDFに保存
    fig2 = plt.figure()
    plt.scatter(st_data[:, 0], st_data[:, 1], label="Setosa")
    plt.scatter(vc_data[:, 0], vc_data[:, 1], label="Versicolor")
    plt.legend()
    plt.xlabel("Sepal length (cm)")
    plt.xlabel("Sepal width (cm)")
    plt.title("Original")
    pdf.savefig(fig2)
    plt.close(fig2)
plt.close()

print(file_path, " にグラフが保存されました。")
