import pkin
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for m in range(1,5):
  for n in range(10,15):
    try:
      value = pkin.pkin(m, n, 10, 10.5)['RBS_E']
      if type(value) == tuple:
        value = value[0]
      ax.scatter(float(m), float(n), value, c='r', marker='o')
    except:
      pass

#Axes3D.plot_wireframe(x2, z2, y2)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()