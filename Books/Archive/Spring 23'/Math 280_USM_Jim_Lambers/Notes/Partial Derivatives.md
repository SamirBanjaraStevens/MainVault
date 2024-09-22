## Techniques

Describe the most practical techniques for computong partial derivatives

It is practical to compute the partial derivative as a function of all of the independent variables, which can then be evalueated at any point at wich we wish to know the value of the partial derivative. 
- Creating a function $\cfrac{\partial f}{\partial x_{i}} (x_{1}, x_{2}, \dots, x_{n})$  and then the values can be substituted for the independent variables, $x_{1}, x_{2}, \dots, x_{n}$ 

#### Example
***
To compute $f_{x}\left(\cfrac{\frac{\pi}{2}}{\pi}\right)$ of $f(x,y) = e^{-(x^{2}+y^{2})}\sin(3x)\cos(4y)$
we treat $y$ as a constant, since we are differentiating with respect to $x$.
Using the Product Rule, and Chain Rules
we obtain,
$$
\begin{align}
f_{x}\left(\cfrac{\frac{\pi}{2}}{\pi}\right) &= \cfrac{\partial}{\partial x}[e^{-(x^{2}+y^{2})}\sin(3x)\cos(4y)] \ \bigg\rvert_{x=\cfrac{\pi}{2}, y = \pi}\\
&= \cos_{4}y \cfrac{\partial}{\partial x}[e^{-(x^{2}+y^{2})}\sin(3x)] \bigg\rvert_{x=\cfrac{\pi}{2}, y = \pi}\\
&= \cos(4y)[-2xe^{-(x^{2}+y^{2})}\sin(3x)+3e^{-(x^{2}+y^{2})}\cos(3x)] \bigg\rvert_{x=\cfrac{\pi}{2}, y = \pi}\\
&= \pi e^{\cfrac{-5\pi^{2}}{4}}
\end{align}
$$

