## Eigenvalues and Eigenvectors

Let $A \in \mathbb{C}^{m\times m}$ be a square matrix

A nonzero vector $x \in \mathbb{C}^{m}$ is an *eigenvector* of $A$ 
and $\lambda \in \mathbb{C}$ is its corresponding *eigenvalue*

if $$Ax = \lambda x$$
Action of matrix $A$ on a subspace $S$ of $\mathbb{C}^{m}$
may sometimes mimic <u>scalar multiplication</u> 

When this occurs, the special subspace $S$ is the *eigenspace*,
	and, any nonzero $x \in S$ is an eigenvector

  The set of all the eigenvalues of a matrix $A$ is the *spectrum* of $A$ a subset denoted by $\Delta(A)$ 

```ad-note
title: NOTE
Eigenvalues problems make sense only when the range and the domain spaces are the same.

***

This reflects the fact that in applicaiton eigenvalues are generally used where a matrix is tobe compounded iteratively, 
***
either explicitly as a power $A^{k}$
or, implicitly in a functional form such as $e^{tA}$
``` 

#### Usefulness
***
Eigenvalues and eigenvectors are useful for two reasons.

Eigenvalue analysis can simplify solutions of certain problems by 
	reducing a coupled system to a collection of scalar problems.

Physically, it can also give insight into b behavior of evolving systems governed by linear equations. 

Such as study of *resonance* (Musical instruments MRI machines.)

or *Stability* (fluid flows when subjected to small perturbations) 

### Eigenvalue decomposition
***
An *eigenvalue decomposition* of a square matrix $A$  is a <u>factorization</u>
$$\tag{24.2}A = X\Delta X^{-1}$$
(such factorization does not always exist)
But, here $X$ is nonsingular and $\Delta$ is diagonal ^9a8f4f

which can be rewritten as such,
$$\tag{24.3} AX = X\Delta$$
that is 
$$
\left[\begin{array}{}
\\
& A &\\
\\
\end{array}\right]
= 
\left[\begin{array}{c|c|c}
\\
x_{1} & x_{2} & \cdots & x_{m}\\
\\
\end{array}\right]
=
\left[\begin{array}{c|c|c}
\\
x_{1} & x_{2} & \cdots & x_{m}\\
\\
\end{array}\right]
=
\begin{bmatrix}
\lambda_{1} \\ 
& \lambda_{2} \\ 
& & \ddots \\ 
& & & \lambda_{m}
\end{bmatrix}
$$

This makes it clear that is $x_{j}$ is the $j$-th column of $X$ and $\lambda_{j}$ is the $j$-th diagonal entry of $\Delta$ 
	then, $Ax_{j} = \lambda_{j}x_{j}$ 

Thus, the $j$-th column of $X$ is an eigenvector of $A$ and the $j$-th entry of $\Delta$ is the corresponding eigenvalue $\lambda$

The eigenvalue decomposition expresses *a change of basis* to “<u>eigenvector coordinates</u>" 

If $Ax = b$ and $A = X\Delta X^{-1}$, we have 
$$\tag{24.4} (X^{-1}b) = \Delta(X^{-1}x)$$
Thus, to compute $Ax$, 
	we can expand $x$ in the basis of columns of $X$,
		apply $\Delta$ 
			and interpret the results a vector of coefficients of linear combination of the columns of $X$

## Geometric Multiplicity

The set of eigenvector corresponding to a single eigenvalue,
	together with the zero vector, 
		forms a subspace of $\mathbb{C}^{m}$ know as *eigenspace* 

If $\lambda$ is an eigenvalue of $A$ its corresponding eigenspace if $E_{\lambda}$ 
	- An eigenspace $E_{\lambda}$ is an example of an *invariant subspace* of $A$ 
		- that is $AE_{\lambda} \subseteq E_{\lambda}$ 

The dimension of $E_{\lambda}$ can be interpreted as the maximum number of linearly independent eigenvectors that can be found, all with the same eigenvalue $\lambda$ 
$$\text{dim}(E_{\lambda}) = \text{ dim}(A-\lambda I)$$ this number is the geometric multiplicity of the nullspace $N(T)$ of $A - \lambda I$
Since that null space is again $E_{y}$
Thus, Nullspace $N(t) = E_{y}$ Eigenspace

## Characteristic Polynomial

The *Characteristic Polynomial* of $A \in \mathbb{C}^{m\times m}$ denoted $p_{A}$ of simply $p$ is the <u>degree</u> $m$ <u>polynomial</u> defined by,
$$\tag{24.5}p_{A}(z) = \det(zI-A)$$
- Due to the minus sign,
	- $p$ is *monic*:
		- the coefficient of its degree $m$ term is 1


#### Theorem 24.1
```ad-important
title: Theorem 24.1
$\lambda$ is an eigenvalue of $A$
if and only if $p_a(\lambda)=0$

***

*Proof:* This follows from the definiton of an eigenvalue:

$$
\begin{aligned}
\lambda \text{ is an eigenvalue } &\Leftrightarrow \text{ there is a non zero vector } x \text{ such that } \lambda x - Ax = 0\\
&\Leftrightarrow \lambda I - A \text{ is singular}\\
&\Leftrightarrow \det(\lambda I - A) = 0
\end{aligned}
$$
```

*Theorem 24.1* Is has an important consequence.
	Even if a matrix is real,
		some of its eigenvalues may be complex.

Physically, this is related to the phenomenon 
	that real dynamical systems can have motions 
		that oscillate as well as grow or decay.

Algorithmically, it means that even if the input to a matrix eigenvalue is real, the output may have to be complex.

## Algebraic Multiplicity

By the fundamental theorem of algebra,
	we can write $p_{a}$ in the form:
		$$p_{a}(z) = (z-\lambda_{1})(z-\lambda_{2})\dots (z-\lambda_{m})$$
for some numbers $\lambda_{j} \in \mathbb{C}$ 

By, *theorem 24.1*, each $\lambda_{j}$ is an eigenvalue of $A$ 
	and all eigenvalues of $A$ appear somewhere in the list 

In general, an eigenvalue might more than once. 

We define *algebraic multiplicity* of an eigenvalue $\lambda$ of $A$ to be its multiplicity as a root of $p_{a}$ 

An eigenvalue is *simple* if it's algebraic multiplicity is $1$

The characteristic polynomial givesus an easy way to count the number of eigenvalues of a matrix.

#### Theorem 24.2 
```ad-important
title:Theorem 24.2

If $A \in \mathbb{C}^{m \times m}$, then $A$ has $m$ eigenvalues,counted with algebraic multiplicity.
***
In particular, if the roots of $p_A$ are simple, then $A$ has $m$ distinct eigenvalues.
```

*Note*: that in particular, every matrix has at least one eigenvalue.

The algebraic multiplicity of an eigenvalue
	is at least as great as
		its geometric multiplicity

## Similarity Transformations

If $X \in \mathbb{C}^{m\times m}$ is non singular,
	then, the map $A \mapsto X^{-1}AX$ is called a *similarity transformation* of $A$. 

We sat that two, matrices $A$ and $B$ are *similar* if there is a similarity transformation relation one to the other
	(if there) exists a nonsingular $X \in \mathbb{C}^{m\times m}$ such that $B = X^{-1}AX$

As described above in the special case of diagonalization [[24 Eigenvalue Problems#^9a8f4f|(24.2)]], any similarity transformation is a change of basis operation
		Many properties are shared by similar matrices $A$ and $X^{-1}AX$ 

#### Theorem 24.3
***
```ad-important
title:Theorem 24.3
If $X$ is nonsingular, then $A$ and $X^{-1}AX$ have the same characteristic polynomial, eigenvalues, andalgebraic and geometric multiplicities. 

*Proof:*
The proof that the characestric polynomials match is straightfordward

$$
\begin{aligned}
P_{X^{-1}AX}(z) &= \det(zI-X^{-1}AX)\\
&= \det(X^{-1}(zI-A)X)\\
&= \det(X^{-1})\det(zI-A)\det(X)\\
&= \det(zI-A)\\
&= p_{A}(z)
\end{aligned}
$$
```

from the agreement of the characteristic polynomials, the agreement of the eigenvalues and algebraic multiplicitesfollows.

Finally, to proce that the geometric multiplicities agree, 
	verify that if $E_{\lambda}$ is an eigenspace for $A$, 
		then, $X^{-1}E_{\lambda}$ is an eigenspace for $X^{-1}AX$
And, conversely

#### Theorem 24.4
***
The algebraic multiplicity of an eigenvalue $\lambda$ is at least as great as its geometric multiplicity.   

Let $n$ be the geometric multiplicity of $\lambda$ for the matrix $A$ 
Form an $m\times n$ matrix $\hat{V}$ whose $n$ columns constitute an orthonormal basis of the eigenspace $\{x : Ax = \lambda x\}$ 
Then, extending $\hat{V}$ to a square unitary matrix $V$ we obtain $V^{*}AV$ in the form
$$\tag{24.7}B = V^{*}AV = \begin{bmatrix}
\lambda I & C \\ 
0 & D
\end{bmatrix}$$

where $I$ is the identity matrix,
$C$ is $n\times(m-n)$ 
and, $D$ is $(m-n)\times(m-n)$
By the definition of the determinant, 
$$
\begin{align}
\det(zI-B) &= \det(zI-\lambda I)\det(zI-D)\\
&= (z-\lambda)^{n}\det(zI-D)
\end{align}
$$
Therfore, the algebraic multiplicity of $\lambda$ as an eigenvalue of $B$ is at least $n$.
Since, similairty transformations preserve multiplicites, the same is true for $A$

## Defctive Eigenvalues and Matricies

Although a generic matrix has algebric and geometric multiplicites that are equal (name, all $1$), this is by no means true for every matrix.

#### Example 24.1
***
Consider the matrices,
$$
A = 
\begin{bmatrix}
2 \\ 
& 2 \\ 
& & 2
\end{bmatrix}
,\quad
B = 
\begin{bmatrix}
2 & 1 \\ 
& 2 & 1 \\
& & 2
\end{bmatrix}
$$
Both $A$ and $B$ have characteristic polynomial $(z-2)^{3}$, 
	so there is a single eigenvalue $\lambda = 2$ of algebraic multiplicity $3$.

  In this case of $A$, 
	  we can choose three independent eigenvectors 
		  $e_{1}, e_{2}, e_{3}$ 
			  so the geometric multiplicity is also $3$

For $B$ 
	we can only find one independent eigenvector 
		(a scalar multiple of $e_{1}$) 
			so the geometric multiplicity of the eigenvalue is only $1$

An eigenvalue whose algebraic multiplicity exceeds its geometric multiplicity is a *defective eigenvalue* 
	A matrix with a defective eigenvalue is a *defective matrix*

Any diagonalmatrix is nondefective.
	For such matrix, 
		both the algebraic and geometric multiplicites of an eigenvalue $\lambda$ 
			are equal to the number of occurances along the digonal.

## Diagonalizability

Only nondefective matricies can have an eigenvalue decomposition.

#### Theorem 24.5
***
an $m\times m$ matrix $A$ is *nondefective*
	if and only if it has an eigenvalue decomposition $A = XAX^{-1}$

**Proof:**
***
($\Leftarrow$) Given an eigenvalue decompositon $A = X\DeltaX^{-1}$, 
	we know by theorem *24.3* that $\Delta$ is simillar to $A$ with the same eigenvalues and the same multiplicites.

Since, $\Delta$ is a diagonal matrix, it is nondefective, and thus the same holds for $A$

($\Rightarrow$) A nondefective matrix must have $m$ linearly independent eigenvectors,
	becasue eigenvectors with diffrent eigenvalues be linearly independent.

And, each eigenvalue can contribute as many linearly independent eigenvectors as its multiplicity. 
	If these $m$ independent eigenvectors are formed into the columns of $X$ then $X$ is nonsingular and we have $A = X\Delta X^{-1}$ 

Another term for nondefective is *diagonalizable*.
	is it diagonalizable?
		is it factorable?
			is it nondefective?

## Determinant and Trace

The trace of $A \in \mathbb{C}^{m\times m}$ is the sum of its diagonal elements.
$$tr(A) = \sum_{j=1}^{m}a_{jj}$$

Both the trace and the determinant are related simply to the eigenvalues.

#### Theorem 24.6
***
The determiant $\det(A)$ and trace $\text{tr}(A)$ 
	are equal to the product 
		and the sum 
			of the eigenvalues of $A$, respeectively 
				counted with algebraic multiplicity:
					$$\tag{24.8}\det(A)=\prod_{j=1}^{m} \ \lambda_{j}, \quad\quad \text{tr}(A) = \sum_{j=1}^{m}\ \lambda_{j}$$
**Proof:** 
***
From *(24.5)* and *(24.6)*, we compute
$$
\begin{align}
\det(A) &= (-1)^{m}\det(-A)\\
&= (-1)^{m}p_{A}(0)\\
&= \prod_{j=1}^{m} \ \lambda_{j}  
\end{align}
$$

This establishes the first formula. 
As for the second, from *(24.5)* 
	it follows that the coefficent of the $z^{m-1}$ term of $p_{A}$ is the negative of the sum of the elements of $A$, 
		or $-\text{tr}(A)$
On the other hand, from *(24.6)*
	this, coefficent is also equal to $-\sum_{j=1}^{m} \ \lambda_{j}$

thus, $\text{tr}(A)  = \sum_{j=1}^{m} \lambda_{j}$ 

## Unitary Diagonalization

It sometimes happnes that not only does an $m\times m$ matrix $A$ have $m$ linearly independent eigenvectors,
	but these can be chosen to be orthogonal. 

In such a case, 
	$A$ is *Unitarily diagonalizable*,
thais is, there exists a unitary matrix $Q$ such that $$\tag{24.9}A = Q\Delta Q^{*}$$
This factorization is both an eigen value decompostion and a singular value decomnposion, 
	aside from the matter of sign (possibly complex) of the entries of $\Delta$

We have already seen some matricies that are unitarily diagonalizable: **The hermetian matricies**.

#### Theorem 24.7
***
A hermetian matrix is unitarily diagonalizable, 
and its eigenvalues are real.

**Proof:**
***
The hermetian matricies are not only the ones that are unitarily diagonalozable.
Other examples are *Skew-hermetian matricies, Unitary Matricies, circulant matricies, and anyof these plus a multuple of an identity*

In general, the calss of matricies that are unitarily diagonalizable have an elegant characterization.
 
By definition, we say that a matrix $A$ is *normal* if $A^{*}$
#### Theorem 24.8
***


**Proof:**
***

## Schur Factorization

#### Theorem 24.9
***

**Proof:**
***

## Eigenvalue-Revealing Factorizations