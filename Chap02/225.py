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
# 関数として定義
def drawing(): # Define as a function
    return freqs.sample(n = 1, weights = "probs").index[0]

# LiDARのセンサ値のヒストグラムの作成
samples = [drawing() for i in range(len(data))]
# samples = [drawing() for i in range(100)]
simulated = pd.DataFrame(samples, columns = ["lidar"])
p = simulated["lidar"]
p.hist(bins = max(p) - min(p), color = "orange", align = 'left')
plt.show()