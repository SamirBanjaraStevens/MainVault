# Ch 1.1
State the order of the given ordinary differential equation. Determine whether the equation is linear or nonlinear
## Problem 4
$$\cfrac{d^2u}{dr^2}+\cfrac{du}{dr}+u=\cos(r+u)$$
**Solution:** Second order non-linear equation
## Problem 5
$$\cfrac{d^2y}{dx^2}=\sqrt{ 1+\left(\cfrac{dy}{dx}\right)^2 }$$
**Solution:** Second order non-linear equation 
## Problem 32
Find the values of $m$ so that the function $y=e^{mx}$ is a solution of the given differential equation, 
$$5y^{'}=2y$$
**Solution:** First find the derivative of the given function $y=e^{mx}$ 
$$
\begin{align}
\frac{d}{dx}(y)&=\frac{d}{dx}(e^{mx}) \\
y^{'}&=me^{mx}
\end{align}
$$
Substitute $y$ and $y'$ into the given differential equation $5y^{'}=2y$
$$
\begin{align}
5(me^{mx})&=2(e^{mx}) \\
5m&=2 \\
m & = \cfrac{2}{5}
\end{align}
$$
Thus, $y=e^{\frac{2}{5}x}$ is a solution to $5y^{'}=2y$


# Ch 2.1
Find the critical points and phase portrait of the given autonomous first-order differential equation. Classify each critical point as asymptotically stable, unstable, or semi-stable. By hand, sketch typical solution curves in the regions in the $xy$-plane determined by the graphs of the equilibrium solutions.
## Problem 26
$$\cfrac{dy}{dx}=y(2-y)(4-y)$$
**Solution:**
### Find Critical Points
Seprate RHS to $0$ to finnd critical points,
$$y(2-y)(4-y)=0$$

Critical points: $y=0$, $y=2$, $y=4$

### Classifiy critical points
To classifiy critical points we must first look at the phase line and extrapolate it into a phase portrait.

Interval between critical points: $(-\infty, 0), (0,2), (2, 4), (4, \infty)$
#### For $y\in (-\infty, 0)$
Test value $y=-1$,
$$
\begin{align}
-1(2+1)(4+1)=-15
\end{align}
$$
Decreasing.

#### For $y \in(0, 2)$
Test value $y=1$,
$$1(2-1)(4-1)=3$$
Increasing.
#### For $y \in(2,4)$
Test value $y=3$,
$$3(2-3)(4-3)=-3$$
Decreasing.
#### For $y \in(4, \infty)$
Test value $y = 5$,
$$5(2-5)(4-5)=15$$
Increasing.

##### Phase Line & Point

***ATTACHED AS IMAGE***
### Stability
For $y=0$ the solution moves away from $y=0$ from both sides, thus, unsatble.
For $y=2$ the solution moves towards $y=2$ from both sides, thus stable.
For $y=4$ the solution moves away from $y=4$ from both sides. thus unstable.
# Ch 2.2 
Solve the given differential equation by separation of varibles. 
## Problem 2
$$\cfrac{dy}{dx}=(x+1)^2$$
**Solution:**
Separate $y$ variables into one side and $x$ into another.
$$dy=(x+1)^2dx$$
Take the integral of both sides
$$
\begin{align}
\int dy \, &=\int (x+1)^2 \, dx \\
y & = \frac{1}{3}(x+1)^3+C \\
 & =\cfrac{x^3}{3}+x^{2+x}+C
\end{align}
$$
## Problem 7
$$\cfrac{dy}{dx}=\left(e^{3x+2y}\right)$$
**Solution:**
$$
\begin{align}
\cfrac{dx}{dy}  & = e^{3x} \cdot e^{2y} \cdot dx \\
\cfrac{1}{e^{2y}}dy &= e^{3x}dx \\
\end{align}
$$
Take the integral of both sides.
$$
\begin{align}
\int \cfrac{1}{e^{2y}} \, dy = \int e^{3x} \, dx  
\end{align}
$$
*Part 1:*
$$\int \cfrac{1}{e^{2y}} \, dx = -\frac{1}{2}e^{-2y}+C$$
*Part 2:*
$$\int e^{3x} \, dx = \frac{1}{3}e^{3x} + C $$
So we now have, 
$$
-\frac{1}{2}e^{-2y} = \frac{1}{3}e^{3x} + C 
$$
Find $y$
$$
\begin{align}
-\frac{1}{2}e^{-2y} & = \frac{1}{3}e^{3x} + C  \\
e^{-2y} & = -\cfrac{2}{3} e^{3x} + C \\
\ln(e^{-2y}) & =\ln\left(-\cfrac{2}{3}e^{3x}+C\right) \\
-2y  & = \ln\left(-\cfrac{2}{3}e^{3x}+C\right) \\
y  & = -\frac{1}{2}\ln\left(-\cfrac{2}{3}e^{3x}+C\right)
\end{align}
$$
Final explicit solution: 
$$
y   = -\frac{1}{2}\ln\left(-\cfrac{2}{3}e^{3x}+C\right)
$$