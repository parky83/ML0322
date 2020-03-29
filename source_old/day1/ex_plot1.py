import numpy as np
import matplotlib.pyplot as plt

# 
np.random.seed(1)
x=np.arange(100)
print(x)
y=np.random.rand(100)
print(y)
# 
plt.plot(x,y, label="test")
plt.legend(loc="upper left")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid()
plt.show()