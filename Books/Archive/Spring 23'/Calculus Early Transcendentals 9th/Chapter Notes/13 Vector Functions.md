# **13.1 Vector Functions and space Curves**

in general a **function**
- is a rule that assigns to each element in the domain and element in the range

A **Vector Valued Function** (or vector function)
- function whose domain is a set of real numbers and whose range is a set of vectors.

Vector functions $r$ whose values are 
three-dimensional vectors
- for every number $t$ in the domain of $r$ there is a unique vector in $V_3$ denoted $r(t)$
- if $f(t),\ g(t),\ h(t)$ are the components of the vector $r(t)$ then $f, \ g, \ h$ are real-valued functions 
- **component functions of** $r$ 
	- $f, \ g, \ h$ 

the unique vector can be written as such,
$$r(t) = \langle f(t), \,g(t), \, h(t) \rangle = f(t)i+g(t)j+h(t)k$$

usually, domain $r$ consists of all values of $t$ for which $r(t)$ is defined


##### **Limits and continuity** 

The **limit** of a vector function $r$ is defined by taking the limits of its component functions

If $r(t) = \langle f(t), \,g(t), \, h(t) \rangle$ then
$$\lim_{t\rightarrow a} r(t) = \left\langle \lim_{t\rightarrow a}f(t), \, \lim_{t\rightarrow a}g(t), \, \lim_{t\rightarrow a}h(t) \right\rangle$$
- provided the limits of the component functions exist

We could also use $\epsilon-\delta$ definition (Exercise 54)

**Space Curve**
- set $C$ of all points $(x, y, z)$ in space where continuous real-valued parametric equations of a vector function and $t$ vary through the interval $I$
	- $C$ is being traced out by a moving particle
	- $r(t) = \langle f(t), \,g(t), \, h(t) \rangle$ is the position vector of point $P(f(t),\, g(t),\, h(t))$  on $C$ 
- Thus any continuous vector function $r$ defines a space curve $C$ that is traced out by the tip of the moving vector $r(t)$


## Example #1 

If 
$$
r(t) = \left\langle f^3, \ln(3-t), \sqrt{t} \right\rangle 
$$
then the component functions are 
$$
f(t) = t^3 \quad g(t) = \ln{(3-t)} \quad h(t) = \sqrt{t}
$$
The domain of $r$ 
- consist of all values of $t$ for which the expression for $r(t)$ is defined. 

The component functions are all defined when
- $3-t\geq 0$ and $t\geq 0$ 

Therefore domain of $r$ is the interval $[0,3)$

## Example #2

Find the limit of $r(t)$ 
$$r(t)=(1+t^3)\,i+t\,e^{-t}j+\cfrac{\sin{t}}{t}k$$
*Solution :*

Limit of $r$ is the vector whose components are the limits of the component functions of $r$
- take the limit of the component functions
$$
\begin{aligned}
\lim_{t\rightarrow 0} r(t) &= \left[\lim_{t\rightarrow 0}\ (1+t^3)\right]\,i+\left[\lim_{t\rightarrow 0}\ t\,e^{-t}\right ]\,j+\left[\lim_{t\rightarrow 0}\ \cfrac{\sin{t}}{t}\right]\,k\\
&= i + k
\end{aligned}
$$

## Example #3

Describe the curve defined by the vector function
$$r(t) = \langle 1 + t, \ 2+5t, \ -1+6t \rangle$$
*Solution :*

Corresponding parametric equations are,
$$
\begin{aligned}
x &= 1+t\\
y &= 2+5t\\
z &= -1+6t
\end{aligned}
$$
We can describe the parametric equations 
as a line passing thought the point $(1, 2, -1)$ 
and parallel to the vector $\langle 1, 5, 6 \rangle$

Also observe the function can be written as 
$$r = r_0 + tv$$
where,
$$
\begin{aligned}
r_0 &= \langle 1, 2, -1 \rangle\\
v &= \langle 1, 5, 6 \rangle
\end{aligned}
$$
and so the vector equation becomes,
$$
\begin{aligned}
r &= (i+2j-k)+t(i+5j+6k)\\
&or \\
&= (1+1t)\,i + (2+5t)\,j + ((-1)+6t)\,k
\end{aligned}
$$


## Example #4

Sketch the curve whose vector equation is,
$$r(t) = \cos{(t)}\,i + \sin{(t)}\,j + t\,k$$
*Solution :*

The parametric equations for this curve are 
$$
\begin{aligned}
x &= \cos{(t)}\\
y &= \sin{(t)}\\
z &= t
\end{aligned}
$$
since $x^2 + y^2 = \cos^2{(t)} + \sin^2{(t)} = 1$ for all values of $t$
the curve must lie on the circular cylinder $x^2+y^2=1$
The point $(x, y, z)$ lies directly above point $(x, y, 0)$ 
- which moves counter clockwise around the circle $x^2+y^2=1$  int he xy-plane.
The Projection of the curve has a vector equation of $r(t) = \langle \cos{(t)}, \sin{(t)}, 0 \rangle$ 
Since, $z = t$, the curve spirals upwards around the cylinder as $t$ increases.
- the curve is known as a helix


## Example #5 

Find a vector equation and a parametric equation for the line segment that joins the point $P(1, 3, -2)$ and $Q(2, -1, 3)$ 

*Solution :*

Find vector equation for the line segment that joins the tip of the vector $r_0$ to the tip of the vector $r_1$ 
$$r(t) = (1-t)r_0+r_1 \quad 0\leq t\leq 1$$
Now we take $r_0$ and $r_1$  to obtain the vector equation of the line segment from $P$ to $Q$.
$$
\begin{aligned}
r(t) &= (1-t)\langle 1, 3, -1 \rangle+ t \langle 2, -1, 3 \rangle\\
&or\\
r(t) &=\langle 1+t,\, 3-4t,\, -2+5t \rangle
\end{aligned}
$$
and the corresponding parametric equations are 
$$
\begin{aligned}
x &= 1+t\\
y &= 3-4t\\
z &= -2+5t
\end{aligned}
$$

## Example #6

Find a vector function that represents the curve of the intersection of the cylinder $x^2+y^2=1$ and the plane $y+z=2$ 

*Solution :*

The projection of the vector function $C$ onto the xy-plane $\textit{proj}_{\mathbf{C}}{\mathbf{xy}}$  is the circle $x^2+y^2=1, \ z = 0$ 
we know from 10.1.2 that we can write the parametric equation as ,
$$
\begin{aligned}
x &= \cos{(t)}\\
y &= \sin{(t)}\\
z &= 2 - y\\
&= 2-\sin{(t)}\\
&0\leq t\leq 2\pi
\end{aligned}
$$
and so the corresponding vector equation is 
$$r(t)=\cos{(t)}\, i + \sin{(t)}\, j + (2-\sin{(t)})\,k\quad 0\leq t\leq 2\pi $$
This equation is the *parametrization* of the curve $C$

# **13.2 Derivates and Integrals of Vectors**

##### **Derivatives**

The derivative $r'$ of a vector function $r$ 
$$
\frac{dr}{dt} = r'(t) = \lim_{h\rightarrow 0} \frac{r(t+h)-r(t)}{h}
$$

if the points $P$ and $Q$ have position vector $r(t)$ and $r(t+h)$ then 
- $\vec{PQ}$ represents the vector $r(t+h)-r(t)$ 
	- which can be regarded as a secant vector.
if $h >0$ 
- the scalar multiple $(\frac{1}{h})(r(t+h))-r(t)$ 
	- has the same direction as vector $\vec{PQ}$ or $r(t+h)-r(t)$
As $h\rightarrow 0$ 
- the vector approaches a vector that lies on the tangent line
	- for this reason vector $r'(t)$ is the **tangent vector** to the curve defined by $r$ at the point $P$
**Tangent line**
- tangent line to $C$ at $P$ is defined to be the line through $P$ parallel to the tangent vector $r'(t)$ 

**Unit Tangent Vector**
$$T(t) = \frac{r'(t)}{|r'(t)|}$$

to compute the derivative of function $r$ 
- differentiate each component of $r$
$$r'(t) = \langle f'(t), \,g'(t), \, h'(t) \rangle = f'(t)i+g'(t)j+h'(t)k$$

##### **Integrals**

The **definite integral** of a continuous vector function is a vector
- But we can express the integral of $r$ in terms of the integrals of its component functions
$$\int_{b}^{a}r(t) = \lim_{n\rightarrow \infty} \ \sum_{i=1}^n r(t_i^*)\, \Delta t$$
$$
= \lim_{n\rightarrow \infty} \left[\left(\sum_{i=1}^n f(t_i^*)\, \Delta t\right)i + \left(\sum_{i=1}^n g(t_i^*)\, \Delta t\right)j + \left(\sum_{i=1}^n h(t_i^*)\, \Delta t\right)k\right]
$$

and so

$$
\int_{b}^{a}r(t) = \left(\int_{b}^{a}f(t) \ dt\right) i + \left(\int_{b}^{a}g(t) \ dt\right) j + \left(\int_{b}^{a}h(t) \ dt\right) k
$$

This means, 
- we can evaluate an integral of a vector function by integrating each component function.

extending the *Fundamental Theorem Of Calculus* to continuous vector function
$$\int_{b}^{a}r(t) \ dt = R(t)]_a^b = R(b) - R(a)$$

where $R$ is an
- *antiderivative* of $r$ 
	- that is $R'(t) = r(t)$ 

## example #1

(a) Find the derivative of $r(t) = (1+t^3)\, i + te^{-1}\, j + \sin{(2t)}\,k$ 
(b) Find the unit tangent vector at the point where $t - 0$

*Solution :*

(a) As we take the limit of each component, we take the derivate of each component of $r$:
$$r'(t) = (3t^2)i + ((1-t)e^{-1})j + (2\cos{(2t)})k$$
(b) since, $r(0) = i$ and $r'(0) = j+2k$ 
The unit tangent vector at the point $(1, 0, 0)$ is 
$$T(0) = \cfrac{r'(0)}{|r'(0)|} = \cfrac{j+2k}{\sqrt{1+4}} = \cfrac{1}{\sqrt{5}}j + \cfrac{2}{\sqrt{5}}k$$


## Example #2 

For the curve $r(t) = \sqrt{t}\, i + (2-t)j$, find $r'(t)$ 
*Solution :*
$$r'(t) = \cfrac{1}{2\sqrt{t}}i-j$$
The curve is a plane curve and elimination of the parameter from the equations $x = \sqrt{t} \ y = 2-t$  
gives, $y = 2-x^2, \ x\geq 0$ 

## Example #3

Find the parametric equations for tge tangent line to the helix with parameric equations
$$x = 2\cos{(t)} \quad y = \sin{(t)} \quad z = t$$
at the point $(0, 1, \frac{\pi}{2})$ 

*Solution :*

the vector equation of the helix is $r(t) = \langle 2\cos{(t)}, \sin{(t)}, t\rangle$ 
so, the derivative is 
$$r'(t) = \langle -2\sin{(t)}, \cos{(t)}, 1\rangle$$

 # 13.4 **Motion in Space**