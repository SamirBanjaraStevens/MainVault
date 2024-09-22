## 1. Find an equation of the tangent plane to the surface $x^{2}+y^{2}-z^{2}=-3$ at the point $(2, 3, 4)$

Equation of tangent plane $z=f(x_{0}, y_{0})+f_{x}(x-x_{0})+f_{y}(y-y_{0})$ 

$f(x_{0}, y_{0}, z_{0}) = f(2, 3, 4) = 2^{2}+3^{2}-4^{2}= -3$
$f_{x}=2x+y^{2}-z^{2}$ 
$f_{x}(2, 3, 4)=2*2+3^{2}-4^{2}=-3$
$f_{y} = x^{2}+2y-z^{2}$
$f_{y}(2, 3, 4) = 2^{2}+2*3-4^{2}=-6$
$f_{z}=x^{2}+y^{2}-2z$
$f_{z}(x_{0}, y_{0}, z_{0}) = 2^{2}+3^{2}-2*4 =5$
Thus, equation of tangent plane is $0 = (-3)(x-2)+(-6)(y-3)+5(z-4)$

or,
$F(2, 3, 4) = 0 + (-3, -6, 5)*\begin{bmatrix}x-1\\y-1 \\ z-1\end{bmatrix}$
$-4=-3x-6y+5z$


## 2. Find the mazimum of the function $f(x, y, z) = xyz$ subject to the restriction $x^{2}+3y^{2}+5x^{2}=8$. Or Show that the maximum does not exist. 

Larange multipliers tell us that $\nabla f = \lambda \nabla g$ or $\langle yz, xz, zy\rangle = \langle 2\lambda x, 6\lambda y, 10\lambda z\rangle$ 
and so we get the system
$$
\begin{align}
yz&=2\lambda x\\
xz &= 6\lambda y\\
xy &= 10\lambda z\\
x^{2}+3y^{2}+5z^{2}&=8
\end{align}
$$
Note that if either $x$, $y$ or $z$ is zero, 
then $x = y =z =0$
which contradicts $x^{2}+3y^{2}+5z^{2}=8$
thus $x\ne_{0}, y \neq 0, z\neq 0$
then, 
$$
\begin{align}
\lambda =& \cfrac{yz}{2x}=\cfrac{xz}{6y}=\cfrac{xy}{10z}\\
x&= \cfrac{yz}{2\lambda}\\
y&=\cfrac{xz}{6\lambda}\\
z&=\cfrac{xy}{10\lambda}
\end{align}
$$

and $\lambda \neq 0$ from which we get 
$$

