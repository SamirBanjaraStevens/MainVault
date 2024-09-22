
## Tangent Planes and Linear Approximations

In single-variable calcus, we learned that the graph of a function $f(x)$ can be approzimated near a point $x_{0}$ by its tangent line.
$$y=f(x_{0})+f'(x_{0})(x-x_{0})$$
For this reason, the fucntion $L_{f}(x)=f(x_{0})+f'(x_{0})(x-x_{0})$ is also the linearization, of linear approzimation, of $f(x)$ at $x_{0}$

Now suppose that we have a function of two variables, $f: D \subseteq \mathbb{R}^{2}\rightarrow \mathbb{R}$  and a point $(x_{0}, y_{0}) \in D$ 
Suppose the first partial derivaes of $f, f_{x}, f_{y}$ exists at $(x_{0}, y_{0})$ 
Becasue the graph of this function is a surface, 
	it follows that a linear function that approzimatesn $f$ near $(x_{0}, y_{0})$ would have a graph that is a plane.

Just as the tangent line of $f'(x)$ passes through point $(x_{0}, f(x_{0}))$, and has a slope that is equal to $f'(x_{0})$,
	the instantaneous rate of change of $f(x)$ with respect to $x$ at $x_{0}$ 
		, a plane that best approzimates $f(x, y)$ at $(x_{0}, y_{0})$ must pass through point $(x_{0}, y_{0}, f(x_{0},y_{0}))$ and the slope of the plane in the $x$- and $y$-directions, respectivelt shoudl equal to the values of $f_{x}(x_{0},y_{0})$  and $f_{y}(x_{0}, y_{0})$ 

Since, a general linear function of two variables can be described by the formula
$$L_{f}(x, y) = A(x - x_{0})+B(y-y_{0})+C$$
so that $L_{f}(x_{0}, y_{0})=C$, and a simple differentation yields
$$\cfrac{\partial L_{f}}{\partial x}=A, \quad \cfrac{\partial L_{f}}{\partial y}=B$$
We conclude that the linear function that best approzimates $f(x, y)$ near $(x_{0, Y_{0}})$ Is the lienar approximation
$$L_{f}(x, y) = f(x_{0}, y_{0}) + \cfrac{\partial f}{\partial x}(x_{0}, y_{0})(x-x_{0})+\cfrac{\partial f}{\partial y}(x_{0}, y_{0})(y-y_{0})$$
furthermore, the graph of this function is called the tangent plane of $f(x, y)$ at $x_{0}, y_{0}$
Its equation is $$z-z_{0} = \cfrac{\partial f}{\partial x}(x_{0}, y_{0})(x-x_{0})+\cfrac{\partial f}{\partial y}(x_{0}, y_{0})(y-y_{0})$$
#### Example
***
Let $f(x,y) = 2x^2y+3y^{2}$ and let $(x_{0}, y_{0}) = (1, 1)$
Then $f(x_{0}, y_{0}) = 5$
and the first partial devivatives at $(x_{0}, y_{0})$ are
$$f_{x}(1, 1) = 4\vert_{x=1, y=1} = 4$$
$$f_{y} (1, 1) = 2x^{2+6y\vert_{x=1, y=1}}= 8$$
It follows that the tangent plane at $(1, 1)$ has the eqauation. 
$$z - 5 = 4(x-1)+8(x-1)$$
and the linearization of $f$ at $(1, 1)$ is 
$$L_{f}(x, y) = 5 + 4(x-1)+ 8(x-1)$$
Let $(x, y) = (1.1, 1.1)$ 
Then, $f(x, y) = 6.291$
while, $L_{f}(x, y) = 6.2$ for an error of $6.292-6.2 = 0.092$

**BUT**
***
Writting formulas that involve the partial derivatives of function of $n$ can be cumber some.

The can be adressed by expressing collections of partial derivative of functions of several variables using vectors and matricies,

By convention, $p_{0} = (x_{1}^{(0)}, x_{2}^{(0)}, \dots, x_{n}^{(0)})$, 
which can be identfied with the positon vector $p_{0} = \langle x_{1}^{(0)}, x_{2}^{(0)}, \dots, x_{n}^{(0)}\rangle$
is considered to be a column vector 
$$
P_{0} =
\begin{bmatrix}
x_{1}^{(0)}\\
x_{2}^{(0)}\\ 
\vdots\\ 
x_{n}^{(0)}
\end{bmatrix}
$$
Also, by convention, given a function of $n$ variables, $f:D \subseteq \mathbb{R}^{n}\rightarrow\mathbb{R}$ , the collection of its parital derivatives with respect to all of its variables is written as a row vector
$$\nabla f(p_{0}) = \begin{bmatrix}
\cfrac{\partial f}{\partial x_{1}}(p_{0}) & \cfrac{\partial f}{\partial x_{2}}(p_{0}) & \dots & \cfrac{\partial f}{\partial x_{n}}(p_{0})
\end{bmatrix}$$

This vector is the gradient of $f$ at $p_{0}$

Viewing the partial derivatives of $f$ as a vector allows us to use vector operation to desscibe, the linearization of $f$.

Specifically, the linerazation of $f$ at $p_{0}$ evalueated at point $p = x_{1}, x_{2}, \dots , x_{n}$
can be written as 

$$
\begin{align}
L_{f}(p) &= f(p_{0}) + \cfrac{\partial f}{\partial x_{1}}(p_{0})(x_{1}-x_{1}^{(0)}) + \cfrac{\partial f}{\partial x_{2}}(p_{0})(x_{2}-x_{2}^{(0)}) + \dots + \cfrac{\partial f}{\partial x_{n}}(p_{0})(x_{n}-x_{n}^{(0)})\\
&=f(p_{0}) + \sum_{i=1}^{n} \cfrac{\partial f}{\partial x_{i}}(p_{0})(x_{i}-x_{i}^{(0)})\\
&= f(p_{0}) + \nabla f(p_{0}) \cdot (p-p_{0})  
\end{align}
$$

#### Example
***

Let $f: \mathbb{R}^{3}\rightarrow \mathbb{R}$ be defiend by
$$f(x, y, z) = 3x^{2}y^{3}z^{4}$$
Then, $\nabla f(x, y, z) = \begin{bmatrix} f_{x} & f_{y} & f_{z}\end{bmatrix} = \begin{bmatrix} 6xy^{3}z^{4}& 3x^{2}3y^{2}z^{4} & 12x^{2}y^{2}z^{3}\end{bmatrix}$
Let $(x_{0}, y_{0}, z_{0}) = (1, 2, -1)$

Then
$$
\begin{align}
\nabla &= f(x_{0}, y_{0}, z_{0})\\
&= \nabla f(1, 2, -1) \\
&= \begin{bmatrix} f_{x}(1, 2, -1) & f_{y}(1, 2, -1), f_{z}(1, 2, -1)\end{bmatrix} \\
&= \begin{bmatrix} 48 & 36 & -96\end{bmatrix}
\end{align}
$$
It follows that the linearization of $f$ at $(x_{0}, y_{0}, z_{0})$ is
$$
\begin{align}
l_{f}(x, y, z) &= f(1, 2, -1) + \nabla f(1, 2, -1)\cdot\langle x-1, y-2, z+1\rangle\\
&= 24 + \langle 48, 36, -96\rangle \cdot \langle x-1, y-2, z+1\rangle\\
&= 24 + 48(x-1) + 36(y-2)-96(z+1)\\
&= 48x + 36y - 96z-192
\end{align}
$$

at point $(1.1, 1.9, -1.1)$ we have $f(1.1, 1.9, -1.1) \approx 36.5$
while at $L_{f}(1.1, 1.9, -1.1) = 34.8$


## The Jacobian Matrix

The jacobian matrix describes the linearization of a vector valued function, 
where as the gradient does it for a scalar-valued function.
