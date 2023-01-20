import matplotlib.pyplot as plot
import random
x = [random.random() for i in range(100)]
y = [random.random() for i in range(100)]
plot.scatter(x,y)
plot.show()
