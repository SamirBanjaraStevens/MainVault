## Projections
**Vector Projections** 
- denoted $\text{proj}_{a}B$
- $\overrightarrow{PQ}$ and $\overrightarrow{PR}$ vectors a and b, with the same initial point P. 
- if *S* is the foot of the perpendicular from *R* to the line containing $\overrightarrow{PQ}$, then $\overrightarrow{PS}$ is the vector projection of *b* onto *a*.

**Scaler Projection**
- $\text{comp}_{a}b$
- (component of b along a)
- signed magnitude of the vector projection.
- $|b| \cos(\theta)$
	- $\theta$ is angle between a and b.

Scalar projection of b onto a : 
$$\text{comp}_{a}b = \dfrac{a\cdot b}{\,|a\,|}$$
Vector Projection of b onto a:
$$\text{proj}_{a}b = \left(\dfrac{a\cdot b}{\,|a\,|}\right) \dfrac{a}{\,|a\,|} = \dfrac{a\cdot b}{\,|a\,|^{2}} \: a$$

## 12.4 The cross Product 
Given two on zero vectors $a = \left\langle a_{1}, a_{2}, a_{3}\right\rangle$ and $b = \left\langle b_{1}, b_{2}, b_{3}\right\rangle$ 

if **c** is perpendicular to both **a** and **b**. where $c =\left\langle c_{1}, c_{2}, c_{3}\right\rangle$, then $a\cdot c = 0$ and $b\cdot c = 0$

and so 

$$
\tag{2} b_{1}c_{1} + b_{2}c_{2} + b_{3}c_{3} = 0
$$ 

To eliminate $c_{3}$, multiply *(1)* by $b_{3}$ and *(2)* by $a_{3}$ and subtract:
$$
\tag{3}
\,(a_{1} b_{3} - a_{3} b_{1}\,) c_{1} + 
\,(a_{2} b_{3} - a_{3} b_{2}\,) c_{2} = 0
$$

and so, the solution of  *(3)* is 
$$c_{1} = a_{2} b_{3} - a_{3} b_{2} \quad c_{2} = a_{3} b_{a} - a_{1} b_{3}$$

Substituting these values into *(1)* and *(2)* , we then get
$$c_{3} = a_{1}b_{2} - a_{2}b_{1}$$

This means that a vector perpendicular to both a and b is

$$\left\langle c_{1}, c_{2}, c_{3}\right\rangle = \left\langle a_{2} b_{3} - a_{3} b_{2},\, a_{3} b_{1} - a_{1} b_{3},\, a_{1}b_{2} - a_{2}b_{1}\right\rangle$$

the resulting vector $\langle c_{1}, c_{2}, c_{3} \rangle$  is the cross product of a and b denoted $a \times b$ 

Definition 
### **Cross Product**  

if $a = \langle a_{1}, a_{2}, a_{3} \rangle$ and $b = \langle b_{1}, b_{2}, b_{3} \rangle$
then the cross product of $a$ and $b$ is the vector 

$$a\times b = \langle a_{2}b_{3} - a_{3}b_{2}, a_{3}b_{1} - a_{1}b_{3}, a_{1}b_{2} - a_{2}b_{1}$$

Cross product unlike dot product is a vector

the cross product of vector $a$ and $b$ is orthogonal to both a and b. 
- and two nonzero vectors $a$ and $b$ are parallel if and only if the cross product is a zero vector. 


#### **Area Of parallelogram** 
Length of the cross product if equal to the area of the parallelogram 


For $3\times 3$ matrix, the **scalar triple product** of the vectors $a, b, c$ is $a\cdot (b\times c)$ 

$$
a\cdot (b\times c) = 
\begin{bmatrix}
a_{1} & a_{2} & a_{3}\\
b_{1} & b_{2} & b_{3}\\
c_{1} & c_{2} & c_{3}\\
\end{bmatrix}
$$

geometric significance can be seen by considering the parallelepiped determined by the vector $a, b, c$ 

the area of the base of parallelogram is $A = |b\times c|$. If $\theta$ is the angle between$a$ and $b\times c$, then the height $h$ of the parallelepiped if $h = |a| |cos \, \theta|$ 
- using $|cos \, \theta|$ instead of $cos \, \theta$ in the case $\theta > \frac{\pi}{2}$ 
therefore the volume of the parallelepiped is
$$V = Ah = |b\times c| |a| |cos\, \theta| = |a \cdot (b\times c)|$$

hence the **volume** of the parallelepiped determined by the vectors $a, b, c$ is the **magnitude of their scalar triple product** 

- if volume is zero of the parallelepiped determined by $a, b, c$  is $0$ then the vectors line in the same plane
	- volume of parallelepiped is zero, then vectors are co-planar


## **12.5 equations of lines**

**vector equation**
$$r = r_{0} + tV$$
- Each value of $t$ (parameter) 
	- gives position vector $r$ 
		- of a point on $L$ 
- As $t$ varies, the line is traced out by the tip of vector $r$ 


$v = \langle a, b, c \rangle$
$tv = \langle ta, tb, tc \rangle$
$r = \langle x, y, z \rangle$
$r_{0} = \langle x_{0}, y_{0}, z_{0}\rangle$ 

and so the vector equation becomes $\langle x, y, z\rangle = \langle x_{0} + ta, y_{0} + tb, z_{0} + tc \rangle$

- two vectors are equal if and only if corresponding components are equal
	- hence we have three scalar equations
$$
\begin{align}
x &= x_{0} + ta\\
y &= y_{0} + tb\\
z &= z_{0} + tc
\end{align}
$$

these three equation are **parametric equations** of the line $L$ through the point $P_{0}\,(x_{0}, y_{0}, z_{0})$
- and **parallel** to the direction vector $v = \langle a, b, c\rangle$ 
	- each value of the parameter $t$ gives a point $(x, y, z)$ on $L$.

## **Example 1 :** 

(a) Find a vector equation and parametric equations for the line that passes through the point $(5, 1, 3)$ and parallel to the vector$i +4j-2k$.
- Lets set up the vector equation  $r = r_o + tV$  
	- $r_0 = \langle 5, 1, 3 \rangle = 5i + j +3k$  
	- $V = i + 4j -2k$ 
		- And so, vector equation $r$ becomes, 
			- $r = (5i + j + 3k) + t(i + 4j -2k)$ 
			- or $r = (5+t)i + (1+4t)j + (3-2t)k$

- and the parametric equations are 
$$
\begin{aligned}
x & = x_0 + at\\
y & = y_0 + bt\\
z & = z_0 + ct
\end{aligned}
$$
where $x_0, y_0, z_0$ is of point and $a, b, c$ is of normal vector 


line segment from $r_{0}$ to $r_{1}$ 
- $r(t) = (1-t)r_{0} + tr-{1} \quad 0\leq t \leq 1$

**Skew lines** 
- do not intersect and are not parallel, (therefore do not lie in the same plane)

A plane in space is determined by a point $P_{0}(x_{0}, y_{0}, z_{0})$ in the plane and a vector $n$ that is orthogonal to that plane. 
- $n$ is the **normal vector**
	- let point $P(x, y, z)$ be an arbitrary point in the plane,
	- let $r_{0}$ and $r$  be the position vectors of $P_{0}$  and $P$ 
		- then the vector $r-r_{0}$ is represented by $\vec{P_{0}P}$
- the normal vector $n$ is orthogonal to every vector in the given plane, in particular, $n$ is orthogonal to $r-r_{0}$ 
giving us **vector equation of the plane**
$$n\cdot (r-r_{0}) = 0$$
rewritten as 
$$n\cdot r = n\cdot r_{0}$$

to obtain a scalar equation for the plane, 
- we write $n=\langle a, b, c \rangle$ 
- $r = \langle x, y, z \rangle$ and 
- $r_{0} = \langle x_{0}, y_{0}, z_{0}\rangle$ 
	- then vector equation of plane becomes
$$\langle a, b, c \rangle \cdot \langle x-x_{0}, y-y_{0}, z-z_{0} \rangle = 0$$
or 
**Scalar equation of the plane through point** $P_{0} (x_{0}, y_{0}, z_{0})$ **with normal vector $n = \langle a, b,c \rangle$ is**
$$a(x-x_{0})+b(y-y_{0})+c(z-z_{0}) = 0$$

## **Example 4 :**

Find an equation of the plane 
through the point $(2, 4, -1)$ 
with normal vector $n = \langle 2, 3, 4 \rangle$ 

*Solution :*  $$\begin{aligned}&a = 2, b = 3, \text{ and }, c = 4\\
& x_0 = 2, y_0 = 4, \text{ and }, z_0 = -1
\end{aligned}$$
so, putting it in the equation of the vector $$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$ 
we get 
$$
\begin{aligned}
2(x - 2) + 3(y-4) + 4(z + 1) &= 0\\
(2x - 4) + (3y - 12) + (4z + 4) &= 0\\
(1x + 3y +4z)+(-4 + -12 +4) &= 0\\
2x + 3y + 4z &= -(-12)\\
2x + 3y + 4z &= 12
\end{aligned}
$$

so the equation of the plan is rewritten as 
$$ax + by +cz + d = 0$$
- (known as linear equation in $x, y, z$)

Two planes are **parallel** if their normal vectors are **parallel**

Distance $D$ from point $P_{1}(x_{1}, y_{1}, z_{1})$ to the plane $ax+by+cz+d=0$
- is equal to the absolute value of the scalar projection of b onto the normal vector $n = \langle a, b, c\rangle$ 
	- $D = |\text{comp}_{n}b| = \frac{|n\cdot b|}{|n|}$ 
	- $D = \frac{|ax_{1} + by_{1}+cz_{1}+d|}{\sqrt{a^{2}+b^{2}+c^{2}}}$ 


## **Example 5:** 

Find an equation of the plane 
that passes through 
the points 
- $P(1, 3, 2)$
- $Q(3, -1, 6)$
- $R(5, 2, 0)$

Solution : 

Given *three* points ($P$ and $Q$ and $R$)
find *two* vectors ($a = \vec{PQ}\quad b = \vec{PR}$)
- $a$ and $b$ are thus vectors in the plane
Then find the normal vector $n$, (orthogonal to $a$ and $b$) 
- through the cross product of vectors $a$ and $b$
	- $n = a \times b$
$$
n = a \times b =
\begin{bmatrix}
i & j & k\\
2 & -4 & 4\\
4 & -1 & -2
\end{bmatrix}
= 12i + 20j + 14k
$$
Like, example 4, 
- we now have 
	- the normal vector $n =\langle 12, 20, 14\rangle$  
		- and a Point $P(1, 3, 2)$ 
Lets find the equation of the plane 
$$a(x-x_0) + b(y-y_0) + c(z-z_0) = 0$$
which is, 
$$12(x-1)+20(y-3)+14(z-2) = 0$$
or $$6x + 10y + 7z = 50$$










