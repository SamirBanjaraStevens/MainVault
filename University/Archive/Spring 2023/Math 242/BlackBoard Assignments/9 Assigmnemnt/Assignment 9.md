## Question 1
Find The maximum value of the function : $f(x, y, z) = x + 3y+ 5z$ 
Subject to the constraint : $x^{2}+y^{2}+z^{2} = 35$

1. Get gradient and set it equal to $(0, 0, 0)$

$\nabla f = \left\langle \cfrac{\partial f}{\partial x}, \cfrac{\partial f}{\partial y}, \cfrac{\partial f}{\partial z} \right\rangle$
$\nabla f = \langle 1, 3, 5 \rangle$
So, gradient at $(0, 0, 0)$ is given by $\nabla = f(0, 0, 0) = (1, 3, 5)$

2. Make a hessian matrix, and study the eigen values.

$$
H_{f} =
\begin{bmatrix}
0 & 0 & 0\\
0 & 0 & 0 \\ 
0 & 0 & 0
\end{bmatrix}
$$
Thus since the hessian matrix of the given function is a zero matrix, it is singular, and it inconclusive.

3. Lets try, $f(-1, -3, -5)$ and $f(1, 3, 5)$

So the *min* is at $-35$ and *max* is at $35$


## Question 2
Evaluate the double integral : $\int \int_{D} \cfrac{2y}{x^{2}+1} \, dA$ 
where : $d = \{ (x, y) \mid 0\leq x \leq 1, \quad 0 \leq y \leq \sqrt{ x } \}$ 

1. $\int _{0}^{1} \cfrac{2y}{x^{2}+1} \, dx$
	- Take constant out
		- $2y \int _{0}^{2} \cfrac{1}{x^{2}+1} \, dx$
	- $\int \cfrac{1}{1+x^{2} \, dx}= \arctan(x)$ identity 
		- $2y[\arctan(x)]\mid_{0}^{1} = \cfrac{2y\pi}{4}=\cfrac{y\pi}{2}$
2. $\int _{0}^{\sqrt{ x }} \cfrac{\pi y}{2} \, dy$
	- take constant out
		- $\cfrac{\pi}{2}\int _{0}^{\sqrt{ x }} y \, dy$
	- Power rule: $\int x^{a} \, dx = \cfrac{x^{a+1}}{a+1}$ 
		- $\cfrac{\pi}{2}\left[\cfrac{y^{2}}{2}\right]_{0}^{\sqrt{ x }} = \cfrac{\pi}{2}\left[\cfrac{x}{2}\right] = \cfrac{\pi x}{4}$

Thus, 
$$\int \int_{D} \cfrac{2y}{x^{2}+1} \, dA = \cfrac{\pi x}{4}$$