#----1---+----2----+----3----+----4----+----5----+----6----+----7----+----8----+
import math
import matplotlib.pyplot as plt

# ガウス分布
def p(z, mu = 209.7, dev = 23.4):
    return math.exp(-(z -mu)**2 / (2*dev))/math.sqrt(2*math.pi*dev)

# グラフの描画
zs = range(190, 230)
ys = [p(z) for z in zs]

plt.plot(zs, ys)
plt.show()