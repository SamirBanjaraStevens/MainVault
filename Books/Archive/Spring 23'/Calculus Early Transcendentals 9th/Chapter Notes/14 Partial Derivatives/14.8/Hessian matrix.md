The **Hessian matrix** or **Hessian** 
	is a *[[Square matricies|square matrix]]* 
		of second-order *[[Partial Derivatives]]* 
			of scalar-valued *[[Function]]* 
				or a *[[Scalar field]]* 
It describes the local curvature
	of a function of many variables.

## Definitions and properties

Suppose $f:\mathbb{R}^{n}\rightarrow\mathbb{R}$ is a function
	taking as input a vector $x \in\mathbb{R}^{n}$
		and outputting a scalar $f(x)\in\mathbb{R}$ 
If all second-order *[[Partial Derivatives]]* 
	of $f$ exist,
		then the Hessian matrix $H$ of $f$ 
			is a square $n\times n$ matrix,
				defined and aranged as 
$$
H_{f}=
\begin{bmatrix}
\cfrac{\partial^{2}f}{\partial x_{1}^{2}} & \cfrac{\partial^{2}f}{\partial x_{1}\partial x_{2}} & \dots & \cfrac{\partial^{2}f}{\partial x_{1}\partial x_{n}}\\ \\
\cfrac{\partial^{2}f}{\partial x_{2}\partial x_{1}} & \cfrac{\partial^{2}f}{\partial x_{2}^{2}}&\dots&\cfrac{\partial^{2}f}{\partial x_{2}\partial x_{n}}\\ \\
\vdots & \vdots & \ddots & \vdots\\ \\
\cfrac{\partial^{2}f}{\partial x_{n}\partial x_{1}}& \cfrac{\partial^{2}f}{\partial x_{n}\partial x_{2}}& \dots & \cfrac{\partial^{2}f}{\partial x_{n}^{2}}\\ 
\end{bmatrix}
$$


that is, the entry of the $i^{\text{th}}$ row 
	and the $j^{\text{th}}$ column is 
		$$\left( H_{f} \right)_{i,j}=\cfrac{\partial^{2}f}{\partial x_{i}\partial x_{j}}$$
If furthermore the second partial derivatives 
	are all continious, 
		the Hessian matrix is a *[[Symmetric matrix]]* 
			by the *[[Symmetry of second derivatives]]* 
The *[[Determinant]]* of the Hessian matrix 
	is called the *Hessian determinant*

The Hessian matrix of a function $f$
	is the transpose of the *[[Jacobian matrix]]* 
		of the *[[Gradient]]* of the function $f$
			that is, 
				$$H(f(x))=J(\nabla f(x))^{T}$$

## Applications

#### Inflection points
***
if $f$ is a *[[Homogeneous polynomial]]* 
	in three variables, 
		the equation $f=0$ 
			is the *[[Implicit equation]]* 
				of a *[[Palne projective curve]]* 
The *[[Inflection points]]* of the curve
	are exactally the non-singular points
		where the Hessian determinant is zero. 

#### Second-derivative test
***
The Hessian matrix of a *[[Convex function]]* 
	is *[[Positive semi-definite]]*.

Refining this property allows us to test
	whether a *[[Critical point]]* $x$ 
		is a local maximum, 
				local minimum,
				or a *[[Saddle point]]*

If the Hessian is *[[Positive-definite]]* at $x$ 
	then $f$ attains 
		an isolated local minimum at $x$

If the Hessian is *[[Negative-definite]]* at $x$ 
	then $f$ attains 
		an isolated local maximum at $x$

If the Hessian 
	has both positive 
	and negative eigenvalues, 
		then $x$ is a *[[Saddle point]]* 
			for $f$

Otherwise the test is inconclusive. 

This implies that at a local minimum
		the hessian is positive-semidefinite
	and at a local maximum
		the Hessian is negative-semidefinite

For positive-definite and negative-semidefinite Hessian,
	the test is inconclusive
			(a critical point where the Hessian is semidefinite but not definite may be a local extremum or a saddlepoint)
		however, more can be said 
			from the point of view of *[[Morse theory]]*

Equivalently, the second-order conditions
	that are sufficent 
		for a local maximum 
				or minimum
			can be expressed in terms
				of sequence of principal
					(upper-leftmost) *[[minors]]* 
						(determinants of sub-matrices) of the Hessian.
	these conditions are a special case 
		for *[[bordered Hessian matrix]]* 
			for constrained optimization
				the case in which 
					the number of constraints 
						is zero
Specifically, the sufficent condition 
	for a minimum is that all 
		of these principal minors be positive
	while the sufficent condition
		for a maximum is that 
			the minors alternate in sign
				with the $1\times 1$ minior being negative.

## Critical points

If the *[[Gradient]]* 
		(the vector of the partial derivates)
	of a function $f$ is zero 
		at come point $x$
	then $f$ has a *[[Critical point]]* 
			(or *[[Stationary points]]*) 
		at $x$
The *[[Determinant]]* of the hessian at $x$ 
	is called 
			in some context,
		a discriminant
If this determinant 
		of the Hessian at $x$ is zero
	then $x$ is called a *degenerate critical point of $f$* 
		or a *non-Morse citicla point of $f$*
Otherwise, it is non-degenerate, 
	and called a *Morse critical point of $f$*

The Hessian matrix plays 
		an important role in *[[Morse theory]]* 
			and *[[Catastrophe theory]]*
	because its *[[Kernel]]* and *[[Eigenvalue|eigenvalues]]* 
		allows classification of the critical points.

The determinant of the Hessian matric
	when evaluated at a critical point 
		of a function
			is equal to the *[[Gaussian curvature]]* 
				of the function considered as a maniflold.
The eigenvalues of the Hessian 
		at that point are 
			the principal curvature 
				of the fucntion
	and the eigenvectors are 
		the principal directions of curvature.
			(see *[[Gaussian curvature]] & [[Relation to principal curvatures]]*
	
## Use in optimization

Hessian matricies are 
	used in large-scale *[[Optimization]]* problems
		within Newton-type methods
			because they are the coefficent
				of the quadratic term
					of a local *[[Taylor expansion]]* 
						of a function
That is, 
$$y=f(x+\Delta x)\approx f(x)+\nabla f(x)^{T}\Delta x+ \frac{1}{2}\Delta x^{T}H(x)\Delta x$$
	where $\nabla f$ is the *[[Gradient]]* 
		$$\left( \cfrac{\partial f}{\partial x_{1}},\dots,\cfrac{\partial f}{\partial x_{n}} \right) $$

Computing and storing 
		the full Hessian matrix takes
			$\Theta \left( n^{2} \right)$ memory
	which is infeasible 
		for high-dimensional fucntions 
			such as the *[[Loss functions]]* of 
					*[[Neural nets]]* ,
				*[[Conditional random fields]]*
				and other *[[Statistical models]]*
					with large number of parameters.
For such siuations, 
		*[[Truncated-Newton]]*
		and *[[Quasi-Newton]]*
	algorithms have been developed.
The latter family of algorithms 
		use approximations to the Hessian;
	one of the most popular quasi-Newton algorith is *[[BFGS]]*	

Such approximations may use 
	the fact that
		an optimazation algorithm 
			uses the Hessian only as *[[Linear operator]]* $H(v)$ 
	and proceed by first noticing that 
		the Hessian also appears in 
			the local expansion of 
				the gradient:
					$$\nabla f(x+\Delta x)=\nabla f(x)+H(x)\Delta x+\mathcal{O}(\lvert \lvert \Delta x \rvert \rvert^{2} )$$
	Letting $\Delta x=rv$
		for some scalar $r$ 
			this gives 
			$$H(x)\Delta x=H(x)rv=rH(x)v=\nabla f(x+rv)-\nabla f(x)+\mathcal{O}(r^{2})$$
			that is, 
			$$H(x)\mathbf{v}=\frac{1}{r}[\nabla f(x+r\mathrm{v})-\nabla f(x)]+\mathcal{O}(r)$$
	so if the hradient is alredy computed, 
		the approximate Hessian
			can be computed by
				a linear 
						(in the size of the gradient)
					number of scalar operations.
	While simple to program, 
		this approzimation scheme 
			is not numberically stabel since $r$ 
				has to be made small 
					to prevent error due to 
						the $\Theta(r)$ term
							but decreasing it
								loses precision 
									in the first term.

Notably regarding Randomized Search Heuristics, the [evolution strategy](https://www.wikiwand.com/en/Evolution_strategy "Evolution strategy")'s covariance matrix adapts to the inverse of the Hessian matrix, [up to](https://www.wikiwand.com/en/Up_to "Up to") a scalar factor and small random fluctuations. This result has been formally proven for a single-parent strategy and a static model, as the population size increases, relying on the quadratic approximation.[](https://www.wikiwand.com/en/Hessian_matrix#cite_note-7)

### Other applications

The Hessian matrix is commonly used for expressing image processing operators in [image processing](https://www.wikiwand.com/en/Image_processing "Image processing") and [computer vision](https://www.wikiwand.com/en/Computer_vision "Computer vision") (see the [Laplacian of Gaussian](https://www.wikiwand.com/en/Laplacian_of_Gaussian "Laplacian of Gaussian") (LoG) blob detector, [the determinant of Hessian (DoH) blob detector](https://www.wikiwand.com/en/Blob_detection#The_determinant_of_the_Hessian "Blob detection") and [scale space](https://www.wikiwand.com/en/Scale_space "Scale space")). It can be used in [normal mode](https://www.wikiwand.com/en/Normal_mode "Normal mode") analysis to calculate the different molecular frequencies in [infrared spectroscopy](https://www.wikiwand.com/en/Infrared_spectroscopy "Infrared spectroscopy").[](https://www.wikiwand.com/en/Hessian_matrix#cite_note-8) It can also be used in local sensitivity and statistical diagnostics.[](https://www.wikiwand.com/en/Hessian_matrix#cite_note-9)