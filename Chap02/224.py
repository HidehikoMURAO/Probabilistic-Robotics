#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import pandas as pd
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv("sensor_data_200.txt", delimiter = " ", 
        header = None, names = ("date", "time", "ir", "lidar"))

# 各センサ値の頻度を集計
freqs = pd.DataFrame(data["lidar"].value_counts())
# freqsに確率の列を追加
freqs["probs"] = freqs["lidar"]/len(data["lidar"])

# LiDARのセンサ値のヒストグラムの作成
freqs["probs"].sort_index().plot.bar()
plt.show()