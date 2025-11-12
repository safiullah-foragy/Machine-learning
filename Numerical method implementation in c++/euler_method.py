import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

def euler_method(x0, y0, x_end, h):
    n = int((x_end - x0) / h)
    x_points = [x0]
    y_points = [y0]

    x = x0
    y = y0

    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h
        x_points.append(x)
        y_points.append(y)

    return np.array(x_points), np.array(y_points)


initial_values = [
    (0, 1, 0.4, 0.1),
    (0, 2, 0.4, 0.1),
    (0.1, 0.5, 0.5, 0.05)
]

plt.figure(figsize=(8,5))

for x0, y0, x_end, h in initial_values:
    x_points, y_points = euler_method(x0, y0, x_end, h)
    plt.plot(x_points, y_points, 'o-', label=f"x0={x0}, y0={y0}, h={h}")

plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's Method for Multiple Initial Values")
plt.legend()
plt.grid(True)
plt.show()
