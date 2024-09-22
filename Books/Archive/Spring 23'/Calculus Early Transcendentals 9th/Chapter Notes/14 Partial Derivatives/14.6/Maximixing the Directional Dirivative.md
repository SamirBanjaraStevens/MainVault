Suppose we have a fucntion $f$ of two or three variables 
and consider all posible dirctional derivatives of $f$ at a given point.
These give the rates of change of $f$ in all possible directions. 
We can then ask the question: ==in which of these directions does $f$ change fastest and what is the maximum rate of change?== 
***
Suppose $f$ is a differentiable function of two or three variables. 
The maximum value of the directional derivative $D_{u}f(x)$ is $\|\nabla f(x)\|$
and it occurs when $u$ has the same direction as the gradient vector $\nabla f(x)$

#### Example 6
***
**(a).** if $f(x, y) = xe^{y}$ find the rate of change of $f$ at th epoint $P(2,0)$ in the direction from $P$ to $Q(\cfrac{1}{2}, 2)$ 

**(b).** In what direction does $f$ have a maximum rate of change? What is this maximum rate of change?

**Solution:**
***
Compute the gradient vector $\nabla f(x, y)$
$$\begin{align}
\nabla f(x, y) &= \langle f_{x}, f_{y}\rangle\\
&= \langle e^{ y }, xe^{y}\rangle\\
\nabla f(1, 2) &= \langle 1, 2\rangle
\end{align}$$

The unit vector in the direction of $\vec{PQ} = \left\langle -\cfrac{3}{2}, 2\right\rangle$ is $u = \left\langle -\cfrac{3}{5}, \cfrac{4}{5}\right\rangle$
So, the rate of change of $f$ in the direction from $P$ to $Q$ is 
$$\begin{align}
D_{u}f(2, 0) &= \nabla f(2, 0)\cdot u\\
&= \langle 1,2 \rangle\cdot \left\langle -\cfrac{3}{5}, \cfrac{4}{5}\right\rangle\\
&= 1\left(-\cfrac{3}{5}\right)+2\left(\cfrac{4}{5}\right)\\
&=1
\end{align}$$
(b). $f$ incrase fastest ==in the direction of the gradient vector== $\nabla f(2, 0) = \langle 1, 2\rangle$ 
The maximum rate of change is 
$$\|\nabla f(2, 0)\| = \|\langle 1, 2\rangle\| = \sqrt{ 5 }$$

#### Example 7
***

Suppose that the remperate at point $(x, y, z)$ in space is given by $T(x, y, z) = \cfrac{80}{(1+x^{2}+2y^{2}+3z^{2})}$ 
where, $T$ is measured in degree Celcius and $x, y, z$ in meters.

In which direction does the temperature increase fastest at the point $(1,1,-2)$

what is the maximum rate of increase?

**Solution:**
***
The gradint of $T$ is $$\nabla T = \cfrac{\partial f}{\partial x}i+\cfrac{\partial f}{\partial y}j+\cfrac{\partial f}{\partial z}k$$