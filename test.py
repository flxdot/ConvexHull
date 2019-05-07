import numpy as np
import matplotlib.pyplot as plt

import chull

# generate random data
cnt = 50
x = np.random.random(cnt)
y = np.random.random(cnt)

# find the
x_hull, y_hull = chull.findHull(x,y)
# close the loop
x_hull = np.append(x_hull, x_hull[0])
y_hull = np.append(y_hull, y_hull[0])

# plot the data
fig = plt.figure()
plt.scatter(x,y)
plt.plot(x_hull, y_hull, color='r')
plt.show()
