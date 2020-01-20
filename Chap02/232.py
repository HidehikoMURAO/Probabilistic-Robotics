#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
# ガウス分布
import math
def p(z, mu = 209.7, dev = 23.4):
    return math.exp(-(z -mu)**2 / (2*dev))/math.sqrt(2*math.pi*dev)
def prob(z, width = 0.5): 
    return width*(p(z - width) + p(z + width))

# グラフの描画
zs = range(190, 230)
ys = [p(z) for z in zs]

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("sensor_data_200.txt", delimiter = " ",
                  header = None, names = ("data", "time", "ir", "lidar"))
freqs = pd.DataFrame(data["lidar"].value_counts())
freqs["probs"] = freqs["lidar"] / len(data["lidar"])

plt.bar(zs, ys, color = "red", alpha = 0.3) # Make graphs transparent with alpha
f = freqs["probs"].sort_index()
plt.bar(f.index, f.values, color = "blue", alpha = 0.3)
plt.show()