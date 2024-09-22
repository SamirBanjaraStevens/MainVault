import numpy as np

# Define the interval and number of data points
x_start = -np.pi/2
x_end = np.pi/2
n = 10  # Number of data points

# Generate equally spaced x values
x = np.linspace(x_start, x_end, n)

# Compute the corresponding y values using the cosine function
y = np.cos(x)

# Determine the number of data points
n = len(x)

# Create the coefficient matrix A
A = np.zeros((n, n))

# Set the diagonal elements to 2
np.fill_diagonal(A, 2)

# Set the sub-diagonal and super-diagonal elements to 1
np.fill_diagonal(A[1:], 1)
np.fill_diagonal(A[:, 1:], 1)

import scipy.linalg as linalg

# Create the y vector
y = y.reshape((-1, 1))

# Solve the system Ac = y to obtain the c's
c = linalg.solve(A, y)


# Create vectors for a, b, and d
a = y.flatten()
b = np.zeros(n)
d = np.zeros(n)

# Solve for b and d
for j in range(n-1):
    h = x[j+1] - x[j]
    b[j] = (y[j+1] - y[j]) / h - (c[j+1] + 2*c[j]) * h / 3
    d[j] = (c[j+1] - c[j]) / (3 * h)

# Print the coefficients
for j in range(n):
    print(f"Spline {j+1}: a = {a[j]}, b = {b[j]}, c = {c[j]}, d = {d[j]}")
    
from scipy.interpolate import CubicSpline

# Create a CubicSpline object using the simulated data
spline = CubicSpline(x, y)

# Extract the coefficients for the first three splines
coefficients = spline.c[:3]

# Print the coefficients
for j, coeff in enumerate(coefficients):
    print(f"Spline {j+1}: a = {coeff[0]}, b = {coeff[1]}, c = {coeff[2]}, d = {coeff[3]}")    

import matplotlib.pyplot as plt

# Generate a finer grid of x values
x_finer = np.linspace(x_start, x_end, 100)

# Evaluate the cosine function for the finer grid
y_cosine = np.cos(x_finer)

# Evaluate the spline function for the finer grid
y_spline = spline(x_finer)

# Plot the cosine curve and the spline curve
plt.plot(x_finer, y_cosine, label='cos(x)')
plt.plot(x_finer, y_spline, label='Spline')
plt.scatter(x, y, color='red', label='Data Points')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Fitting Natural Cubic Splines')
plt.grid(True)
plt.show()