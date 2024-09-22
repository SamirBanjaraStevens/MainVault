For a function of three cariables we can define directional derivaitives in a simmilar manner.

Again $D_{u}f(x, y, z)$ can be interted as the rate of change of the function in the direction of a unit vector $u$

$$
D_{u} f(x_{0}, y_{0}, z_{0}) = \lim_{ h \to 0 } \cfrac{f(x_{0}+ha, y_{0}+hb, z_{0}+hc)-f(x_{0}, y_{0}, z_{0})}{h}
$$

in vector notaion
$$D_{u}f(x_{0}) = \lim_{ h \to 0 } \cfrac{f(x_{0}+hu)-f(x_{0})}{h}$$
where, $x_{0}=\langle x_{0}, y_{0}\rangle$ if $n=2$ and $x_{0}=\langle x_{0}, y_{0}, z_{0}\rangle$ if $n=3$

This is because, the vector equation of the line through $x_{0}$ in the direction of the vector $u$ is given by $x = x_{0}+tu$ 
and so, $f(x_{0}+hu)$ represents the value of $f$ at a point on the line.

If $f(x, y, z)$ is differentiable and $u = \langle a, b, c\rangle$
then, we show that 
$$D_{u}d(x, y, z) = f_{x}(x, y, z)a+ f_{y}(x, y, z)b+f_{z}(x, y, z)c$$

For a function of $f$ with three variables
	the gradient vector 
		denoted $\nabla f$
			is 
				$$\nabla f(x, y, z) = \langle f_{x}(x, y, z), f_{y}(x, y, z), f_{z}(x, y, z) \rangle$$
**or for short:**
$$\nabla f= \langle f_{x}, f_{y}, f_{z}\rangle = \cfrac{\partial f}{\partial x}i+ \cfrac{\partial f}{\partial y}j+ \cfrac{\partial f}{\partial z}k$$
and the directional derivative can be written
$$D_{u}f(x, y, z) = \nabla f(x, y, z)\cdot u$$
#### Example
***
if $f(x, y, z) = x\sin(yz)$
(a). Find the gradient of $f$
(b). Find the direction derivative of $f$ at $(1, 3, 0)$ in the direction of $v = i+2j-k$

**Solution:**
***
(a). $\nabla f(x, y, z) = \cfrac{\partial f}{\partial x}i+\cfrac{\partial f}{\partial y}j+\cfrac{\partial f}{\partial z}k$
$$
\begin{align}
\cfrac{\partial f}{\partial x} &= \sin(yz)\\
\cfrac{\partial f}{\partial x} &= x\cos(yz)z\\
\cfrac{\partial f}{\partial x} &= x \cos(yz)y
\end{align}
$$
so, $$\begin{align}
\nabla f(x, y, z) &= (\sin(yz))i+(x\cos(yz)z)j+(x \cos(yz)y)k\\
&=\langle (\sin(yz)), (x\cos(yz)z), (x \cos(yz)y)\rangle
\end{align} $$
(b). at $(1, 3, 0)$ we have $\nabla f(1, 3, 0) = \langle 0, 0, 3\rangle$

The unit vector in the direction of $v = i+2j-k$ 
is $$u=\cfrac{1}{\sqrt{ 6 }}i+\cfrac{2}{\sqrt{ 6 }}j-\cfrac{1}{\sqrt{ 6 }}k$$

Therefore 
$$
\begin{align}
D_{u}f(1, 3,0) &= \nabla f(1, 3, 0)\cdot u\\
&=3k \cdot \left(\cfrac{1}{\sqrt{ 6 }}i+\cfrac{2}{\sqrt{ 6 }}j-\cfrac{1}{\sqrt{ 6 }}k\right)\\
&= 3\left(-\cfrac{1}{\sqrt{ 6 }}\right)\\
&= -\sqrt{ \cfrac{3}{2} }
\end{align}
$$


