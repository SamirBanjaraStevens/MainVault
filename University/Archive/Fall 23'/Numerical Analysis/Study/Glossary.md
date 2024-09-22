### 1. Interpolation:

  

**Definition:** Estimation of unknown values within the range of a discrete set of known values.

  

**Methods:**

- **Lagrange Polynomial:** A polynomial that passes through a given set of points in the plane. Given two points $(x_{0}, y_{0})$ and $(x_{1}, y_{1})$. The interpolating polynomial of the least degree is a linear function of the form:

$$P(x) = y_{0} + \cfrac{y_{1}-y_{0}}{x_{1}-x_{0}}(x-x_{0})$$
For a set of $n+1$ points, there exists exactly one polynomial of degree at most $n$ that passes through all the data points. The interpolation polynomial can be written in the Lagrange form:

  - **Formula:** 

  $$

  P(x) = \sum_{i=0}^{n} y_i L_i(x)

  $$

  where each $l_{i}(x)$ is the Lagrange basis polynomial:

  $$

  L_i(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}

  $$
***
The Lagrange form of the interpolation polynomial shows the linear character of polynomial interpolation and the uniqueness of the interpolation polynomial. Moreover, the Lagrange interpolation is susceptible to the Runge phenomenon, a problem of oscillation at the edges of an interval of polynomial interpolation. This problem can be resolved by using the Chebyshev nodes as interpolation points.
***
  




- **Neville's Method:** A recursive algorithm for polynomial interpolation.
	- Neville's algorithm is a recursive method used to evaluate the interpolating polynomial of a given set of data points without explicitly determining the polynomial itself. The algorithm is based on the idea of divided differences and provides a way to estimate the polynomial's value at a given point.
	- The formula for neville's method is given by:
$$P_{ij}(x)=\cfrac{(x-x_{i})P_{i+1, j+1}(x)-(x-x_{i+j})P_{ij-1}(x)}{}$$
		where $P_{ij}(x)$ represents the polynomial that interpolates the points
		$$(x_{i}, y_{i}), (x_{i+1}, y_{i+1}), \cdots, (x_{i+j}, y_{i+j})$$
- The value of the polynomial at a specfiv point $x$ can be found by recursively applying the formula until reaching $P_{0, n}(x)$ which gives the desired value. 

  The recursive nature of Neville's algorithm comes from the formula itself. To compute $P_{ij}(x)$, you need values from $P_{i+1,j−1}​(x)$ and $P_{ij−1}​(x)$. This means to get the value of the polynomial at a certain level, you need values from the previous levels. This process continues until you reach the base cases, which are the given data points themselves.

For example, to compute $P_{0,2}​(x)$ for three data points, you'd need $P1,1(x)P1,1​(x)$ and $P_{0,1}(x)$. To compute those, you'd need $P_{2,0}(x) P_{1,0}(x)$, and $P_{0,0}​(x)$, which are just the y-values of the data points.

The recursive structure can be visualized as a triangular table or matrix, where the base row contains the y-values of the data points, and each subsequent row is computed based on the values in the row below it. The topmost value in this triangle gives the interpolated value at the desired point xx.

- **Newton's Divided-Difference Formula:** A formula to represent data as coefficients of a polynomial.

  - **Formula:** 

  $$

  P(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \dots

  $$

  This is a method used to construct interpolating polynomials.
  Construct a polynomial that passes through a set of data points.
  This polynomial then can be used to estimate values between the known data points.
  The divided difference is calculated recursively. Th first divided difference is the difference between two function values. The second divided difference is the difference between the first two divided difference and so on
  This can be represented using a divided difference table. 
  It allows for the addition of new data points without the need to recalculate the entire polynomial. 
  Useful where new data is being continuously added.

- **Hermite Interpolation:** Interpolation that considers both function values and their derivatives.

  While Lagrange interpolation computers a polynomial of degree less than $n$ that matches the value of a given function at $n$ specfied points.
  Hermite interpolation goes a step further.

It computes a polynomial of degree less than $mn$ such that the polynomial and it $m-1$ first derivatives match the values at $n$ given points of both specified function and its $m-1$ derivatives.

Closely related to Newtons interpolation method since both derive from the calculations of divided differences.
However there are other ways to compute a Hermite interpolating formula.
One approach used linear algebra, treating the coefficients of the interpolating formula as unknowns. Then the linear equations are formed based on the constraints that the interpolating polynomial must satisfy. 

The essence of Hermite interpolation is to compute a polynomial of the lowest possible degree that matches an unknown function in both its observed and the observed value of the the first $m$ derivatives. 
This requires knowledge of $n(m+1)$ values, resulting in a polynomial with a degree less than $n(m+1)$.
In more general cases, $m$ doesn't need to be a fixed value, meaning some points might have more known derivatives than others. 
In such scenarios the resulting polynomial has a degree less than the total number of data points.
When using divided differences to calculate the Hermite polynomial of a function $f$, the initial step involves copying each point $m$ times. Given $n+1$ data points and their corresponding values and derivatives for a function $f$ that we wish to interpolate a new dataset is created. A divided differences table is then formed for these points. In some cases, the divided difference might be undefined, and in such instances, the divided difference is replaced by the derivative of the function at that point.

- **Osculating Polynomial:** A polynomial that satisfies both function and derivative values at interpolation points.

  

### 2. Approximation Theorems:

  

- **Weierstrass Approximation Theorem:** Every continuous function defined on a closed interval can be uniformly approximated by polynomial functions.

***
The theorem asserts that every continuous function defined on a closed interval $[a,b]$ can be uniformly approximated as closely as desired by a polynomial function. This means that for any continuous function $f(x)$ on the interval $[a,b]$ and for any given small positive number $\epsilon$, there exists a polynomial $P(x)$ such that the maximum difference between $f(x)$ and $P(x)$ on the interval is less than $\epsilon$.
***
Mergelyan's theorem, which generalizes the Weierstrass theorem to functions defined on certain subsets of the complex plane.
***
The theorem states that every continuous function defined on a closed interval can be uniformly approximated by polynomial functions. This means that no matter how complex or intricate a continuous function might be, there exists a polynomial that can come arbitrarily close to that function over the specified interval.
***

- **Piecewise Polynomial Approximation:** Approximating a function using different polynomials on different intervals.

**Definition**: In mathematics, a piecewise polynomial approximation refers to the representation of a function using different polynomial functions over distinct intervals of its domain. This approach is commonly employed because it allows for flexibility in approximating complex functions that may behave differently over various intervals.
**Formula**: A piecewise polynomial function can be represented as:
$$S(x) = 
\begin{cases} 
P_1(x) & \text{if } x \in [a_1, b_1] \\
P_2(x) & \text{if } x \in [a_2, b_2] \\
\vdots \\
P_n(x) & \text{if } x \in [a_n, b_n] 
\end{cases}
$$
Here, each $P_{i}(x)$ is a polynomial function defined over the interval $[a_{i}, b_{i}]$

**Essence**: The core idea behind piecewise polynomial approximation is to capture the local behavior of a function. Instead of using a single polynomial to approximate a function over its entire domain (which might lead to inaccuracies, especially for functions with varying behavior), different polynomials are used for different intervals. This ensures a closer and more accurate approximation. Moreover, piecewise polynomial approximations, especially splines, are often preferred over high-degree polynomial interpolations to avoid issues like Runge's phenomenon, where high-degree polynomial interpolations can exhibit oscillatory behavior.
### 3. Difference Operators and Formulas:

  

- **Forward Difference:** The difference between a function value and the next value.

In the realm of single-variable calculus, the forward difference is a mathematical expression that represents the difference between a function's value at a particular point and its value at the next point. It provides an approximation of the derivative of the function.

  - **Formula:** 

  $$

  f'(x) \approx \frac{f(x+h) - f(x)}{h}

  $$

  Here, $h$ is the difference between two consecutive points in the domain of the function. When $h$ is omitted, it is typically taken to be $1$.
  
  - **Essence**: The forward difference serves as a measure of the average rate of change of the function over a specified interval, in this case, an interval of length $h$. When taken to the limit as $h$ approaches $0$, the forward difference provides an approximation to the derivative of the function, representing the instantaneous rate of change. In numerical differentiation, forward differences are widely used to approximate derivatives, especially when the function's analytical derivative is difficult to compute or not available.

- **Backward Difference:** The difference between a function value and the previous value.

In numerical analysis, the backward difference is a finite difference that represents the difference between a function's value at a particular point and its value at the previous point. It serves as an approximation to the derivative of the function, especially when considering discrete data points.

  - **Formula:** 

  $$

  f'(x) \approx \frac{f(x) - f(x-h)}{h}

  $$

  - Here, $h$ is the difference between two consecutive points in the domain of the function. When $h$ is omitted, it is typically taken to be $1$.
    
- **Essence**: The backward difference provides a measure of the average rate of change of the function over a specified interval, in this case, an interval of length $h$. In numerical differentiation, backward differences are particularly useful when data is available only up to the current point and not beyond. It offers a way to approximate the derivative at the end of a set of data points.

- **Forward-Difference Operator:** An operator that computes the forward difference.

  

- **Backward-Difference Operator:** An operator that computes the backward difference.

  

- **Divided Differences:** Differences computed using function values at distinct points.

  

  - **Properties:** Symmetry, Linearity, Multiplication, Relation to divided differences of derivatives, Newton's interpolatory polynomial, Relation to higher order derivatives.

  

- **Error Formulas:** Formulas that provide bounds on the error of numerical methods.

  

### 4. Spline Interpolation:

  

- **Natural Cubic Spline:** A piecewise cubic polynomial that is twice differentiable.

  n the realm of numerical analysis, a natural cubic spline is a type of spline interpolation where the interpolant is a piecewise polynomial, specifically a cubic polynomial. The term "spline" originally referred to elastic rulers that were bent to pass through a number of predefined points, or knots. These were used for technical drawings in fields like shipbuilding. In mathematical terms, given a sequence of knots, there will be a cubic polynomial between each successive pair of knots connecting them. The natural cubic spline is a special case of the cubic spline that ensures certain boundary conditions.

For a set of knots $(x_{0}, y_{0})$ through $(x_{n}, y_{n})$, there will be a cubic polynomial $q_{i}=y$ between each sussesive pair of knots $(x_{i-1}, y_{i-1})$ and $(x_{i}, y_{i})$. The natoral cubic spline has a additional condition:
$$q_{1}^{''}(x_{0})=q_{n}^{''}(x_{n})=0$$
	This condition ensures that the second derivatives of the spline is zero at the end points, making it 'Natural'

**Essence**: The natural cubic spline is designed to provide a smooth curve that passes through a given set of data points. By ensuring that the second derivative is zero at the endpoints, the natural cubic spline avoids unnatural bends at the boundaries. This makes it particularly useful for smoothly interpolating data without introducing artificial oscillations or bends, especially at the data boundaries. The cubic nature of the spline ensures that it is smooth and differentiable, making it a popular choice for various applications in science, engineering, and computer graphics.

- **Clamped Boundary Condition:** A condition where the spline's first derivative is specified at the endpoints.
**Definition**: In spline interpolation, the clamped boundary condition refers to a condition where the first derivative of the spline is specified at the endpoints. This means that the slope of the spline is predetermined at the starting and ending points.
  
**Essence**: The clamped boundary condition ensures that the spline not only passes through the given data points but also has a specified slope at the endpoints. This can be particularly useful when the behavior of the function near the boundaries is known or when a specific shape or trend of the spline is desired at the endpoints.
- **Natural Boundary Condition:** A condition where the spline's second derivative is zero at the endpoints.
**Definition**: The natural boundary condition in spline interpolation refers to a condition where the second derivative of the spline is set to zero at the endpoints. This means that the curvature of the spline is flat at the starting and ending points.

**Formula** for the spline function $s(x)$, the natural boundry condition can be represented as $s''(x_{0})=0$ and $s''(x_{n})=0$ here $x_{0}$ and $x_{n}$ are end points of the interval

**Essence**: The natural boundary condition ensures a "smooth" or "flat" curvature at the endpoints of the spline. This results in a spline that does not exhibit any abrupt changes or bends at its boundaries, making it appear more "natural", especially when there's no prior knowledge about the behavior of the function near the boundaries.

- **Clamped Cubic Spline:** A cubic spline with clamped boundary conditions.

  

- **Bezier Curve:** A parametric curve used in computer graphics.

  

### 5. Numerical Methods for Root Finding:

  

- **Bisection Method:** A method that divides the interval into two subintervals and selects the subinterval in which the function changes sign.

  - **Description:** Choose \(a\) and \(b\) such that \(f(a)\) and \(f(b)\) have opposite signs. The root is approximated in the interval \([a,b]\). The midpoint \(c = \frac{a+b}{2}\) is computed and the interval in which the root lies is determined to be either \([a,c]\) or \([c,b]\) based on the sign of \(f(c)\).

  

- **Secant Method:** A method that uses linear interpolation to find the root.

  - **Definition:** The Secant Method is a root-finding algorithm that uses a succession of roots of secant lines to better approximate a root of a function.

  - **Formula:** 

  $$

  x_{n+1} = x_n - \frac{f(x_n)}{\frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}}

  $$

  

- **Steffensen's Method:** An acceleration technique for the fixed-point iteration.

  

- **Fixed-Point Iteration:** A method where a function is iteratively applied to produce a sequence of approximations.

  

- **Method of False Position:** A method that combines the bisection method and the secant method.

  

- **Miiller's Method:** A method that uses three points to find the root.

  

- **Newton's Method:** A method that uses the derivative to find the root.

  

- **Aitken's A2 Method:** An acceleration technique for convergence.

  

- **Horner's Method:** A method to evaluate polynomials efficiently.

  

### 6. Calculus and Analysis:

  

- **Limits, Continuity, Differentiability:** Fundamental concepts in calculus.

  

- **Rolle's Theorem, Intermediate Value Theorem, Weighted Mean Value Theorem, Generalized Rolle's Theorem:** Theorems that provide conditions under which certain properties hold for functions.

  

- **Taylor's Theorem:** A theorem that gives an approximation of a function using a polynomial.

  

- **Riemann Integral:** A way to define the integral of a function.

  

### 7. Numerical Errors and Stability:

  

- **Finite digit arithmetic, round-off errors:** Errors that arise due to the finite representation of numbers in computers.

  

- **Stability:** The property of a numerical method to produce accurate results despite small errors.

  

- **Finite digit representation:** The representation of numbers with a finite number of digits.

  

### 8. Miscellaneous:

  

- **Algorithms:** Step-by-step procedures to solve problems.

  

- **Numerical software:** Software tools used for numerical computations.

  

### 9. Solving Ordinary Differential Equations (ODEs):

  

- **Euler's Method:**

  - **Formula:** 

  $$

  y_{n+1} = y_n + h f(x_n, y_n)

  $$

  - **Description:** A first-order numerical procedure for solving ODEs with a given initial value. It's a simple method that uses the idea of local linearity or linear approximation.

  - **Parameters:** \(h\) is the step size.

  

- **Runge-Kutta Methods:**

  - **Description:** A set of iterative methods used to solve ODEs and partial differential equations.

  - **4th order Runge-Kutta method:**

    - **Formula:** 

    $$

    y_{n+1} = y_n + \frac{1}{6} (k_1 + 2k_2 + 2k_3 + k_4)

    $$

    - **Intermediate Values:** \(k_1, k_2, k_3,\) and \(k_4\) are computed at each step to refine the solution's accuracy.

  

### 10. Integration:

  

- **Trapezoidal Rule:**

  - **Formula:** 

  $$

  \int_{a}^{b} f(x) dx \approx h \left[ \frac{f(a) + 2f(a+h) + 2f(a+2h) + \dots + f(b)}{2} \right]

  $$

  - **Description:** A method for approximating the definite integral using linear interpolation.

  - **Parameters:** \(h\) is the width of the subintervals.

  

- **Simpson's 1/3 Rule:**

  - **Formula:** 

  $$

  \int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[ f(a) + 4f(a+h) + 2f(a+2h) + 4f(a+3h) + \dots + f(b) \right]

  $$

  - **Description:** A method for approximating the definite integral using quadratic interpolation.

  

- **Simpson's 3/8 Rule:**

  - **Formula:** 

  $$

  \int_{a}^{b} f(x) dx \approx \frac{3h}{8} \left[ f(a) + 3f(a+h) + 3f(a+2h) + f(b) \right]

  $$

  - **Description:** An extension of Simpson's 1/3 rule that uses cubic interpolation instead of quadratic.