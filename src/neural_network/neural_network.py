"""
ファイル名: neural_network.py
概要:
    Iris（あやめ）データセットの先頭 100サンプルを読み込み、
    単純な 2–2–1 構造のフィードフォワードニューラルネットワークで分類を行い、
    分類結果を PDF に保存するスクリプトです。

使用方法:
    コマンドラインから実行してください。
    例) python neural_network.py
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import os
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
from matplotlib.backends.backend_pdf import PdfPages

iris = datasets.load_iris()
iris_data = iris.data
sl_data = iris_data[:100, 0]  # SetosaとVersicolor、Sepal length
sw_data = iris_data[:100, 1]  # SetosaとVersicolor、Sepal width


# 平均値を0に
sl_ave = np.average(sl_data)
sl_data -= sl_ave
sw_ave = np.average(sw_data)
sw_data -= sw_ave

# 入力をリストに格納
input_data = [[x, y] for x, y in zip(sl_data, sw_data)]


# シグモイド関数
def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


class Neuron:
    def __init__(self):
        self.input_sum = 0.0
        self.output = 0.0

    def set_input(self, inp):
        self.input_sum += inp

    def get_output(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0


class NeuralNetwork:
    def __init__(self):
        # 重みを設定
        self.w_im = [[4.0, 4.0], [4.0, 4.0]]
        self.w_mo = [[1.0, -1.0]]

        # バイアスを設定
        self.b_m = [2.0, -2.0]
        self.b_o = [-0.5]

        # 各層の宣言
        self.input_layer = [0.0, 0.0]
        self.middle_layer = [Neuron(), Neuron()]
        self.output_layer = [Neuron()]

    def commit(self, input_data):
        # 各層のリセット
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]
        self.middle_layer[0].reset()
        self.middle_layer[1].reset()
        self.output_layer[0].reset()

        # 入力層 to 中間層0
        self.middle_layer[0].set_input(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].set_input(self.input_layer[1] * self.w_im[0][1])
        self.middle_layer[0].set_input(self.b_m[0])

        # 入力層 to 中間層1
        self.middle_layer[1].set_input(self.input_layer[0] * self.w_im[1][0])
        self.middle_layer[1].set_input(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].set_input(self.b_m[1])

        # 中間層 to 出力層
        self.output_layer[0].set_input(
            self.middle_layer[0].get_output() * self.w_mo[0][0]
        )
        self.output_layer[0].set_input(
            self.middle_layer[1].get_output() * self.w_mo[0][1]
        )
        self.output_layer[0].set_input(self.b_o[0])

        return self.output_layer[0].get_output()


def main():
    # ニューラルネットワークのインスタンス
    neural_network = NeuralNetwork()

    # 実行
    st_predicted = [[], []]  # Satosa
    vc_predicted = [[], []]  # Versicolor
    for data in input_data:
        if neural_network.commit(data) < 0.5:
            st_predicted[0].append(data[0] + sl_ave)
            st_predicted[1].append(data[1] + sw_ave)
        else:
            vc_predicted[0].append(data[0] + sl_ave)
            vc_predicted[1].append(data[1] + sw_ave)

    # ファイルパス定義
    SCRIPT_DIR = Path(__file__).resolve().parent
    dir = SCRIPT_DIR.parents[1] / "outputs" / "neural_network"
    os.makedirs(dir, exist_ok=True)
    now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%dT%H%M%S")
    file_name = "neural-network_" + str(now) + ".pdf"
    file_path = dir / file_name

    # 分類結果をPDF保存
    plt.scatter(st_predicted[0], st_predicted[1], label="Setosa")
    plt.scatter(vc_predicted[0], vc_predicted[1], label="Versicolor")
    plt.legend()

    plt.xlabel("Sepal length (cm)")
    plt.ylabel("Sepal width (cm)")
    plt.title("Predictged")

    with PdfPages(file_path) as pdf:
        pdf.savefig()
        plt.close()
    plt.close()

    print(file_path, " にグラフが保存されました。")


if __name__ == "__main__":
    main()
