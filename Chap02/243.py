#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv("sensor_data_600.txt", delimiter = " ",
                  header = None, names = ("data", "time", "ir", "lidar"))

# グラフの描画
data["hour"] = [e//10000 for e in data.time]  #hourly_mean,Note that "//"
d = data.groupby("hour")
d.lidar.mean().plot()

plt.show()