import pkin
from matplotlib import pyplot as plt

x1 = []
x2 = []
y1 = []
y2 = []
for n in range(1,92):
  try:
    z = pkin.pkin('Cl', n, 10, 10.5)['RBS_E']

    if type(z) == tuple:
      x1.append(n)
      x2.append(n)
      y1.append(z[0])
      y2.append(z[1])
    else:
      x1.append(n)
      y1.append(z)
  except:
    pass

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.show()