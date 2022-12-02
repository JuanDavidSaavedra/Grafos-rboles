import matplotlib.pyplot as plt
import numpy as np

cx = np.arange(1,2,3)
cy = np.arange(1,4,9)
cy1 = np.arange(3,2,8)
plt.figure(figsize = (10,12))
fig, ax = plt.subplots()
ax.bar(cx, cy, width=1, edgecolor="white", linewidth=0.7)

ax.set(cxlim=(0, 9,3), cxticks=np.arange(1, 2,3),
       cylim=(0, 9,4), cyticks=np.arange(1, 4,9))
plt.xlabel("numeros")
plt.ylabel("diagonal")
plt.yticks([1,4,8])
plt.legend(loc = "lower right")
plt.title("Gráfica matriz")
plt.savefig("matriz.png")
plt.show()
