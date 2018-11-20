import sys
from numpy import sin, linspace
from matplotlib import pyplot as plt

def f(x):
    return sin(x)

x = linspace(0, 7, 71)
y = f(x)

delta_x = x[1] - x[0]

plt.grid()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Funkcija $sin(x)$")
plt.plot(x, y, color = "#FF0000")
##plt.legend(["$sin(x)$"])
##plt.show()

y_first_derivative = (f(x+delta_x) - f(x)) / delta_x
plt.plot(x, y_first_derivative, color = "#00FF00")
##plt.legend(["$sin(x)$", "$sin\"(x)$"])
##plt.show()

N = len(x)
y_first_derivative_built_from_array = []
for i in range(N-1):
    temp = (y[i+1] - y[i]) / (delta_x)
    y_first_derivative_built_from_array.append(temp)
##    print(i, x[i], x[i+1], y[i], y[i+1], temp, y_first_derivative_built_from_array)


plt.plot(x[0:N-1], y_first_derivative_built_from_array, color = "#0000FF")
plt.legend(["$sin(x)$", "$sin\"(x)$", "$sin\"(x) - build from arrays$"])
plt.show()
    
