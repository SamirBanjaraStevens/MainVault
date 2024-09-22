Samir Banjara
04/26/23
7:08 PM

## Question 1
Evaluate the double integral $\iint_{D} \ xy^{2} \ dA$ 
Where $D$ is enclosed by $x=0$ and $x=\sqrt{ 1-y^{2} }$
#### Solution 
***
**Intersection:**
$0=\sqrt{ 1-y^{2} }$
    $y= \pm1$ 

**Type $II$ region:**
$D=\{ (x,y)\mid -1\leq y\leq 1, \quad 0\leq x\leq \sqrt{ 1-y^{2} }\}$

Thus, 
$$
\begin{align}
\iint_{D} \ xy^{2} \ dA  &= \int _{-1}^{1}\int _{0}^{\sqrt{ 1-y^{2} }} (xy^{2}) \, dx  \, dy\\
&= y^{2}\int _{-1}^{1}\left[ \frac{x^{2}}{2} \right]_{x=0}^{x=\sqrt{ 1-y^{2} }}  \, dy\\
&= \int _{-1}^{1}\left( \cfrac{(1-y^{2}) \cdot y^{2}}{2}\right)  \, dy\\
&= \frac{1}{2}\int _{-1}^{1} -y^{4}+y^{2} \ dy\\
&= \frac{1}{2}\left( -\int _{-1}^{1}y^{4} \ dy + \int _{-1}^{1} y^{2}\ dy  \right) \\
&=\frac{1}{2}\left( \frac{-2}{5} + \frac{2}{3} \right) \\
&=\frac{2}{15}
\end{align}
$$

## Question 2

Set up the integral of the function $f(x, y, z) = x + y + z$ over the region $\mathbb{R}^{3}$ 
bounded by $x+3y+z=2$, $x=3y$, $x=0$, $z=0$
#### Solution 
***
Determine the limits of integration for each variabe

From the equation $x=3y$
we can focus on the region where $x\geq 0$ 

Next we need to find the limits for $y$ and $z$ at ta given value of $x$
we can rearrange the equation $x+3y+z=2$ to get $z=2-x-3y$
Therefore, the limits for $y$ and $z$ are $0\leq y\leq \frac{1}{3}$ and $0\leq z\leq 2-x-3y$ respectively.

Finally we integrate $f(x,y,z)=x+y+z$ over the region $\mathbb{R}^{3}$ as follows:
$$
\begin{align}
V &= \int_{\mathbb{R}^{3}} \ f(x,y,z) \ dV\\
&= \int_{x=0}^{x={3}} \int_{y=0}^{y=\frac{1}{3}x}\int_{z=0}^{z=2-x-3y} \ (x+y+z) \ dz, \ dy, \ dx
\end{align}
$$