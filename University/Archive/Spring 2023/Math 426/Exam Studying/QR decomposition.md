**QR Decomposition** or **QR Factozization**
	is a [[decomposition]] of a [[matricies|matrix]] $A$ into product $A=QR$ 
		of an *[[Orthonormal matrix]]* $Q$ 
		and an *[[Upper triangular matrix]]* $R$
Often used to solve the *[[Linear least square]]* problem
	and is the basis for a particular *[[Eigenvalue algorith]]*, the *[[QR algorithm]]* 

## Cases and Definitions

#### Square matrix

Any real *[[Square matricies]]* $A$ may be decomposed as 
	$A=QR$
		where $Q$ is an *[[Orthogonal matrix]]* 
				(its columns are *[[Orthogonal unit vectors]]* 
					meaning $Q^{T}=Q^{-1}$
		and $R$ is an upper *[[Triangular matrix]]* 

If $A$ is *[[Invertible]]* 
	then the factorization is unique 
		if we require deagonal elements of $R$ to be positive

If insted $A$ is a comple square matrix,
	then there is a decomposition $A=QR$ 
		where $Q$ is a *[[Unitary matrix]]* 

If $A$ has $n$ *[[linearly independent]]* columns,
	then the first $n$ columns of $Q$ form an *[[Orthonormal basis]]* 
		for the *[[Column space]]* of $A$.

More generally, the first $k$ columns of $Q$ form an orthonormal basis
	for the *[[Span]]* of the first $k$ columns of $A$ for any $1\leq k\leq n$

The fact that any column $k$ of $A$ only depends on first columns of $Q$ 
	corresponds to the triangular form of $R$

#### Rectangular matrix

More generally, we can factor a complex $m\times n$ matrix $A$ with $m\geq n$ 
	as the product of $m\times m$ *[[Unitary matrix]]* $Q$ 
		and an $n\times n$ upper triangular matrix $R$
As the bottom $(m-n)$ rows 
	of an $m\times n$ upper triangular matrix 
		consists entirely of zeros 
	It is often useful to partiion $R$ or both $R$ and $Q$:
		$$A=QR=Q\left[ \begin{array}{}R_{1}\\0\end{array} \right] = \left[ Q_{1} \ \ Q_{2} \right]\left[ \begin{array}{}R_{1}\\0\end{array} \right]=Q_{1}R_{1}$$
		where $R_{1}$ is an $n\times n$ upper triangular matirx,
		$0$ is an $(m-n)\times n$ zero matrix
		$Q_{1}$ is $m\times n$ 
		$Q_{2}$ is $m\times(m-n)$ 
			and both $Q_{1}$ and $Q_{2}$ both have orthogonal columns.
				**Refered to as the *reduced QR factorization*** 
		If $A$ is of full *[[rank]]* $n$
			and we require that the diagonal elements of $R_{1}$ are positive
				then $R_{1}$ and $Q_{1}$ are unique
					but in general $Q_{2}$ is not.
		$R_{1}$ is then equal to 
			the upper triangular factor of the *[[Cholesky decomposition]]* of 
				$A^{*}A=(A^{T}A)$ if $A$ is real 

We can use 
	*[[Gram-Schdmit]]* 
	*[[Householder reflections]]* (*Householder transformations, Householder method*)
	Givens rotations

## Connection to a determinant or a product of eigenvalues

We can use QR decomposition to find the *[[Determinant]]* of a square matrix.
Suppose a matrix is decomposed as $A=QR$, then we have
$\det(A)=\det(Q)\det(R)$ 

$Q$ can be chosen such that the $\det(Q)=1$. Thus,
$$\det(A)=\det(R)=\Pi_{i}r_{ii}$$
	where $r_{ii}$ are the diagonal entries of $R$

Furthermore, becasue the determinant 
	equals the product of the eigenvalues, 
		we  have
$$\prod_{i}r_{ii}=\prod_{i}\lambda_{i}$$
	where the $\lambda_{i}$ are the eigenvalues of $A$

We can extend the above properties to a non-square complex matrix $A$
	by introducing the definition of QR factorization
		for the non-square complex matricies
			and replacing the eigenvalues with singular values

Start with a QR decomposition for a non-square matrix $A$ 
$$A=Q\left[ \begin{array}{}R\\0\end{array} \right], \quad Q^{*}Q=I$$
	where $0$ denotes the zero matrix
		and $Q$ is an unitary matrix.

From the properties of the *[[SVD]]* 
	and the determinant of a matrix, we have
$$\left|\prod_{i}r_{ii}\right|=\prod_{i}\sigma_{i}$$
	where the $\sigma_{i}$ 
		are the singular values of $A$

**Note** that the singular values of $A$ and $R$ are identical,
	although their complex eigenvalues may be different.

However if $A$ is square, then
$$\prod_{i}\sigma_{i}=\left|\prod_{i}\lambda_{i}\right|$$
It follows that the QR decomposition can be used efficiently to calcuate the product of the eigenvalues or singular values of a matrix.