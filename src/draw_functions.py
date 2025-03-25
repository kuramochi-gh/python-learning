import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# データ作成
x = np.linspace(-5, 5)
y = 2*x + 1

# グラフ描画
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="y = 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function: y = 2x + 1")
plt.legend()
plt.grid(True)

# PDFに保存する
with PdfPages("linear_graph.pdf") as pdf:
    pdf.savefig()
plt.close()

print("'linear_graph.pdf' にグラフが保存されました。")
