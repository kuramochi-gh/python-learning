"""
ファイル名: draw_functions.py
概要:
    ユーザが入力した引数に従って、関数のグラフを描画したPDFを出力します。

使用方法:
    コマンドラインから実行してください。
    引数としてx軸の開始位置、x軸の終了位置、"y="に続く数式を与えてください。
    数式は複数受け付けます。
    例1) python draw_functions.py -5 5 "2*x + 1"
    例2) python draw_functions.py -4 4 "2*x + 1" "x**2 -4" "0.5*x**3 - 6*x"

"""

import sys
from sympy import symbols, sympify, lambdify
import numpy as np
import matplotlib.pyplot as plt
import inflect
from datetime import datetime
from zoneinfo import ZoneInfo
from matplotlib.backends.backend_pdf import PdfPages


def make_graph_pdf(x_start, x_end, formulas):
    """グラフを描画したPDFを作成する"""
    # データ作成
    x = np.linspace(x_start, x_end)
    y_list = []

    for f in formulas:
        y_list.append(evaluate_formula(x, f))

    # グラフ描画
    plt.figure(figsize=(8, 6))
    p = inflect.engine()
    i = 1
    for y in y_list:
        plt.plot(x, y, label=p.ordinal(i))
        i += 1

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Function: y = " + ", y = ".join(formulas))
    plt.legend()
    plt.grid(True)

    # PDFに保存する
    now = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%dT%H%M%S")
    file_name = "draw_functions" + str(now) + ".pdf"
    with PdfPages(file_name) as pdf:
        pdf.savefig()
    plt.close()

    print(file_name, " にグラフが保存されました。")


def evaluate_formula(x, formula):
    """数式として評価する"""
    x_symbol = symbols("x")
    try:
        expr = sympify(formula)
        func = lambdify(x_symbol, expr, "numpy")
        return func(x)
    except Exception as e:
        print("数式の評価に失敗しました:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("error: 引数の数が異なります")
        sys.exit(1)

    try:
        x_start = float(sys.argv[1])
        x_end = float(sys.argv[2])
    except ValueError:
        print("error: 第二引数または第三引数に数値以外が入力されています")
        print("第二引数: ", sys.argv[1])
        print("第三引数: ", sys.argv[2])
        sys.exit(1)

    length = len(sys.argv)
    formulas = []
    for i in range(3, length):
        formulas.append(sys.argv[i])

    make_graph_pdf(x_start, x_end, formulas)
