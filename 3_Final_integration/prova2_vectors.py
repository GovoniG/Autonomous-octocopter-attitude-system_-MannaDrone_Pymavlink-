import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ax = plt.figure().add_subplot(projection='3d')
u = ax.quiver(0, 0, 0, 1, 0, 0, color="r")
v = ax.quiver(0, 0, 0, 0, 1, 0, color="g")
w = ax.quiver(0, 0, 0, 0, 0, 1, color="b")

# set empty line plots with colors associate to the
# quivers. Doing so we can show a legend.
ax.plot([], [], [], color="r", label="u")
ax.plot([], [], [], color="g", label="v")
ax.plot([], [], [], color="b", label="w")
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()
plt.show()