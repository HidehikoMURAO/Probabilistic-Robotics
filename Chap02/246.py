#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# データの読み込み
data = pd.read_csv("sensor_data_600.txt", delimiter = " ",
                  header = None, names = ("data", "time", "ir", "lidar"))

data["hour"] = [e//10000 for e in data.time]  #hourly_mean,Note that "//" is not "/"#
d = data.groupby("hour")

each_hour = {i : d.lidar.get_group(i).value_counts().sort_index() for i in range(24)} # data frames every hour
freqs = pd.concat(each_hour, axis = 1) # Connect with concat
freqs = freqs.fillna(0) # Replace missing values(NaN) with 0
probs = freqs/len(data) # Convert frequency to probability

# グラフの描画
sns.jointplot(data["hour"], data["lidar"], data, kind = "kde")

plt.show()