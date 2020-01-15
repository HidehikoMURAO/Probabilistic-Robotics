#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
# データの読み込み
import pandas as pd
data = pd.read_csv("sensor_data_200.txt", delimiter = " ", 
        header = None, names = ("date", "time", "ir", "lidar"))

# LiDARのセンサ値のヒストグラムの作成
import matplotlib.pyplot as plt
data["lidar"].hist(bins = max(data["lidar"]) - min(data["lidar"]), align = 'left')
plt.show()