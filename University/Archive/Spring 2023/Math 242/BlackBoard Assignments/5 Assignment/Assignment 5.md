---
Author : Samir Banjara
Date : 02/27/22
---

### **Question 1**

Express the curve, parametrized by $t$, traversed by an object along the cylinder $x^2+y^2=4$ that moves up from the $xy$-plane at a linear rate.

*Solution :*

So, we are expressing the curve as a vector function. 
we can find the parameterization for the intersection of the circular cylinder ($x^2+y^2=4$) in $\mathbb{R}^3$ and the plane ($z = xy$) by substituting the parametric equations ($x = r\sin{(t)},\, y=r\cos{(t)}$ ) with the $r =\sqrt{4} = 2$
$$x = r\cos{(t)}, \quad y=r\sin{(t)}, \quad r =\sqrt{2} = 2$$
$$
\begin{aligned}
z &= xy\\
&=(2\sin{(t)})(2\cos{(t)})\\
&= 4\sin{(t)}\cos{(t)}\\
&= 2\sin{(2t)}
\end{aligned}
$$
thus, the vector function of the curve can be represented as, 
$$r(t) = \langle 2\sin{(t)},2\cos{(t),2\sin{(2t)}}\rangle$$

### **Question 2**

Find the length of the segment of the helix,
$$
\vec{r}(t) = \left\langle \cos{(t)}, \sin{(t)}, t \right\rangle \quad \text{ where } t\in[\,0,2\pi\,]
$$

*Solution :*

Parameter interval: $[\,0,2\pi\,]$ 
$r'(t) = \left\langle -\sin{(t)}, \cos{(t)}, 1 \right\rangle$
$|r'(t)| = \sqrt{sin^2{(t)}+\cos^2{(t)}+1^2} = \sqrt{2}$ 
and so, the length is,
$$
\int_0^{2\pi}\sqrt{2}\, dt = 2\sqrt{2\pi}
$$

## **Notes:**
Line segment from $r_0$ to $r_1$ is given by the vector equation 
$$
\begin{aligned}
r(t)&=(1-t)r_0+t\,r_1\\
&or\\
\Delta r &= r(t+\Delta t) -r(t)
\end{aligned}
$$

If points are close together,
the length of $\Delta r$ is close to he length of the curve between the two points.
If we add up the lengths of many such tiny vectors, placed head to tail along a segment of the curve, we get an approximation to the length of the curve over that segment.
In the limit, this sum turn into an integral that computes the length of the curve.

$$
\vert\Delta r\vert = \cfrac{\Delta r}{\Delta t} \Delta t \approx \vert r'(t)\vert\Delta t,
$$

when $\Delta t$ is small.

Then the length of the curve between $r(a)$ and $r(b)$ is 
$$
\begin{aligned}
\lim_{n\rightarrow\infty} \sum_{i=0}^{n-1}\vert\Delta r\vert &= \lim_{n\rightarrow\infty} \sum_{i=0}^{n-1} \cfrac{\Delta r}{\Delta t} \Delta t\\
&= \lim_{n\rightarrow\infty} \sum_{i=0}^{n-1}|r'(t)| \Delta t\\
&=\int_a^b |r'(t)|\,dt
\end{aligned}
$$
Works if between $a$ and $b$ the segment of curve is traced out exactly once. 
