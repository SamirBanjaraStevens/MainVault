## Question
***
Let $f(x, y, z) = xyz^2-x^2y^3$ subject to the constraint $g(x,y, z) = x^2+y^2=9$.
What is the absolute maximum and minimum of $f$ subject to these constraints?

**Solution :** 
Use Lagrange multipliers method to solve 

This method is used to find the local maxima and minima of a function subject to equality constraints.

The Lagrange function is given by: 
$$L(x, y, z, \lambda) = f(x, y, z)-\lambda \cdot (g(x, y, z)-c)$$
where $f(x, y, z)$ is the function to be optimized, 
	$g(x, y,z)$ is the constraint function
		& $\lambda$ is the Lagrange multiplier

*Given :*
$$f(x, y, z) = xyz^2-x^2y^3$$
$$g(x,y, z) = x^2+y^2-9$$
Thus the Lagrange function is 
$$L(x,y, z, \lambda) = xyz^2-x^2y^3-\lambda(x^2+y^2-9)$$

We can find the critical points by taking the partial derivatives of $L$ with respect to $x, y, z, \text{ and } \lambda$ 
	and setting them to zero


$$\cfrac{\partial L}{\partial x}; \quad \cfrac{\partial L}{\partial y}; \quad \cfrac{\partial L}{\partial z}; \quad \cfrac{\partial L}{\partial \lambda}$$
$$
\begin{align}
\cfrac{\partial L}{\partial x} &= yz^2-2xy^3-2\lambda x=0\\
\cfrac{\partial L}{\partial y} &= xz^2-x^23y^2-2\lambda y
=0\\
\cfrac{\partial L}{\partial z} &= 2xyz=0
=0\\
\cfrac{\partial L}{\partial \lambda} &= x^2+y^2-9 =0
\end{align}
$$
we then solve these equations simultaneously to find the critical points 
$(x, y, , \lambda)$ 

To find the absolute maximum 
	and minimum of $f$ 
		subject to the constraints
		we evaluate $f$ at all critical points 
			and at the boundary of the region defined by the constraints

However, this set of equations is quite complex and may not have straightforward analytical 
after obtaining potential points $(x, y, z)$ we compare the values of $f(x, y, z)$ to determine which points provide an absolute maximum and minimum.

## Question 23
Use Green's theorem to evaluate $\int _{C} F \cdot  \, dr$ 
	where$F(x, y) = \left< x^{3}y+y^{2}, x^{2}-xy^{2} \right>$
		and $C$ is a triangle traversed counter clockwise with vertices $(-2, 0), (0, 4), (2, 0)$ 

**Solution :**

***

In spherical coordinates, $x = \rho\sin\phi\cos\theta$, $y = \rho\sin\phi\sin\theta$, and $z = \rho\cos\phi$ where $\rho$ is the radial distance from the origin, $\phi$ is the angle measured from the positive z-axis (0 ≤ $\phi$ ≤ $\pi$), and $\theta$ is the angle measured from the positive x-axis in the xy-plane (0 ≤ $\theta$ < 2$\pi$).
