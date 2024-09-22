# Proof for Complex Numbers and Binomial Coefficients

## 1. Complex Numbers

### (a) Modulus and Argument

For a complex number $z = a + bi$, the modulus is given by:
$$ |z| = \sqrt{a^2 + b^2} $$
and the argument  is given by:
$$ \text{arg}(z) = \tan^{-1}\left(\frac{b}{a}\right)$$
Principal value of the argument: Denoted by $\mathrm{Arg}(z)$ 
	is the unique value of the argumant in the interval $(-\pi, \pi]$  

***
The argument formula $\text{arg}(z) = \tan^{-1} \left( \cfrac{b}{a} \right)$ is valid when $a$ is not zero. 
It would be helpful to clarify that when $a = 0$, the argument is $\cfrac{\pi}{2}$ or $\cfrac{3\pi}{2}$ depending on the sign of $b$
***
#### i. For $z = \frac{i}{2}$

Given $z = \frac{i}{2}$, where $a = 0$ and $b = \frac{1}{2}$:

Using the formula for **modulus**:
$$ |z| = \sqrt{0^2 + \left(\frac{1}{2}\right)^2} = \frac{1}{2} $$

For the argument, since the denominator(real part) is zero, the angle lies on the positive y-axis(imaginary part is positive),

the **argument set** is $\cfrac{\pi}{2}+2\pi k$,

and the **principal value of the argument** is:
$$ \text{arg}(z) = \frac{\pi}{2} $$
***
#### ii. For $z = 2 - i$

Given $z = 2 - i$, where $a = 2$ and $b = -1$:

Using the formula for **modulus**:
$$ |z| = \sqrt{2^2 + (-1)^2} = \sqrt{5} $$

The **argument** is given by:
$$\arg(2-i)=-\arctan\left( \frac{1}{2} \right)$$
This value is negative as the complex number is in the fourth quadrant. The **argument set** is 
$$\arg(2-i)=-\arctan\left( \frac{1}{2} \right)+2\pi k$$
    and the **principal value of the argument** is $-\arctan\left( \frac{1}{2} \right)$


***
The argument is in the third quadrant, use method such as $\text{arg }(z) = \pi + \tan ^{-1}\left( \cfrac{b}{a} \right)$ when both $a$ and $b$ are negative
***
#### iii. For $z = -1 - i$

Given $z = -1 - i$, where $a = -1$ and $b = -1$:

Using the formula for **modulus**:
$$ |z| = \sqrt{(-1)^{2} + (-1)^{2} } = \sqrt{2} $$
The **argument** is given by:
$$\arg (-1-i) = \arctan\left( \frac{-1}{-1} \right)+\pi = -\cfrac{5\pi}{4}$$
	This value is in the third quadrant, we add $\pi$ to the arctangent value

The **argument set** is $\arg(-1-i) = -\cfrac{5\pi}{4}+2\pi k$
	and the **principal value of the argument** is 
	$$-\cfrac{5\pi}{4}$$

### (b) Power of Complex Number

Using De Moivre's theorem, for $z = 1 + i$, the power can be found by expressing $1+i$ in its polar form and then raising it to the power of 42:
$$ (1+i)^{42} = 2097152i $$

### (c) Alternating Sums of Binomial Coefficients

The binomial coefficient is given by:
$$ \binom{n}{k} = \frac{n!}{k!(n-k)!} $$

### (i) Even Indices

The alternating sum for even indices can be derived using the binomial expansion of $(1-1)^{42}$:
$$ \sum_{k=0}^{21} (-1)^k \binom{42}{2k} = 0 $$

### (ii) Odd Indices

The alternating sum for odd indices can be derived using the binomial expansion of $(1+i)(1-i)$ raised to the power of 21-k:

$\sum_{k=0}^{20} (-1)^{k} \binom{42}{2k+1}= 2097152$

Thus, 
Simplify $1-i^{2}= 1+1 = 2$ since $i^{2}= -1$
$$ \sum_{k=0}^{20} (-1)^{k} \binom{42}{2k+1}\cdot2^{21-k}= 972551540 $$

## 2. Squares

### (a) Possible squares with vertices at $1+3i$ and $3-i$


Given two points $A(1+3i)$ and $B(3-i)$:

1. For the square with $A$ and $B$ as opposite vertices, the other two vertices can be found using the midpoint formula and the properties of squares.

Find midpoint of $A$ and $B$

To find the other two verticies of the square, we can find the midpoint of $A$ and $B$ and then find the points equidistant from this midpoint, perpendicular to the line $AB$

- Mid point $M$ of $A$ and $B$ :
$$
\begin{align}
M &= \cfrac{A+B}{2}  \\
&= \cfrac{(1+3i)+(3-i)}{2} \\
&= \cfrac{(4+2i)}{2}\\
&= 2 + i \\
\end{align}
$$
Now to find the two other vertices $C$ and $D$ of the square with $A$ & $B$ as opposite vertices. 

The line segment $AB$ has a slope, which is the imaginary part divided by the real part of $B-A$:
$$
\begin{align}
\text{Slope of } AB &= \cfrac{\mathrm{\mathrm{Im}(B-A)}}{\mathrm{Re}(B-A)} \\
&= \cfrac{\mathrm{\mathrm{Im}(3-i-(1+3i))}}{\mathrm{Re}(3-i-(1+3i))} \\
&= \cfrac{\mathrm{\mathrm{Im}(2-4i)}}{\mathrm{Re}(2-4i)} \\
&= -2
\end{align}
$$
The perpendicular slope to $AB$ will be the negative reciprocal of the slope of $AB$:
$$\text{Perpendicular Slope } = \cfrac{1}{2}$$
To find the other two vertices, $C$ and $D$ we can use the midpoint $M(2+i)$ and move along the line with a perpendicular slope to $AB$ by a distance equal to half the length of the diagonal $AB$.

The length of the diagonal $AB$ is the distance between $A$ and $B:
$$
\begin{align}
\left|\, AB \,\right| &= \left|\, B - A \,\right| \\
&= 2\sqrt{ 5 }
\end{align}
$$

Now, to find the other verticies, $C$ and $D$, we can use the midpoint and move along the line with a perpendicular slope to $AB$ by a distance equal to half the length of the diagonal $AB$:
$$
\begin{align}
\text{Distance to move} &= \cfrac{\left|\, AB \,\right| }{2} \\
&= \sqrt{ 5 }
\end{align}
$$

Denote movement along the real axis as $\Delta x$ and the movement along the imaginary axis as $\Delta y$. Since we are moving along a line with a slope of $\cfrac{1}{2}$, we have:
$$
\begin{align}
\cfrac{\Delta y}{\Delta x} &= \cfrac{1}{2}\\
\Delta y &= \cfrac{\Delta x}{2}
\end{align}
$$
Also, the distance to move, $\sqrt{ 5 }$, is related to $\Delta x$ and $\Delta y$ by the Pythagorean theorem:
$$
\begin{align}
\sqrt{ 5 }  & = \sqrt{ \left( \Delta x \right)^{2} + \left( \cfrac{\Delta x}{2} \right)^{2} } \\
5 & = \Delta x^{2}+\cfrac{\Delta x^{2}}{4} \\
5  & = \cfrac{5\Delta x^{2}}{4} \\
\Delta x^{2} & = 4 \\
\Delta x & = 2 
\end{align}
$$
Substituting back to find $\Delta y$:
$\Delta y = \cfrac{2}{2} = 1$

Now, we can find the coordinates of $C$ and $D$:
$$
\begin{align}
C  & = M + \Delta x+i\Delta y \\
 & = (2+i)+2+i \\
 & =4+2i
\end{align}
$$
$$
\begin{align}
D  & = M - \Delta x-i \Delta y \\
& = (2+i) - (2+i) \\
& = 0
\end{align}
$$






3. For the square with $A$ and $B$ as adjacent vertices, the other two vertices can be found using vector addition and the properties of squares.
	Lets use the following relations:
$$
\begin{align}
C'  & = A + (B - A) \cdot (1 + i) \\
D'  & = B + (A - B) \cdot (1 + i)
\end{align}
$$

Lets calculate:
$$
\begin{align}
C'  & = (1+3i) + ((3-i)-(1+3i) \cdot (1+i) \\
 & = 2i-(1+3i)(1+i)+4 \\
 & = 2i+2-4+4 \\
 & = 6-2i
\end{align}
$$

$$
\begin{align}
D'  & = (3-i) + ((1+3i)-(3-i)) \cdot (1+i)\\
& = (3-i)+(-2+4i)(1+i)\\
&= 3 - i + 2i - 6 \\
&= -3+i
\end{align}
$$


### (b) Squares on the exterior of a convex quadrilateral $ABCD$

Given a convex quadrilateral $ABCD$, if we construct squares on the exterior of its sides with centers $P, Q, R, S$, then the midpoints $I, J, K, L$ of the sides of $PQRS$ will form a square. 

**Proof:** 

1. Let $I$ be the midpoint of $PQ$, $J$ be the midpoint of $QR$, $K$ be the midpoint of $RS$, and $L$ be the midpoint of $SP$. 
2. Since $P, Q, R, S$ are the centers of the squares constructed on the sides of $ABCD$, the segments $PQ, QR, RS, SP$ are diagonals of these squares and are therefore equal in length. 
3. The midpoints of equal segments divide the segments into equal halves. Thus, $PI = IQ$, $QJ = JR$, $RK = KS$, and $SL = LP$. 
4. Since all four segments $PI, QJ, RK, SL$ are equal, the quadrilateral $IJKL$ is a rhombus. 
5. Additionally, since $PQRS$ is a square (because all its sides are equal and all its angles are right angles), the angles $P, Q, R, S$ are all $90^\circ$. 
6. The diagonals of a square are perpendicular bisectors of each other. Therefore, the angles $IPQ, JQR, KRS, LSP$ are all $90^\circ$. 
7. Given that $IJKL$ is a rhombus with all angles equal to $90^\circ$, $IJKL$ is a square.

Uses the properties of squares and midpoints to show that the midpoints of the sides of a square formed on the exterior of a convex quadrilateral will also form a square.

## 3. Geometric Transformations

### (a) Composition of transformations

Given the transformations: 
1. Translation by $i$ 
2. Inversion 
3. Counter-clockwise rotation by $\pi/3$ with center at 0 
4. Translation by $1+i$ 

Lets denote a general complex number as $z = a + bi$ where $a, b \in\mathbb{R}$ 

1. Translation by $i$
$$
\begin{align}
z' & = z + i \\
 & = a + (b+1)i
\end{align}
$$

2. Inversion:
$$
\begin{align}
z'' & = \cfrac{1}{z'} \\
 &  = \cfrac{1}{a+(b+1)i}
\end{align}
$$
3. Counter-clockwise rotation by $\frac{\pi}{3}$ with a center at $0$:
$$
\begin{align}
z''' & = e^{i \,\cfrac{\pi}{3}} \cdot z'' \\ \\
 \\
 & = \cfrac{e^{i\cfrac{\pi}{3}}}{a+(b+1)i}
\end{align}
$$

4. Translation by $1+i$:
$$
\begin{align}
f(z) &= z''' + (1+i)  \\
\\
& = \cfrac{e^{i\cfrac{\pi}{3}}}{a+(b+1)i}+(1+i)
\end{align}
$$
Final composition:
$$
f(z)=(1+i)+\cfrac{e^{i\cfrac{\pi}{3}}}{a+(b+1)i}
$$

This is the function $f(z)$ after applying all the transformations in the given order.

The composition of transformations is given by applying each transformation in sequence to a general complex number $z$.

### (b) Express $f(z) = \frac{z+i}{iz+1}$ as a composition

Given the function $f(z) = \frac{z+i}{iz+1}$, we can express it as a composition of geometric transformations. 

**Decomposition:**

1. **Translation by $i$:** $z \rightarrow z + i$ 
$$
\begin{align}
f(z) &= \cfrac{z+i+i}{iz+i+1} \\
 & = \cfrac{z+2i}{iz+1+i}
\end{align}
$$
2. **Inversion:** $z \rightarrow \frac{1}{z}$
$$
f(z) = \cfrac{iz+i+1}{z+2i}
$$
1. **Rotation by $\pi/2$ (90 degrees counter-clockwise):** $z \rightarrow iz$
$$
f(z) = \cfrac{i^2z+i^2+i}{z+2i}
$$
1. **Translation by 1:** $z \rightarrow z + 1$ 
$$
\begin{align}
f(z) & = \cfrac{1+i^2z+i^2+i}{1+z+2i} \\
& = \cfrac{i^2z+i^2+i+1}{z+2i+1} \\
 & = \cfrac{iz}{z+i}
\end{align}
$$

Applying these transformations in sequence, we get: $$ f(z) = \frac{iz}{z+i} $$
the function can be expressed as a sequence of geometric transformations.

## 4. Inversion Transformation $z \rightarrow f(z) = z^{-1}$

### (a) Points on a circle not passing through 0

Given distinct points $z_1, z_2, z_3, z_4$ on a circle not passing through 0, we need to show that there exists a circle passing through $f(z_1), f(z_2), f(z_3), f(z_4)$ where $f(z) = z^{-1}$. 

**Proof:** 

Consider the inversion transformation $f(z) = z^{-1}$. The property of inversion is that it maps circles and lines not passing through the origin to other circles and lines. 

Let's consider a circle $C$ with center $O$ and radius $r$, not passing through the origin. 
	The equation of a circle in the complex plane not passing through the origin is given by: $|z - O| = r$
Let's assume $z_1, z_2, z_3, z_4$ are distinct points on this circle.

To find the inverse of the points on the circle, we use the transformation $f(z) = z^{-1}$. Thus, the inverses of the points $z_1, z_2, z_3, z_4$ are:
$f(z_1) = z_1^{-1}$
$f(z_2) = z_2^{-1}$
$f(z_3) = z_3^{-1}$
$f(z_4) = z_4^{-1}$

Since the original points are on a circle not passing through the origin, their inverses will also lie on a circle, proving the existence of a circle passing through $f(z_1), f(z_2), f(z_3), f(z_4)$.

The inversion transformation maps circles and lines not passing through the origin to other circles and lines. Thus, points on a circle not passing through the origin will map to another circle.

### (b) Points on a circle passing through 0

Given distinct points $$z_1, z_2, z_3$$ on a circle passing through 0, we need to show that there exists a straight line passing through $$f(z_1), f(z_2), f(z_3)$$ where $$f(z) = z^{-1}$$
**Proof:**


Given the inversion transformation $f(z) = z^{-1}$, it maps circles passing through the origin to straight lines not passing through the origin. Their inverses $f(z_1), f(z_2), f(z_3), f(z_4)$ will also lie on a circle (or possibly a line if the original circle passed through the origin). 

Proof: 
Let's consider a circle $C'$ passing through the origin. Let's assume $z_1, z_2, z_3$ are distinct points on this circle.

Since the circle passes through the origin, the inverses of the points $z_1, z_2, z_3$ will be:
$f(z_1) = z_1^{-1}$
$f(z_2) = z_2^{-1}$
$f(z_3) = z_3^{-1}$

These inverses will lie on a straight line, proving the existence of a straight line passing through $f(z_1), f(z_2), f(z_3)$.

The inversion transformation maps circles passing through the origin to straight lines not passing through the origin, and vice versa. Thus, points on a circle passing through the origin will map to a straight line.

### (c) Points on a straight line not passing through 0

Given distinct points $$z_1, z_2, z_3$$ on a straight line not passing through 0, we need to show that there exists a circle passing through $$0, f(z_1), f(z_2), f(z_3)$$ where $$f(z) = z^{-1}$$. 
**Proof:** 

Given the inversion transformation $f(z) = z^{-1}$, it maps straight lines not passing through the origin to circles passing through the origin.

Let's consider a straight line $L$ not passing through the origin. Let's assume $z_1, z_2, z_3$ are distinct points on this line.

The equation of a straight line in the complex plane can be represented as:
$z_3 = z_1 + t(z_2 - z_1)$

To find the inverses of the points on the line, we use the transformation $f(z) = z^{-1}$. Thus, the inverses of the points $z_1, z_2, z_3$ are:
$f(z_1) = z_1^{-1}$
$f(z_2) = z_2^{-1}$
$f(z_3) = z_3^{-1}$

Since the original points are on a straight line not passing through the origin, their inverses will lie on a circle passing through the origin, proving the existence of a circle passing through $0, f(z_1), f(z_2), f(z_3)$.
