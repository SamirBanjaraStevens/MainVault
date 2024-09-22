import numpy as np
import scipy.linalg as linalg
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


# 1. Simulate data from y = cos(x) for x in the interval [-π/2, π/2]. Use equally spaced x values.

# Define the interval and number of data points
x_start, x_end, num_points = -np.pi/2, np.pi/2, 10 # Number of data points

x = np.linspace(x_start, x_end, num_points)  # Generate equally spaced x values
y = np.cos(x)  # Compute corresponding y values using the cosine function

# 2. Set up the tri-diagonal coefficient matrix A for natural cubic splines.
# Determine the number of data points
n = len(x)
A = np.zeros((n, n))  # Initialize coefficient matrix A
A += np.diag([2] * n)  # Diagonal elements to 2
A += np.diag([1] * (n - 1), k=-1)  # Sub-diagonal elements to 1
A += np.diag([1] * (n - 1), k=1)  # Super-diagonal elements to 1

# 3. Set up the y vector and solve the system Ac = y to obtain the c's.
c = linalg.solve(A, y)  # Solve the system Ac = y to obtain the c's

# 4. Solve for the other coefficients: a's, b's, and d's.
a, b, d = y.copy(), np.zeros(n), np.zeros(n)
for j in range(n-1):
    h = x[j+1] - x[j]
    b[j] = (y[j+1] - y[j]) / h - (c[j+1] + 2*c[j]) * h / 3  # Calculate b coefficients
    d[j] = (c[j+1] - c[j]) / (3 * h)  # Calculate d coefficients

# For educational display, print the coefficients.
for j in range(n):
    print(f"Spline {j+1}: a = {a[j]}, b = {b[j]}, c = {c[j]}, d = {d[j]}")

# 5. Compare the fitted coefficients with values from the scipy built-in cubic splines function.
spline = CubicSpline(x, y)  # Built-in cubic spline function
coefficients = spline.c[:, :3]  # Extract coefficients for the first three splines

# For educational comparison, print the coefficients from the built-in function.
for j, coeff in enumerate(coefficients.T):
    print(f"Spline {j+1}: a = {coeff[3]}, b = {coeff[2]}, c = {coeff[1]}, d = {coeff[0]}")  # Notice the reversed order

# 6. Plot the cos(x) curve and interpolate the values using a finer grid and your own spline code.
x_finer = np.linspace(x_start, x_end, 100)  # Finer grid of x values
y_cosine, y_spline = np.cos(x_finer), spline(x_finer)  # Evaluate the cosine and spline functions

plt.plot(x_finer, y_cosine, label='cos(x)')  # Plot original cosine curve
plt.plot(x_finer, y_spline, label='Spline')  # Plot spline curve
plt.scatter(x, y, color='red', label='Data Points')  # Highlight original data points
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting Natural Cubic Splines')
plt.grid(True)
plt.show()
