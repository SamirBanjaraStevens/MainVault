We found equation. of the tangent plane to the graph of the function $f(x, y) = 2x^{2}=y^{2}$ at the point$(1, 1, 3)$ is $z = 4x +2y - 3$ 

Therefore, the linear function of the two variables, $L(x, y) = 4x + 2y -3$ is a good approximation to $f(x, y)$ when $(x, y)$ is near $(1, 1)$ 

The function $L$ is called the **Linearization** of $f$ at $(1, 1)$  and the approximation $$f(x, y) \approx 4x +2y -3$$ is called the **linear approximation** or **Tangent plane approximation** of $f$ at $(1, 1)$ 

for instance, at point $(1.1, 0,95)$ the linear approximation gives us,
$$f(1.1, 0.95) \approx 4(1.1) + 2(0.95) - 3 = 3.3$$
which is close to the true value of $f(1.1, 0.95) = 2(1.1)^{2}+ (0.95)^{2} = 3.3225$

*Note :* Did we just solve the system with the psuedoinverse?

We know that an equation of the tangent plane tot he graph of a function $f$ of two variables at the point $(a, b, f(a, b))$ is
$$z = f(a, b) + f_{x}(a, b)(x-a)+f_{y}(a,b)(y-b)$$
The linear function whose graph is this tangent plane, (tangent plane)
$$L(x, y) = f(a, b) + f_{x}(a, b)(x-a)+f_{y}(a,b)(y-b)$$
is called the **linearization** of $f$ at $(a, b)$ and the approximation 
$$f(x,y) = f(a,b) +f_{x}(a,b)(x-a)+f_{y}(a,b)(y-b)$$
is the **Linear approximation** or tangent plane approximation of $f$ at $(a,b)$ 

**What if $f_{x}$ and $f_{y}$ are not continuous?**

its equation would be 
$$
f(x, y) = 
\begin{cases}
\cfrac{xy}{x^{2}+y^{2}} \quad\quad &\text{if } (x, y)\neq (0,0) \\
0 \quad\quad &\text{if } (x,y) = (0, 0)
\end{cases}
$$
its partial derivative exists at the origin end 
$$f_{x}(0,0) = 0$$
$$f_{y}(0, 0) = 0$$
**BUT** 
$f_{x}, f_{y}$ are not continuous

The linear approximation would be $f(x, y) \approx 0$ but $f(x, y) = \cfrac{1}{2}$ at all points on the line $y = x$

So a function of two variables can behave badly even though both of its partial derivative exist.

For a function of one variable $y = f(x)$ 
if, $x$ changes from $a$ to $a + \Delta x$, <u>we can define the increment</u> of $y$ as $$\Delta y = f(a + \Delta x) - f(a)$$ if $f$ is differentiable at $a$ then 
$$\Delta y = f'(a) \Delta x + \epsilon \Delta x \quad \text{ where } \epsilon \rightarrow 0 \text{ as } \Delta x \rightarrow 0$$
now consider a function of two variables, $z = f(x, y)$, and suppose $x$ changes from $a$ to $a + \Delta x$ and $y$ changes from $b$ to $b+\Delta y$

then, the correct increment of $z$ is 
$$\Delta z = f(a+\Delta x, b +\Delta y) - f(a, b)$$
thus the increment $\Delta z$ represents the <u>change in the value of</u> $f$ <u>when</u> $(x,y)$ <u>changes from</u> $(a, b)$ to $(a+\Delta x, b+\Delta y)$ 

**THUS,**

If
$$
z = f(x, y)
$$
then $f$ is **differentiable at $(a, b)$** is $\Delta z$ can be expressed in the form 
$$\Delta z=f_{x}(a,b)\Delta x+f_{y}(a, b)\Delta y+ \epsilon_{1} \Delta x+\epsilon_{2}\Delta y$$
where $\epsilon_{1}$ and $\epsilon_{2} \rightarrow 0$ as $(\Delta x, \Delta y) \rightarrow (0,0)$

***
A differentiable function is one for which the linear approximation 
$$f(x,y) = f(a,b) +f_{x}(a,b)(x-a)+f_{y}(a,b)(y-b)$$

is a good approximation when $(x, y)$ is near $(a, b)$ 
	in other words
		The tangent plane approximates the graph of $f$ well near the point of tangency

***
Convent and sufficient condition for differentiability

```ad-note
title: Theorem
If the partial derivatives $f_{x}$ and $f_y$ exist near $(a, b)$ 
And, are continious at $(a, b)$ 
Then, $f$ is differentiable at $(a, b)$
```

### Example 2
***
Show that $f(x, y) = xe^{xy}$ is differentiable at $(1, 0)$ and find its linearization.

Then use the linearization to approximate $f(1.1, -0.1)$ 

#### Steps
***
First, find the Partial derivatives
```ad-example
Title: Partial derivatives of $f(x,y)$

$$
\begin{aligned}
f_{x}(x,y)&= e^{xy}+x e^{x}y\\
f_{x}(1,0) &= e^{0} + 1 * e^{1}* 0 &= 1\\
f_{y}(x,y) &= x^{2} * e^{xy}\\
f_{y}(1,0) &= 1^{2} * e^{0} &= 1
\end{aligned}
$$
```

Thus, both $f_{x} \text{ and } f_{y}$ are continuous, so $f$ is differentiable at $(1, 0)$ 

Then find the linearization,
$L(x, y) = f(a, b) + f_{x}(a, b)(x-a)+f_{y}(a,b)(y-b)$
```ad-example
title: Linerization
$$
\begin{aligned}
L(x, y) &= f(1, 0) + f_x(1,0)(x-1) + f_{y}(1, 0)(y - 0)\\
&= 1 + 1(x-1) + 1(y)\\
&= 1 + 1x - 1 + 1y\\
&= 1x + 1y
\end{aligned}
$$
```

The corresponding linear approximation is 
$$x \ e^{xy}\approx x + y$$
so, 
$$f(1.1, -0.1) \approx 1.1 - 0.1 = 1$$
compare this to the actual result
$$f(1.1, -0.1) = (1.1) \cdot e^{(1.1)(-0.1)} =1.1e^{-0.11} \approx 0.98542$$

