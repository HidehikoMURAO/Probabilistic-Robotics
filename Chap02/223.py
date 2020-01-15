#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv("sensor_data_200.txt", delimiter = " ", 
        header = None, names = ("date", "time", "ir", "lidar"))

# 平均値の計算
mean1 = sum(data["lidar"].values)/len(data["lidar"].values)
mean2 = data["lidar"].mean()

# LiDARのセンサ値のヒストグラムの作成
data["lidar"].hist(bins = max(data["lidar"]) - min(data["lidar"]), 
        color="orange", align = 'left')
plt.vlines(mean1, ymin=(), ymax=5000, color="red")
plt.show()