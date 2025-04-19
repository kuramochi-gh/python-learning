"""
ファイル名: single_neuron.py
概要:
    コマンドライン引数から受け取った3つの数値を入力として、
    単一ニューロン（単純パーセプトロン + シグモイド活性化）による
    feedforward 処理を行うサンプル実装です。
    3入力 x 重み + バイアス のfeedforward計算を実装しています。

使用方法:
    コマンドラインから実行してください。
    引数として3つの数値を与えてください。
    例) python single_neuron.py 1 2 3
"""

import sys
import numpy as np


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


class NeuralNetwork:
    def __init__(self):
        self.neuron = Neuron()

        # 重みを定義
        self.w = [1.5, 0.75, -1.0]

        # バイアスを設定
        self.bias = 1.0

    def commit(self, input_data):
        for i in range(len(input_data)):
            self.neuron.set_input(input_data[i] * self.w[i])
        self.neuron.set_input(self.bias)
        return self.neuron.get_output()


def main():
    # インスタンス
    neural_network = NeuralNetwork()

    # 実行
    length = len(sys.argv)
    if length != 4:
        print(
            f"error: 引数の数が異なります。本ファイル名+数値（3つ）を引数に与えてください。引数の数: {length}"
        )
        sys.exit(1)

    nums = []
    for i in range(1, length):
        try:
            num = float(sys.argv[i])
        except ValueError:
            print("error: 引数に数値以外が入力されています")
            sys.exit(1)

        nums.append(num)

    input_data = nums
    print(neural_network.commit(input_data))


if __name__ == "__main__":
    main()
