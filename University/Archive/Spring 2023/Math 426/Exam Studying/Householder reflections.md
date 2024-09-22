A *[[Linear transformation]]* that describes a *[[Reflection]]* about a *[[Plane]]* or *[[Hyperplane]]* containing the origin.

Its analogue over general *[[Inner product spaces]]* is the *[[Householder operator]]* 

## Definiton

#### Transformation
***
The reflection hyperplane can be defined by its *normal vector*,
	a *[[Unit-vector]]* $v$ 
			(a vector with length $1$)
		that is *[[orthogonal]]* to the hyperplane.

The reflection of a *[[Point]]* $x$ about this hyperplane is the *[[Linear transformation]]* 
$$x-2\left< x, v \right> v=x-2v(v^{*}x)$$
	where $v$ is given as a column unit vector with *[[Conjugate transpose]]* 

#### Householder Matrix
***
The matrix constructed from this transformation 
	can be expressed in terms of an *[[Outter product]]* as:
		$$P=I-2vv^{*}$$
			$P$ is known as the **Householder Matrix**,
			$I$ is the *[[Identity matrix]]*

##### Properties
***
The Householder matrix has the following properties:
- It is *[[Hermetian]]*
- It is *[[Unitary matrix]]*
- hence it is *[[Involutory]]* 
- A Householder matrix has eigenvalues $\pm_{1}$
	- to see this, notice that if $u$ is orthogonal to the vector $v$
		- Which was used to create the reflector,
			- then $Pu=u$, i.e., (1 is an eigenvalue of multiplicity $n-1$)
				- since there are $n-1$ independent vectors orthogonal to $v$ 
					- Also notice $Pv=-v$
						- and so $-1$ is an eigenvalue with multiplicity $1$
- The determinant of a Householder reflector is $-1$
	- since the determinant of a matrix is the product of its eigenvalues
		- in this case one of which is $-1$ 
			- with the remainder being $1$

## Applications

#### Geometric optics
***
In geometric optics, 
	*[[specular reflection]]* can be expressed in terms of the Householder matrix

#### Numerical Linear Algebra
***
Used to annihilate the entries below the main diagonal of a matrix,
		to perform *[[QR decomposition]]* 
	and in the first step of the *[[QR algorithm]]* 
They are also wifely used for transforming to a *[[Hessenberg]]* form.
For symmetric or *[[Hermetian]]* matricies, 
	the symmetry can be preserved
		resulting in *[[Tridiagonalization]]* 

#### QR decomposition
***
Householder reflections can be used to calculate *[[QR decomposition]]* 
	by reflecting first one column of a matrix 
		onto a multiple of a standard basis vector
			calculating the transformation matrix, 
				multiplying it with the original matrix
					and then recursing down the $(i, i)$ *[[minors]]* of that product

#### Tridiagonalization
***
Uses altered $\text{sgn}$ function 
	with $\text{sgn}(0)=1$ 
In the first step
	to form the Householder matrix in each step
		we need to determine $\alpha$ and $r$ 
			which are:
					$\alpha=-\text{sgn}(a_{21})\sqrt{ \sum_{j=2}^{n}a_{j1}^{2} };$
					$r=\sqrt{ \frac{1}{2}(\alpha^{2}-a_{21}\alpha) }$
			from $\alpha$ and $r$ construct vector $v$:
					$v^{(1)}=\begin{bmatrix}v_{1}\\ v_{2}\\\vdots\\v_{n}\end{bmatrix},$ 
						where $v_{1}=0, v_{2}=\frac{a_{21}-\alpha}{2r}$ and 
							$v_{k}=\frac{a_{k1}}{2r}$ for each $k=3, 4, \dots, n$
				Then compute:
					$P^{1}=I-2v^{(1)}\left( v^{(1)} \right)^{T}$
					$A^{(2)}=P^{1}AP^{1}$
				having found $P^{1}$ 
					and computed $A^{(2)}$ 
						the process is repeated for $k=2, 3, \dots, n-2$  
							as follows:
$$
\begin{align}
\alpha&=-\text{sgn}\left( a_{k+1,\ k}^{k} \right)\sqrt{ \sum_{j=k+1}^{n} \left( a_{jk}^{k} \right)^{2}  } \\
r&=\sqrt{ \frac{1}{2}\left( \alpha^{2}-a_{k+1, \ k}^{k} \ \alpha \right)  }\\
v_{1}^{k}&= v_{2}^{k} = \dots = v_{k}^{k}=0 \\
v_{k+1}^{k}&=\cfrac{a_{k+1, \ k}^{k}-\alpha}{2r}\\
v_{j}^{k}&=\cfrac{a_{jk}^{k}}{2r} \quad \text{for } j=k+2, k+3, \dots, n\\
P^{k}&=I-2v^{(k)}\left( v^{(k)} \right)^{T} \\
A^{(k+1)}&= P^{k}A^{(k)}P^{k} \\
\end{align}								
$$
								contniniuing in this manner, 
									the tridiangonal 
										and symmetric matrix is formed

The Householder transformations  
	was shown to have a one-to-one relationshop
		with the canonical coset decomposition
			of unitray matricies
				defined in group theory
					which can be used to parametrze
						unitry operators in a very efficent manner.

A single Householder transform 
	can act on all columns of a matrix
		and such exhibits computational cost for $QR$ decomposition
			and tridiagonolozation
The penalty for this 'computational optimality'
	is that the Householder operations 
		cannot be as deeply or efficently parallelized.
As such Householder is preferred for dense matricies on sequential machines,
	whilst Givens is preferred on sparse matricies 
		and/or parallel machines.