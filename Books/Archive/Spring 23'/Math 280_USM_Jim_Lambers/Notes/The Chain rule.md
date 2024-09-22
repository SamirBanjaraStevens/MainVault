In single variable calculus that if a function $g(x)$ is ddifferentiable at $x_{0}$ 
and $f(x)$ is diffrentiable at $g(x_{0})$,
then, the derivative of the composition $(f\circ g)(x)=f(g(x))$ is given by the ==chain rule==. 
$$(f\circ g)'(x_{0})=f'(g(x_{0}))g'(x_{0})$$
<u>Lets generalize the chain rule to functions of several variables.</u>
***
Let $f: D\subseteq \mathbb{R}^{n}\rightarrow\mathbb{R}^{m}$ 
and let $g:U\subseteq \mathbb{R}^{p}\rightarrow D$ 
- that is the range of $g$ is the domain of $f$

Aussume that $g$ if differentiable at point $p_{0}\in U$ 
and that $f$ is differentiable at point $q_{0} = g(p_{0})$  

Then, $f$ has a Jacobian matrix $J_{f}(q_{0})$ and $g$ has a Jacobian matrix $J_{g}(p_{0})$
- the matricies $J_{f}(q_{0})$ and $J_{g}(p_{0})$ contain the first partial derivatives of $f$ and $g$ evulated at at $q_{0}$ and $p_{0}$ respectively.

Then, the **chain rule** states that the **derivative of the composition** $(f\circ g) : U\rightarrow \mathbb{R}^{m}$, defined by $(f\circ g)(x)= f(g(x))$ at $p_{0}$ is **given by** the **Jacobian Matrix** 
$$J_{f\circ g}(p_{0}) = J_{f}(g(p_{0}))J_{g}(p_{0})$$ That is, the product of $f\circ g$ at $p_{0}$ is the prioduct, in the sense of *matrix multiplication* 
- of the derivative of $f$ at $g(p_{0})$ and the derivative of $g$ at $p_{0}$
	- which is entirely analogus to the *Chain Rule* from single-variable calculus

It follows from rules of matrix multiplication that the partial derivatives of the $i$-th component function of $f\circ g$ with respect to the variable $x_{j}$ an independent variable of $g$ 
	- is given by the **dot product** of the **gradient** of the $i$-th component function of $f$ with the vector that contains the partial derivatives of the component functions of $g$ with respect to $x_{j}$ 
***
#### Example
***
Let $f: \mathbb{R}^{3}\rightarrow \mathbb{R}$ be defined by 
$$f(x, y, z) = e^{z} \cos(2x)\sin(3y)$$
and let $g: \mathbb{R}\rightarrow\mathbb{R}^{3}$ be a vector valued function of one variable defiend by
$$g(t)=\langle x(t), y(t), z(t)\rangle = \langle 2t, t^{2}, t^{3}\rangle$$
**Then**, $f\circ g$ is a scalar valued function of $t$,
$$(f\circ g)(t)= e^{z(t)}\cos(2x(t))\sin(3y(t))=e^{t^{3}}\cos(4t)\sin(3t^{2})$$ 
to compute its derivative with respect to $t$ we first compute the gradient
$$\nabla f=[ \ f_{x}, f_{y}, f_{z} \ ] = [ \ -2e^{z}\sin(2x)\sin(3y), 3e^{z}\cos(2x)\cos(3y), e^{z}\cos(2x)\sin(3y) \ ]$$ and $$g'(t) = \langle x'(t), y'(t), z'(t)\rangle = \langle 2, 2t, 3t^{2}\rangle$$
$$\begin{align}
x'(t) &= \cfrac{dx}{dt}\\
y'(t) &= \cfrac{dy}{dt}\\
z'(t) &= \cfrac{dz}{dt}
\end{align}$$
then apply the *Chain Rule* to obtain
$$
\begin{align}
\cfrac{df}{dt} &= \nabla f(x(t), y(t), z(t))\cdot g'(t)\\
&=
\begin{bmatrix}
f_{x}(x(t), y(t), z(t)) & f_{y}(x(t), y(t), z(t)) & f_{z}(x(t), y(t), z(t))\\
\end{bmatrix}
\begin{bmatrix}
\cfrac{dx}{dt} \\ 
\cfrac{dy}{dt} \\ 
\cfrac{dz}{dt}
\end{bmatrix}\\
&=f_{x}(x(t), y(t), z(t))\cfrac{dx}{dt}+f_{y}(x(t), y(t), z(t))\cfrac{dy}{dt}+f_{z}(x(t), y(t), z(t))\cfrac{dz}{dt}\\
&= [-2e^{z}\sin(2x)\sin(3y)(2)]+ [e^{z}\cos(2x)\cos(3y)(2t)] + [e^{t^{3}}\cos(2x)\sin(3y)(3t^2)]\\
&= [-4e^{t^{3}}\sin(4t)\sin(3t^{2})]+ [6te^{z}\cos(4t)\cos(3t^{2})] + [3t^{2}e^{t^{3}}\cos(4t)\sin(3t^{2})]
\end{align}
$$
***
#### Example
***
Let $f:\mathbb{R}^{2}\rightarrow\mathbb{R}$ be defined by 
$$f(x, y) = x^{2}y+xy^{2}$$
and let $g: \mathbb{R}^{2}\rightarrow\mathbb{R}^{2}$ be defined by
$$g(s, t) = \begin{bmatrix}
x(s, t)\\
y(s, t)
\end{bmatrix}
= \begin{bmatrix}
2s+t \\ 
s-2t
\end{bmatrix}
$$
then, $f\circ g$ is a scalar-valued function $s$ and $t$ 
$$(f\circ g) = x(s, t)^{2}y(s, t) + x(s, t)y(s, t)^{2}$$
$$= (2s+t)^{2}(s-2t)+(2s-t)(s-2t)^{2}$$
To compute the gradient, which includes its partial derivatives with respect to $s$ and $t$, we first compute
$$\nabla f = [f_{x} \quad f_{y}] = [ \ 2xy+y^{2} \quad x^2+2xy\ ]$$
and, 
$$J_{g}(s, t) = \begin{bmatrix}
x_{s} & x_{t} \\ 
y_{s} & y_{t}
\end{bmatrix} = 
\begin{bmatrix}
2 & 1 \\ 
1 & -2
\end{bmatrix}$$
and then apply the *chain rule* to obtain
$$
\begin{align}
\nabla (f\circ g)(s, t) &= \nabla f(x(s, t), y(s,t))J_{g}(s, t)\\
&= \begin{bmatrix}
f_{x}(x(s, t), y(s, t)) & f_{y}(x(s, t), y(s, t))
\end{bmatrix}
\begin{bmatrix}
x_{s}& x_{t} \\ 
y_{s} & y_{t}
\end{bmatrix}\\
&= \begin{bmatrix}
f_{x}(x(s, t), y(s, t))(x_{s})+f_{y}(x(s, t), y(s, t))(y_{s}) & f_{x}(x(s, t), y(s, t))(x_{t})+f_{y}(x(s, t), y(s, t))(y_{t})
\end{bmatrix}\\
&= \begin{bmatrix}
[2x(t)y(t)+y(t)^{2}](2) + [x(t)^{2}+2x(t)y(t)](1) & [2x(t)y(t)+y(t)^{2}](1) + [x(t)^{2}+2x(t)y(t)](-2)
\end{bmatrix}\\
&= \begin{bmatrix}
4(2s+t)(s-2t)+2(s-2t)^{2}+(2s+t)^{2}+2(2s+t)(s-2t) & 2(2s+t)(s-2t)+ (s-2t)^{2}-2(2s+t)^{2}-4(2s+t)(s-2t)
\end{bmatrix}
\end{align}
$$



contd



















