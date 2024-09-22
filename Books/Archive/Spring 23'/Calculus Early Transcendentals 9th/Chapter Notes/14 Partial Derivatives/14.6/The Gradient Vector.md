The directional derivative of a differentiable function can be written as the dot product of two vectors:
$$
\begin{align}
D_{u}f &= f_{x}(x, y)a+f_{y}(x,y)b\\
&=\langle f_{x(x,y)}, f_{y}(x, y) \rangle\cdot\langle  a, b\rangle\\
&= \langle f_{x(x,y)}, f_{y}(x, y) \rangle \cdot u
\end{align}
$$

The first vector in this dot product is known as the gradiebt of $f$
	$\nabla f$

Then the Gradiuent of $f$ is the vector $\nabla f$ defiend by
$$\begin{align}
\nabla f &= \langle f_{x(x,y)}, f_{y}(x, y)\rangle\\
&=\cfrac{\partial f}{\partial x}i + \cfrac{\partial f}{\partial y}j
\end{align}$$
#### Example 3
***
if $f(x, y) = \sin(x)+e^{xy}$ then,
$$\begin{align}
\nabla f(x,y) &= \langle f_{x}, f_{y}\rangle\\
&=\langle \cos(x) + ye^{xy}, xe^{xy} \rangle\\
\nabla f(0, 1) &= \langle 2, 0 \rangle
\end{align}$$

with this notion we can write the directional derivative of a differentiable function as 
$$D_{u}f(x,y) = \nabla f(x,y)\cdot u$$
This expresses the directional derivative in the direction of a unit vector $u$ as the scalar projection of the gradient vector onto $u$


#### Example 4
***
Find the directional derivative of the function $f(x,y) = x^2y^3-4y$
at the point $(2, -1)$ in the direction of the vector $v = 2i+ 5j$ 

**Solution:** 
***
Compute the gradient vector at $(2, -1)$
$$\nabla f(x,y) = 2xy^{3}i+(3x^2y^{2}-4)j$$
$$\nabla f(2,-1)= -4i+8j $$
Note that $v$ is not a unit vector. 
but since $\|v\|=\sqrt{ 29 }$ 
the unit vector in the direction of $v$ is 
$$u = \cfrac{v}{\|v\|}= \cfrac{2}{\sqrt{ 29 }}i+\cfrac{5}{\sqrt{ 29 }}j$$
Therefore
$$
\begin{align}
D_{u}f(2, -1) &= \nabla f(2, -1)\cdot u\\
&=(-4i+8j)\cdot \left(\cfrac{v}{\|v\|}= \cfrac{2}{\sqrt{ 29 }}i+\cfrac{5}{\sqrt{ 29 }}j\right)\\
&= \cfrac{-4\cdot 2 +8\cdot 5}{\sqrt{ 29 }}\\
&= \cfrac{32}{\sqrt{ 29 }}
\end{align}
$$
