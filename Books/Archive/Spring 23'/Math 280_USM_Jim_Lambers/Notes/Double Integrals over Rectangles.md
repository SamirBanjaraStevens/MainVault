We define the integral of a function $f(x)$ over an inverval $[a, b]$
$$\int _{a}^{b}f(x) \, d = \lim_{ n \to \infty } \sum _{i=1}^{n}f(x_{i}^{*})\Delta x $$
limit as $n$ approaches infinity of the sum from $1$ to $n$ of the area of rectangles
$$\Delta x = \frac{(b-a)}{x} \quad \forall \, i , x_{i-1}\leq x_{i}^{*}\leq x_{i} \quad , x_{i} = a+ i\Delta x$$ 
The purpose of the definite integral is to compute the area of region with curved boundy, 
using the formula of a rectangle. 

The summatation used to define the integral is the sum of the area of $n$ rectangles, 
	each with width $\Delta x$ and height $f(x_{i}^{*})$, for $i=1, 2, \dots , n$ 

By taking the limit as $n$ the number of rectangles, temds to infinity, we obtains the sum of the area of the infinitely many rectangles of infinitely small width.

We define the area of the region bounded by the line $x=a, y=0, x=b, y=f(x)$ to be this limit, if it exists.


However, we we used $F(x) = \int _{a}^{x} f(s) \ ds$ 

then $$F'(x) = \lim_{ n \to 0 } \cfrac{1}{h} \left[\int _{a}^{x+h} f(s) \ ds - \int _{a}^{x} f(s) \, ds\right] = \cfrac{1}{h} \int _{x}^{x+h} f(s) \ ds$$

Intuitively, as $h\rightarrow 0$
	this expression converges to the area of a rectangle of width $h$ and height $f(x)$, 
		divided by the width, 
			withc is simply the height $f(x)$
				that is, $F'(x) = f(x)$

*Fundemental theorem of calcus* 





$$\int _{a}^{b} f(x) \, dx =F(b) - F(a)$$
Where, $F$ is the *antiderivative* of $f$: that is $F' = f$
Therfore definite integrals are evaluated by attempting to undo the diferentation process to find an antiderivative of the *Intergand* $f(x)$ and then evaluating this antiderivative at $a$ and $b$, the limits of the integral. 

Now, let $f(x, y)$ be a function of two variables. 
We consider the problem of computing the **Volume** of the solid in 3-d space
bounded by the surface $z = f(x, y)$ 
and the planes $x = a$, $x = b, y=c, y=d, z =0$ where $a, b, c, d$ are constants.
As before we divide the interval $[a, b]$ into $n$ subintervals of width $\Delta x=(b-a)/n$ 
and we similarly divide the intercal $[c, d]$ into $m$ subintervals of width $\Delta y=(d-c)/m$
For convenience, we also define $x_{i} = a+i\Delta x$ and $y_{y}=c+j\Delta y$ 

Then, we can approximate the volume $V$ of this solid by the sum of $mn$ boxes.
The base of each box is a rectangle with dimensions $\Delta x\text{ and } \Delta y$
and the height is given by $f(x_{i}^{*}, y_{i}^{*})$ where, for each $i$ and $j$ $x_{i-1}\leq x_{i}^{*}\leq x_{i}$ and $y_{j-1}\leq y_{j}^{*}\leq y_{j}$, that is
$$V \approx \sum_{i=-1}^{n}\sum_{j=1}^{m} \ f(x_{i}^{*}, y_{j}^{*})\Delta y\Delta x$$
We then obtain the exact volume of this solid by letting the number of subintervals $n$, tend to infinity.
The result is the double integral of $f(x,y)$ over the rectangle $R=\{ (x, y)\mid a\leq x\leq b, c\leq y\leq d \}$ which is also written as $R = [a, b]\times[c,d]$
The double integral is defined to be,
$$V = \int \int _{R} \, f(x, y)  \, dA = \lim_{ m, n \to \infty } \sum_{i=-1}^{n}\sum_{j=1}^{m} \ f(x_{i}^{*}, y_{j}^{*})\Delta y\Delta x$$

which is equal to the volume of the given solid.

The $dA$ corresponds to the quantity $\Delta A = \Delta x\Delta y$ 
and emphasozes the fact that the integral is defined to be the be th elimit of the sum of volumes of boxes, each with a base of area $\Delta A$
***
To evaluate double integrals of this form, we can proceed as in the single-variable case, by noting that if $f(x_{0}, y)$ a function of $y$ is integrable on $[c, d]$ for each $x_{0}\in [a, b]$ then w e have, 
$$
\begin{align}
\int \int _{R} f(x, y) \,dA &= \lim_{ m, n \to \infty } \sum_{i=-1}^{n}\sum_{j=1}^{m} \ f(x_{i}^{*}, y_{j}^{*})\Delta y\Delta x \\
&=\lim_{ m, n \to \infty } \sum_{i=1}^{n}\left[\lim_{ m \to \infty } \sum_{j=1}^{m} f(x_{i}^{*}, y_{j}^{*})\Delta y \right]\Delta x\\
&= \lim_{ m, n \to \infty } \sum_{i=1}^{n}\left[\int _{c}^{d} f(x_{i}^{*}, y) \, dy \right]\Delta x\\
&= \int _{a}^{b}\int _{c}^{d} f(x,y) \, dy  \, dx 
\end{align}
$$
Similarly if $f(x, y_{0})$ a function of $x$ is integrable on $[a, b]$ for each $y_{0}\in [c, d]$ we also have
$$\int \int _{R} f(x, y) \, dA =\int _{a}^{b}\int _{c}^{d} f(x,y) \, dy  \, dx $$

This is known as **Fubini's Theorem** which states that a double intergal of a function $f(x, y)$ can be evalauated as two *iterated* single integrals, 
	provided that $f$ is integrable as a function of either variable when the other variable is held fixed.
		This is guaranteed if, for instance, f(x, y) is continious on the entire rectanble $R$ 

That is, we can evaluate a double integral by performing *partial integration* with respect to either variable $x$ or $y$ which entails applying the Fundamental Theorem of Calclus to intergrate $f(x, y)$ with respect to *only* that variable, while treating the other varible as a constant. 

The result will be a function of only the other variable, while treating the other vriable as a constant. 

The result will be function of only the other variable, to which the Fundemental Theorem of Calculus can be applied a second time to complete the evaluation of the double integral.

## Example
Let $R = [0,1]\times[0, 2]$, and let $f(x, y) = x^2y+xy^{3}$
Evaluate $\int \int _{R} f(x,y) \, dA$

We have,
$$
\begin{align}
\int \int _{R} f(x,y) \, dA &= \int _{0}^{1}\int _{0}^{2} x^{2}y+xy^{3} \, dx  \, dx\\
&= 
\end{align}
$$





