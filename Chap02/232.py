#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import math
import matplotlib.pyplot as plt
import pandas as pd

# データの読み込み
data = pd.read_csv("sensor_data_200.txt", delimiter = " ",
                  header = None, names = ("data", "time", "ir", "lidar"))
freqs = pd.DataFrame(data["lidar"].value_counts())
freqs["probs"] = freqs["lidar"] / len(data["lidar"])

# 確率密度関数
mean1 = sum(data["lidar"].values)/len(data["lidar"].values)

zs = data["lidar"].values
mean = sum(zs) / len (zs)
diff_square = [(z -mean)**2 for z in zs]
sampling_var = sum(diff_square)/(len(zs))
stddev1 = math.sqrt(sampling_var)

# グラフの描画
from scipy.stats import norm

zs = range(190, 230)
ys = [norm.pdf(z, mean1, stddev1) for z in zs]

plt.plot(zs, ys)
plt.show()

ys = [norm.cdf(z, mean1, stddev1) for z in zs]

plt.plot(zs, ys, color = "red")
plt.show()

ys = [norm.cdf(z + 0.5, mean1, stddev1) - norm.cdf(z - 0.5, mean1, stddev1) for z in zs]

plt.bar(zs, ys)
plt.show()