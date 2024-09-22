recall that if $z = f_{x}(x,y)$, then the partial derivaatives $f_{x}$ and $f_{y}$ are defined as, 
$$
\begin{align}
f_{x}(x_{0}, y_{0}) &= \lim_{ h \to 0 } \cfrac{f(x_{0}+h, y_{0})-f(x_{0}, y_{0})}{h}\\
f_{y}(x_{0},y_{0}) &= lim_{ h \to 0 } \cfrac{f(x_{0}, y_{0}+h)-f(x_{0}, y_{0})}{h} 
\end{align}
$$
and represent the rates of change of $z$ in the 

The **Directional Derivative** of $f$ at $(x_{0}, y_{0})$ in the direction of a unit vector $u = \langle a, b\rangle$ is 
$$D_{u}f(x_{0}, y_{0}) = lim_{ h \to 0 } \cfrac{f(x_{0}+ha, y_{0}+hb)-f(x_{0}, y_{0})}{h}$$
If this limit exists

if $u = i = \langle 1, 0\rangle$ then, $D_{i}f=f_{x}$
if $u = j = \langle 1, 0\rangle$ then, $D_{j}f= f_{y}$

In other words the partial derivatives of $f$ with respect to $x$ and $y$ are just special cases of the directional derivative.

#### Example 1
***
Estimate the value of the directional derivative of the temperature function

**Solution:**
***
Unit vector in south is $u = \cfrac{(i-j)}{\sqrt{ 2 }}$ 
Approximate the directional derivateive $D_{u}T$ by thr avrage rate of change of the temperature between the points where this line intersect $T = 50$ and $T = 0$
Distance between these two points is $75$
so, $D_{u}T \approx \cfrac{60-50}{75}=\cfrac{10}{75}\approx 0.13$

USe the theorem,
$$D_{u}f(x,y) = f_{x}(x,y)a+f_{y}(x, y)b$$
#### Example 2
***
Find the directional derivative $D_{u}f(x,y)$ if 
$$f(x,y) = x^{3}-3xy+4y^2$$
and $u$ is the unit vector given by angle $\theta=\frac{\pi}{6}$ 

What is $D_{u}f(1,2)$?

**Solution:**
***
$$f_{x}(1,2)\cos(\frac{\pi}{6}) + f_{y}(1,2)\sin(\frac{\pi}{6})$$
$$-3\cdot\cfrac{\sqrt{ 3 }}{2}+13\cdot\cfrac{1}{2}$$
$$\cfrac{-3\sqrt{ 3 }+13}{2}$$


