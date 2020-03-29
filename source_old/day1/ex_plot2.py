import numpy as np
import matplotlib.pyplot as plt

#


def f(x):
    return (x-2)*x*(x+2)


print(f(1))

print(f(np.array([1, 2, 3])))

#

x = np.arange(-3, 3.5, 0.5)
print(x)

#
x = np.linspace(-3, 3, 10)
print(np.round(x, 2))

plt.plot(x, f(x), color="red", label="$w=2, x=10$")
# plt.show()


def f2(x, w):
    return (x-w)*x*(x+2)


x = np.linspace(-3, 3, 100)

plt.plot(x, f2(x, 2), color="black", label="$w=2, x=100$")
plt.plot(x, f2(x, 1), color="cornflowerblue", label="$w=1, x=100$")
plt.legend(loc="upper left")
plt.ylim(-15, 15)
plt.title("$f(x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.grid(True)
plt.show()
