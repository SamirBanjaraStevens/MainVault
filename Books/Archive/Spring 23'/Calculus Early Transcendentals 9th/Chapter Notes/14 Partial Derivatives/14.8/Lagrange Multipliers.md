#### Summary
***
The method of **Larange Multipliers** 
	is utlized to determine the *local* [*[Maxima and minima]]* 
		of a *[[Function]]*
			subject to *[[Equality constraints]]* 
					(i.e., subject to the condition that one or more *[[Equations]]* have to be satisfied by exactly by the chosen values of the *[[Variables]]*)
The Idea is to convert a constrained problem
	into a form such
		that *[[Derivative test]]* 
			of an unconstrained problem
				can still be applied.
The relationship between
	the gradient of the fucntion
		and gradients of the constraisnts 
			rather naturally 
				lead to a reformulation
					of the original problem
						known as the **Lagradian Function**
##### Method can be summarized as follows:
***
In order to find the maximum or minimum 
	of a function $f(x)$
		subjected to the equality constraint $g(x)=0$ 
			form the **Lagrangian function**
				$$\mathcal{L}(x, \lambda) \equiv f(x)+\lambda \cdot g(x)$$
				and find the *[[Stationary points]]* 
					of $\mathcal{L}$ considered 
						as a function of $x$ 
				and the Lagrange multiplier $\lambda$ 
This means that all *[[Partial Derivatives]]*
	should be zero,
		includind the partial derivative with respect to $\lambda$
			$$\cfrac{\partial \mathcal{L}}{\partial x}=0, \quad\cfrac{\partial \mathcal{L}}{\partial \lambda}=0$$
			or equivalentely
$$\cfrac{\partial f(x)}{\partial x}+\lambda \cdot\cfrac{\partial g(x)}{\partial x}=0, \quad \text{ and } g(x)=0$$

***

The solution corresponding
	to the original constrained optimazation 
		is always a *[[Saddle point]]*
			of the Lagrangian function,
	which can be identfied 
		among the stationary points 
			from the *[[Definiteness]]* 
				of the *[[bordered Hessian matrix]]*

The great advantage of this method 
	is that it allows the optimazation 
		to be solved 
			without explicit *[[Parameterization]]* 
				in terms of the constraints.
As a result 
	the method of Lagrange multipliers
		is widely used to solve 
			challennging constrained optimazation problems.
Further, the method of Lagrange multipliers
	is generalized by the 
		*[[Karush-Kuhn-Tucker conditions]]* 
			which can also 
				take into account inequality constrinst of the form
					$$h(x)\leq c$$
						for a given constant $c$

## Lagrange multiplier theorem

Let $f:\mathbb{R}^{n}\rightarrow \mathbb{R}$ 
	be the objective function,
and let $g:\mathbb{R}^{n}\rightarrow\mathbb{R}^{c}$ 
	be the constraints function
both belonging to $C^{1}$
	that is having continious first derivatives

Let $x_{*}$ be an optimal solution 
	to the following optimization problem
		such that $\text{rank}(D \ g(x_{*}))=c<n$ 
			here $D \ g(x_{*})$ denotes the matrix of partial derivatives, 
				$$\left[ D \ g(x_{*}) \right]_{j,k} = \left[ \cfrac{\partial g_{j}}{\partial x_{k}} \right] $$
				$$\begin{array}{} \text{maximize } f(x)\\\text{subject to: }g(x)=0\end{array}$$
Then there exists a unique Lagrange multiplier 
$$\lambda_{*}\in\mathbb{R} \text{ such that } Df(x_{*})=\lambda_{*}^{T}Dg(x_{*})$$

The Lagrange multiplier theorem states that at any local maximum (or minimum) of the function evaluated under the equality constraints, if constraint qualification applies, then the *[[Gradient|gradient]]* of the function (at that point) can be expressd as a linear combination of the gradients of the constraints (at that point), with the Lagrange multipliers acting as *[[Coefficients|coefficients]]*. This is equivalent to saying that any direction perpendicular to all gradients of the constraints is also perpendicular to the gradient of the function. Or still, saying that the *[[Directional Derivatives]]* of the function is $0$ in ever feasible direction.

The method of Lagrange multipliers relies on the intution that at a maximum, $f(x, y)$ cannot be increasing in the direction of any such neighboring point that also has $g=0$. If it were, we could walk along $g=0$ to get higher, meaning that the starting point wasn't actually the maximum. Viewed in this way, it is an exact analogue to testing if the derivative of an unconstrained function is $0$, that is, we are verifying that the directional derivative is $0$ in any relevant (viable) direction. 


in *example 14.7.6* 
	we maximized a volume function $V =xyz$ 
		subject to the constraint $2xz+2yz+xy=12$ 
			which expressed the side condition 
				that the surface area was $12 \text{ m}^{2}$ 

Here we will present **Larange's method** 
	for maximizing or minimizing 
		a genereal function $f(x,y,z)$ 
			subject to a constraint 
				of the form $g(x, y, z)=k$

Let's first find the extreme values of $f(x,y)$ 
	subject to a constraint $g(x,y)=k$ 
In orther words, 
	we see the extreme values of $f(x, y)$ 
		when the point $(x, y)$ 
			is restricted to lie on the level curve $g(x,y)=k$

To maximize $f(x,y)$ 
	subject to $g(x,y)=k$
		is to find the largest value of $c$ of $f(x,y)=c$ 
			such that the level curve $f(x,y)=c$
				intersects $g(x,y)=k$
This occurs when 
	they have a common tangent line. 
This means that the normal lines
	at the point $(x_{0}, y_{0})$ 
		where they touch are identical
So the gradients vectors are parallel
	that is,
		$\nabla f(x_{0},y_{0})=\lambda \nabla g(x_{0},y_{0})$
				for some scalar $lambda$

Suppose that a function $f$ 
	has an extreme value at a point $P(x_{0}, y_{0}, z_{0})$
		on the surface $S$
			and let $C$ be a curve
				with the vector equation $r(t)\left< x(t), y(t), z(t) \right>$ 
					that lies on $S$
						and passes through $P$
If $t_{0}$ is the parameter value
	corresponding to the point $P$
		then $r(t_{0})=\left< x_{0}, y_{0}, z_{0} \right>$
The composite function $h(t)=f(x(t), y(t), z(t))$
	represents the values 
		that $f$ takes on the curve $C$
Since, $f$ has an extreme value at $(x_{0}, y_{0}, z_{0})$ 
	it follows 
		that $h$ has 
			an extreme value 
				at $t_{0}$
	so, $h'(t_{0})=0$
But if $f$ is differentiable, 
	we can use the chain rules to write 
$$
\begin{align}
0&=h'(t_{0})\\
&= f_{x}(x_{0}, y_{0}, z_{0})x'(t_{0})+f_{y}(x_{0}, y_{0}, z_{0})y'(t_{0})+f_{z}(x_{0}, y_{0}, z_{0})z'(t_{0})\\
&=\nabla f(x_{0},y_{0},z_{0})\cdot r'(t_{0})
\end{align}
$$

This shows that 
	the gradient vector $\nabla f(x_{0},y_{0},z_{0})$ 
		is orthogonal 
			to the tangent vector $r'(t_{0})$
				to every such curve $C$
But we know that 
	the gradient vector of $g$
		$\nabla g(x_{0},y_{0},z_{0})$ 
			is also orthogonal to $r'(t_{0})$
				for every such curve.
This means that the gradient vector $\nabla f(x_{0},y_{0},z_{0})$ and $\nabla g(x_{0},y_{0},z_{0})$ 
	must be parallel.
Therefore, 
	if $\nabla g(x_{0},y_{0},z_{0})\neq 0$ 
		then there is a number $\lambda$ 
			such that 
$$
\nabla f(x_{0},y_{0},z_{0})=\lambda \nabla g(x_{0},y_{0},z_{0})
$$

the *[[Scalars|scalar]]* $\lambda$ is the **Larange Multiplier**

***
## Method of Larange Multipliers

To find the maximum 
	and minimum values
		 of $f(x, y, z)$
	subject to the 
		constraint $g(x, y, z)=k$
{**Assuming that these extreme values exist and $\nabla g\neq 0$ on the surface $g(x, y, z)=k$**}

**(A)** Find all the values of $x, y, z$ and $\lambda$ 
		such that 
			$$\begin{align}
\nabla f(x,y,z)&=\lambda \nabla g(x, y, z)\\
g(x, y, z)&=k\\
\end{align}$$
**(B)** Evaluate $f$ at all the points $(x, y, z)$ 
		that result from **(A)** 
	The largest of these values is the maximum
		and the smallest is the minimum values of $f$ 
***


## Example 1



