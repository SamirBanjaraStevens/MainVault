# Chapter 2.3

## Problem 13
$$x^2y'+x(x+2)y=e^x$$
Divide all terms by $x^2$ to get the normal form,
$$y'+\cfrac{(x+2)y}{x}=\cfrac{e^x}{x^2}$$
Integrating factor is given by,
$$\begin{align}
\mu(x)&=\exp \left[ \int 1+\frac{2}{x} \, dx  \right] \\
 & =\exp \left[ x+2\ln|x| \right] \\
&= e^xe^{x^2} \\
 & =e^x x^2
\end{align} $$
multiply the integrating factor,
$$e^{x}x^2+e^{x}x(x+2)y=e^x$$
take the integral of the LHS,
$$
\begin{align}
e^{x}x^2y&=\int e^x \, dx  \\
 & =e^x+C
\end{align}
$$
solve for $y$,
$$y=\frac{1}{x^2}+C$$
Because we have a $x$ in the denominator, $x\neq 0$ and $x=0$ is a singularity,
Thus interval is $x \in(-\infty,0)\cup(0,\infty)$

Additionally, $\cfrac{C}{x^2e^x}$ is a transient term

## Problem 23
Solve the IVP 
$$y \cfrac{dx}{dy}-x=2y^{2} \ ; \ y(1)=5$$
1. Rearrange the equation
$$\cfrac{dx}{dy}-\cfrac{x}{y}=2y$$
2. Identify the integrating factor,
$$
\begin{align}
\mu(x) &= \exp \left[ \int -\frac{1}{y} \, dx  \right]  \\
 & =\exp \left[ -\ln(y) \right] \\
 & = \frac{1}{y} 
\end{align}
$$
3. Multiply by the Integrating factor
$$\frac{1}{y} \frac{dx}{dy} - \frac{1}{y} \frac{x}{y} = \frac{1}{y}2y$$
	1. simplify
$$\frac{d}{dy}\left( \cfrac{x}{y} \right) = 2$$
4. Integrate with respect to $y$,
$$\frac{x}{y}=\int 2 \, dy =2y+C$$
5. Solve for $x$,
$$x=2y^2+C$$
6. Plug in $x=1, y=5$
$$1=2(5)^2+C$$
7. Final solution
$$x = 2y^2-49$$
# Chapter 2.4
## Problem 4
$$(\sin y-y\sin x)dx+(\cos x+x\cos y-y)dy=0$$
$$
\begin{align}
M(x,y) & = \sin y-y\sin x \\
N(x,y)  &  = \cos x+x\cos y-y
\end{align}
$$
  Calculate $\cfrac{\partial M}{\partial y}$ and $\cfrac{\partial N}{\partial x}$ 
  $$
  \begin{align}
\cfrac{\partial M}{\partial y} & =\cfrac{\partial}{\partial y}\left( \sin y \right) -\cfrac{\partial}{\partial y}\left( y\sin x \right) \\
 & =\cos y-\sin x 
\end{align}
$$
And $\cfrac{\partial N}{\partial x}$,
$$
\begin{align}
\cfrac{\partial N}{\partial x} & = \cfrac{\partial}{\partial x}\left( \cos x \right) +\cfrac{\partial}{\partial x}(x\cos y)-\cfrac{\partial}{\partial x}(y) \\
 & =-\sin x+\cos y
\end{align}
$$
Thus we have shown, $\cfrac{\partial M}{\partial y} = \cfrac{\partial N}{\partial x}$ and so the given equation is an exact equation

Then to solve it we integrate $M(x,y)$ with respect to $x$
$$\int \sin y-y\sin x \, dx = x\sin y+y \cos x+g(x)$$
then differentiate with respect to $y$
$$\cfrac{d}{dx}\left( x\sin y+y\cos x+g(x) \right) = x\cos(y)+\cos x+g'(x)$$
then we set $x\cos(y)+\cos x+g'(x)$ to $N(x,y)$
$$
\begin{align}
x\cos(y)+\cos x+g'(x) &= \cos x+x\cos y-y \\
g'(x)=-y \\
\text{or} \\
g(x)=\cfrac{-y^2}{2}
\end{align}
$$
We have shown that,
$$f(x, y) = x\sin y+y\cos x-\cfrac{y^2}{y}$$
and the solution we see is,
$$x\sin y+y\cos x-\cfrac{y^2}{y}=C_{1}$$
## Problem 29
Verify that the given differential equation is not exact. Multiply the given differential equation by the indicated integrating factor and verify that the new equation is exact. Solve.

$$(-xy\sin x+2y\cos x)dx+(2x\cos x)dy=0 \ ; \ \mu(x, y)=xy$$
we identify,
$$
\begin{align}
M(x,y) & = -xy\sin x+2y\cos x \\
N(x,y) & = 2x \cos x
\end{align}
$$
verify that $M(x,y)\neq N(x,y)$
$$
\begin{align}
\cfrac{\partial M}{\partial y}&=2\cos x-x\sin x \\
\cfrac{\partial N}{\partial x} & = 2\cos x-2x\sin x
\end{align}
$$
Thus not exact.
Lets multiply by the given integrating factor.
$$
\begin{align}
\mu(x,y)M(x,y)dx+\mu(x,y) N(x,y)dy&=0 \\
 \\
(xy)(-xy\sin x+2y\cos x)dx+(xy)(2x\cos x)dy&=0 \\
(-x^2y^2\sin x+2xy^2\cos x)dx+(2x^2y\cos x)dy&=0
\end{align}
$$

Testing for exactness,
$$
\begin{align}
\cfrac{\partial M}{\partial y}\left( -x^2y^2\sin x+2xy^2\cos x \right)  & =-2x^2y\sin x+4xy\cos x \\
\cfrac{\partial N}{\partial x}\left( 2x^2y\cos x \right) & =4xy\cos x-2x^2y\sin x 
\end{align}
$$
They are now exact. Thus there is function $f(x,y)$
***
Now solve it
$$(-x^2y^2\sin x+2xy^2\cos x)dx+(2x^2y\cos x)dy=0$$
Integrate $(-x^2y^2\sin x+2xy^2\cos x)$ with respect to x
$$
\int (-x^2y^2\sin x+2xy^2\cos x) \, dx =x^2y^2\cos x+g(x)
$$
Differentiate with respect to y and set the result equal to $N(x,y)$, we obtain, 
$$
\begin{align}
\cfrac{d}{dx}\left( x^2y^2\cos x+g(x)\right)&= 2x^2y\cos(x)+g'(x) \\
 \\
2x^2y\cos x+g'(x) & =2x^2y\cos x \\
g'(x)=0
\end{align}
$$

thus we find, 
$$f(x,y) = x^2y^2\cos(x)$$
# Chapter 2.5

## Problem 18
Solve the given differential equation (Bernoulli equation) by using an appropriate substitution.
$$x \cfrac{dy}{dx}-(1+x)y=xy^2$$
