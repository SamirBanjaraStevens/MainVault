Suppose $S$ is a surface with the equation $F(x, y, z) = k$ that is, it is a level surface of a function $F$ of three variables 
and let $P(x_{0}, y_{0}, z_{0})$ be a point on $S$.

Let $C$ be any curve that lies on the surface $S$ and passes through the point $P$.

Recall that the curve $C$ is describe by a continious vector function $r(t) = \langle x(t), y(t), z(t)\rangle$ 
and let $t_{0}$ be the parameter value corresponding to $P$; that is $r(t_{0}) = \langle x_{0}, y_{0}, z_{0}\rangle$ 
since, $C$ liens on S, any point $(x(t), y(t), z(t))$ must satisfy the equation of $S$ that is,
$$F(x(t), y(t), z(t)) = k$$

If $x, y, z$ are differentiable functions of $t$ and $F$ is also differentiable, then we can use the Chain Rule to differentiate both sides of the Equations 16 as follows:
$$\tag{17}\cfrac{\partial F}{\partial x}\cfrac{dx}{dt}+\cfrac{\partial F}{\partial y}\cfrac{dy}{dt}+\cfrac{\partial F}{\partial z}\cfrac{dz}{dt}=0$$
But since, $\nabla F=\langle F_{x}, F_{y}, F_{z}\rangle$ and $r'(t) = \langle x'(t), y'(t), z'(t)\rangle$ 

We can re write *(17)* as a dot product, 
$$\nabla F \cdot r'(t)=0$$
In particular, when $t = t_{0}$ we have $r(t_{0}) = \langle x_{0}, y_{0}, z_{0}\rangle$ so, 
$$\tag{18}\nabla F(x_{0}, y_{0}, z_{0})\cdot r'(t_{0})=0$$

Equation *(18)* says that the gradient vector at $P$ , $\nabla F(x_{0},y_{0},z_{0})$ 
is perpendicular to the tangent vector $r'(t_{0})$ to any curve $C$ on $S$ that passes through $P$ 

If $\nabla F(x_{0},y_{0},z_{0}) \neq 0$
Therefore, define the **tangent plane to the level surface** $F(x, y, z)=k$ at $P(x_{0}, y_{0}, z_{0})$ as the ==plane that passes through $P$ 
	and has the normal vector $\nabla F(x_{0},y_{0},z_{0})$ 

Using standard equation of a plane, we can write the equation of this tangent plane as
$$\tag{19} F_{x}(x_{0},y_{0},z_{0})(x-x_{0})+F_{y}(x_{0},y_{0},z_{0})(y-y_{0})+F_{z}(x_{0},y_{0},z_{0})(z-z_{0})=0$$

The **Normal Line** to $S$ at $P$ is the line passign through $P$ and perdendicular to the tangent plane.

The direction of the normal line is given by the gradient vector, thus, itsymmetric equations are
$$\tag{20}
\cfrac{z-z_{0}}{F_{x}(x_{0},y_{0},z_{0})}
=
\cfrac{y-y_{0}}{F_{y}(x_{0},y_{0},z_{0})}
=
\cfrac{z-z_{0}}{F_{z}(x_{0},y_{0},z_{0})}
$$

In the special case in which the equation of a surface $S$ is of the form $z = f(x, y)$
	that is $S$ is the graph of a fucntion $f$ of two variables

We can rewrite equation *(20)* as $$F(x, y, z) = f(x, y)-z = 0$$

and regard $S$ as alevel surface (with $k=0$) of $F$ then
$$\begin{align}
F_{x}(x_{0},y_{0},z_{0}) &= f_{x}(x_{0}, y_{0})\\
F_{y}(x_{0},y_{0},z_{0})&= f_{y}(x_{0}, y_{0})\\
F_{z}(x_{0},y_{0},z_{0})&= -1\\
\end{align}$$

so equation *(19)* becomes 
$$f_{x}(x_{0}, y_{0})(x-x_{0})+ f_{y}(x_{0}, y_{0})(y-y_{0})-(z-z_{0})=0$$

Find the equations of the tangent plane and normal line at the point $(-2, 1, -3)$ to the ellipsoid, 
$$\cfrac{x^{2}}{4}+y^{2}+\cfrac{z^{2}}{9}=3$$

**Solution:**
***
The ellipsoid is the level surface (with $k=3$) of the function,
$$F(x, y, z) = \cfrac{x^{2}}{4}+y^{2}+\cfrac{z^{2}}{9}$$

Thefore we have 
$$F_{x}(x,y, z) = \cfrac{x}{2},\quad F_{y}(x, y, z) = 2y, \quad F_{z}(x, y, z)=\cfrac{2z}{9}$$
$$F_{x}(-2, 1, 3) = -1, \quad F_{y}(-2, 1, 3) = 2, \quad F_{z}(-2, 1, -3) = -\cfrac{2}{3}$$
Then, *equation (19)* give the equation of the tangent plane at $(-2, 1,-3)$ as 
$$-1(x+2)+2(y-1)-\cfrac{2}{3}(z+3)=0$$
which simplifis to $3x-6y+2z+18=0$