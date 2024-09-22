A **Subspace** of a vector space $V$ is a subset $W$ which satisfies,
1. The zero vector is in $W$
2. if $\vec{x},\vec{y}\in W$ then also $\vec{x}+\vec{y}\in W$
3. if $\vec{x}\in W$ and $k$ is any scalar, then also $\vec{k}x\in W$
***
The **Span** of vector $\{\vec{v_{1}},\dots, \vec{v}_{n}\}$ is
- Span $\{\vec{v_{1}},\dots, \vec{v}_{n}\} = \{c_{1}\vec{v_{1}}+ c_{2}\vec{v_{2}}+\dots+ c_{n}\vec{v}_{n}\ | \ c_{i} \in \mathbb{R}\}$
***
A **Relation** on a set of vectors $\{\vec{v_{1}},\dots, \vec{v}_{n}\}$ is any expression of the form 
$$c_{1}\vec{v_{1}}+ c_{2}\vec{v_{2}}+\dots+ c_{n}\vec{v}_{n}=0$$
where the $c_{i}$ are scalars
***
The set of vectors $\{\vec{v_{1}},\dots, \vec{v}_{n}\}$ **Linearly Independent** if whenever 
$$c_{1}\vec{v_{1}}+ c_{2}\vec{v_{2}}+\dots+ c_{n}\vec{v}_{n}=0$$
for some scalars $c_{i}$, then $c_{1}=c_{2}=\cdots=c_{n}=0$
***
A **basis** for $V$ is a ==orered set== of vectors in $V$ which are both *linearly independent*and span $V$

- A set of vectors is a *basis* if and only if it is a minimal spanning set.
- A set of vectors is a *basis* if and only if it is a maximal linearly independent set.
***
The **dimenson** of a vector space is the number (possibly infinite) of elements in a basis.
- Let $V$ be a vector space with *dimension* $m$ then.
	- we can find at most $m$ linearly indepenent vectors in $V$
	- we need at least $m$ vectors to span $V$
	- any set of $m$ linearly independent vectors in $V$ is a basis
	- any set of $m$ vectors which spans $V$ is a basis
***
Let $V$ and $W$ be vector spaces. 
A **Linear Transformaation** is a mapping $T: V\rightarrow W$ that satisfies,
- $T(\vec{x}+\vec{y}) = T(\vec{x})+T(\vec{y})$ for all vectors $\vec{x}, \vec{y} \in V$
- $T(k \vec{x}) = kT(\vec{x})$ for all vectors $\vec{x} \in V$ and all sclaars $k$
***
An **Isomorphisim** is a bijective linear transformation
```ad-seealso
title:Recall
Recall that **bijective** means the map is both **surjective** and injective.
- **Surjective** means the image of $T$ is the whole target
- **Injective** means that if $x\neq y$ are two elements in the source, then $T(x)\neq T(y)$
```
***
The **image** of a linear transformation $T: V\rightarrow W$ is 
$$im T = \{\vec{w}\in W \ | \ T(\vec{v}) = \vec{w} \quad \exists \vec{v}\in V\}$$
***
The **Rank** of the transformation $T: V\rightarrow W$ is the *dimension* of the image.
***
The **Kernel** of a linear transformation $T: V\rightarrow W$ is 
$$\text{ker}(T) = \{\vec{v} \in V \mid T(\vec{v}) = \vec{0}\}$$
```ad-info
title:Remember
- $\text{dim}(\text{im}(t))$ is called the *rank* of $T$
- Another word for $\text{dim}(\text{ker}(t))$ is *nullity*
```
***
The **standard matrix** of a linear transformation $T: \mathbb{R}^{m} \rightarrow \mathbb{R}^{n}$ is the unique $n\times m$ matrix $A$ such that $T(\vec{x}) = A \vec{x} \quad \forall\vec{x}\in \mathbb{R}^{m}$ 
This is the same as the **matrix of** $T$ **in the standard basis**
- The rank of $T$ is the same as the rank of the matrix $A$
- The image of $T$ is the span of the column of $A$
- $T$ is an isomorphisim if and only if $A$ is invertible,
	- same as $\det A\neq 0$
- The kernal of $A$ is the solution of $A \vec{x}= \vec{0}$
***
**Rank-Nullity Theorem:**
let $T: V\rightarrow W$ be a *linear transformation*, where $V$ is finite dimensional, then
$$\text{dim }(\text{im}(T)) + \text{ dim }(\text{ker}(T)) = \text{dim}(V)$$
```ad-example
title: The rank-nullity theorem implies the folowing facts:
- if $V$ and $W$ were vector space of the **same** dimension. The following are equivalent,
	- $T$ is surjective
	- $T$ is injective
	- $T$ is an isomorphism
```

```ad-caution
title:Caution
color: 219, 4, 22
the ideas above is **FALSE** for infinite dimensional vector space! 
```

```ad-example
title: Theorem
Two finite dimensional vector spaces $V$ and $W$ are **isomorphic** 
- if and only they have the dimension
```

```ad-caution
title:Caution
color: 219, 4, 22
This theorem says that two vectors spaces of demension $17$ are isomorphic.
**However**, *does not say* that every linear map beyween them is an isomorphism
- only that *some map* between them is.
***
For example, the linear transformation $\mathbb{R}^{2}\rightarrow\mathbb{R}^2$ **projection** onto some line is **not** an isomorphism, 
- though the source and target are isomorphic
```
***
**Coordinates:** 
Let $V$ be an infinite dimensional vector space with basis $\mathcal{B} = (\vec{v_{1}},\vec{v_{2}},\dots, \vec{v}_{n})$  
The $\mathcal{B}$**-coordinates** of $\vec{v}$ are the unique scalars $a_{i}$ such that
$$\vec{v}=a_{1}\vec{v}_{1}+a_{2}\vec{v}_{2}+\cdots + a_{n}\vec{v}_{n}$$ are arranged into a column vector
$$
[\vec{v}]_{\mathcal{B}} = 
\begin{bmatrix}
a_{1}\\
a_{2}\\
\vdots \\ 
a_{n}
\end{bmatrix}
$$
***
Let $\mathcal{A}$ and $\mathcal{B}$ be two bases for $V$ 
The map sending $[\vec{x}]_{\mathcal{B}} \mapsto [\vec{x}]_{\mathcal{A}}$ for each $\vec{x} \in V$
- is a ****linear transformation****

It's standard matrix is called the **change of basis matrix from $\mathcal{B}$ to $\mathcal{A}$** 
***
**Change of Basis Matrix:**
- The *change of basis matrix from $\mathcal{B}$ to $\mathcal{A}$* is the unique standard matrix $S_{\mathcal{B}\rightarrow\mathcal{A}}$
	- such that
	- $$S_{\mathcal{B}\rightarrow\mathcal{A}}[\vec{x}]_{\mathcal{B}} = [\vec{x}]_{\mathcal{A}} \quad \text{ for all } \vec{x}\in V$$
we know how to write down the change of matrix!
```ad-note
title: Formula for change of basis matrix
color:217, 105, 7
- if $\mathcal{B} = (\vec{v}_{1},\dots, \vec{v}_{n})$,
- then, $$S_{\mathcal{B} \rightarrow \mathcal{A}} = [[\vec{v_1}]_{\mathcal{A}} \ [\vec{v_2}]_{\mathcal{A}} \ \cdots \ [\vec{v_n}]_{\mathcal{A}}]$$
- this is the unique matrix such that 
- $$S_{\mathcal{B}\rightarrow\mathcal{A}}[\vec{v}]_{\mathcal{B}} = [\vec{v}_{\mathcal{A}}]$$ for all $\vec{v} \in V$
```
***
Two $n\times n$ matricies $A$ and $B$ are **similar** if there exists an invertible $n\times n$ matrix $S$ such that $B = S^{-1}AS$ 
- So the theorem sats that the matricies of $T$ in diffrene bases are similar to each other.

The change of basis matrix $S_{\mathcal{B}\rightarrow\mathcal{A}}$ is easy to find when $\mathcal{A}$ is an =="nice basis"== 
```ad-example
title:example
- When $V = \mathbb{R^n}$ and $\mathcal{A}$ is the standard basis.
- If $\mathcal{B} = (\vec{v_{1}},\vec{v_{2}},\dots, \vec{v}_{n})$ 
- and, $\mathcal{E} = (\vec{e_{1}},\vec{e_{2}},\dots, \vec{2}_{n})$ 
	- then, 
		- $$S_{\mathcal{B}\rightarrow\mathcal{E}} = [\vec{v_{1}} \ \vec{v_{2}} \ \dots \ \vec{v}_{n}]$$
```
***
The **Length** or **Magnitude** $\|\vec{v}\|$ of a vector $\vec{v}$ in $\mathbb{R}^{n}$ is $\sqrt{ (\vec{v}\cdot \vec{v}) }$
- *scalar product of the vectors $\vec{v}$*
***
Vectors $\vec{v}$ and $\vec{w}$ in $\mathbb{R}^{n}$ are **perpendicular** (*Orthogonal*) if $\vec{v}\cdot \vec{w}=0$
- when the scalar product of the two vectors is equal to zero
***
Vectors $\{\vec{u_{1}}, \dots, \vec{u}_{n}\}$ are an **orthonormal set** if $\vec{u}_{i} \cdot \vec{u}_{j} = 0$ 
- unless $i = j$, which case $\vec{u}_{1}\cdot \vec{u}_{j} = 1$ 
	- Equivalently, they are unit length and mutually perpendicaular
***
```ad-info
title:Theorem
An *orthonormal set of vectors is lineary independent*
```
***
The **orthonormal complement** of a subspace $V$ of $\mathbb{R}^{n}$ is the subspace
$$V^{\perp}=\{\vec{x}\in\mathbb{R}^{n}\mid \vec{x}\cdot \vec{v}=0 \quad \exists \ \vec{v}\in V\}$$
***
```ad-info
title:Theorem
- Let $V$ be a subspace of $\mathbb{R}^n$ then $V\cap V^{\perp} = 0$
- and $\text{dim}(V) + \text{dim}(V^{\perp}) = n$
- Furthermore, $(V^{\perp})^{\perp} = V$
```
***
**Orthogonal Projection:**
Every vector $\vec{x} \in \mathbb{R}^{n}$ can be written uniquely as $\vec{x}^{\|}+\vec{x}^{\perp}$
- where $\vec{x}^{\|}\in V$ and $\vec{x}^{\perp} \in V^{\perp}$ 
	- The linear transformation taking each vector $\vec{x}$ to $\vec{x}^{\|}$ is called the **Projection onto** $V$ 
		- ***Why projection onto $V$ has image $V$ and kernal $V^{\perp}$***
		- ***Why does the map fix all elements of $V$***
			- Understand this geometrically.

We can imagine the vector $\vec{x}^{\perp}$ as a perpendicaular line segment "dropped form the head of $\vec{x}$ down to $V$" 
The difference, $\vec{x}^{\|}$ lies in $V$ 
This $\vec{x}^{\|}$ is the projection of $\vec{x}$ onto $V$
- Put differently, the *projection* of $\vec{x}$ to $V$ is the closest vector in $V$ to $\vec{x}$
	- Shortest distance.
***
Compute Projections,
```ad-important
title:Theorem
Let $V$ be a subspaceof $\mathbb{R}^{n}$ and $\{\vec{u_{1}}, \dots, \vec{u}_{n}\}$ be an orthonormal basis for $V$
- Then the orthogonal projection onto $V$ is 
	- $\vec{x} \mapsto \text{proj}_{v}(\vec{x}) = (\vec{x}\cdot\vec{u}_1)\vec{u}_1+(\vec{x}\cdot\vec{u}_2)\vec{u}_2+\dots+(\vec{x}\cdot\vec{u}_d)\vec{u}_d$
```
**NOTE:** - Every Subspace of $\mathbb{R}^{n}$ has an orthonormal basis

A good technnique for finding an orthonormal basis is **Gram Schmidt Orthonormalization** 
This techique takes any basis to an orthonormalized basis.

Or **QR Factorization**
***
A linear transformation $T: \mathbb{R}^{n}\mapsto \mathbb{R}^{n}$ is **orthogonal**
- if and only if $T(\vec{x})\cdot T(\vec{y})=\vec{x}\cdot \vec{y}$ for all $\vec{x},\vec{y}\in\mathbb{R}^{n}$ 

A linear transformation $T$ is orthogonal exactally when $T$ respect dot products.
Geometrically, this means $T$ preserves the length of every vector, as well as the angles between the vectors.
***
A composition of orthogonal transformations is orthogonal 
Orthogonal transformations are invertible, 
- the inverse of an orthogonal transformation is also orthogonal
***
A **matrix** $A$ is **orthogonal** if it is square $n\times n$ and $A^{T}A=I_{n}$ 
***
Following are equivalent for any $n\times n$ square matrix $A$:
- $A$ is orthogonal
- $A$ is the (standard) matrix of an orthogonal tramsformation
- $AA^{T}=I_{n}$
- the **columns** *and* **rows** of $A$ are **orthonormal**
***
$\text{Rank}(A) = \text{Rank}(A^{T})$
$(AB)^{T} = B^{T}A^{T}$
$(A+B)^{T}=A^{T}+B^{T}$
***
A matix is **symmetric** if $A = A^{T}$
***
A matric is **skew-symmetric** if $A = -A^{T}$
***
Recall, that a system $A\vec{x}=\vec{b}$ is **consistent** if and only if $\vec{b}$ is in the image of $A$
***
The **least square** solution to the system $A\vec{x}=\vec{b}$ are the actual solutions to the consistent system $A\vec{x}=\text{proj}_{\text{im}(A)}(\vec{b})$ 
we think of these as ==the solutions to the closest consistent system.==

**NOTE:** the least squares solutions to the system $A\vec{x}=\vec{b}$ are the same as the actual solutions to $A^{T}A\vec{x}=A^{T}\vec{b}$
***
**Moving matrices across Scalar product**
- Let $A$ be any $m\times n$ matrix
	- Then $A\vec{x}\cdot \vec{y}=\vec{x}\cdot A^{T}\vec{y}$
	- Then $(\text{ker}(A))^{\perp}=\text{im}(A^{T})$
***
**Inner Product**
An inner product combines two vectors in a vector space $V$ to get a **scalar**. Just like, the dot product in $\mathbb{R}^{n}$ 

an **inner product** on a vector space $V$ is a function
$$V\times V\rightarrow\mathbb{R}$$
which assigns to each pair of vectors $f, g$ some scalar $\langle f, g\rangle$ called the *inner product*

A vector space $V$ with a choice of an inner product is called an **inner product space**
***
The **Magnitude** of a vector $\vec{v}$ is an *inner product space*, denoted $\|\vec{v}\|$ is the scalar $\sqrt{ \vec{v}^{2}+\vec{v}^{2} }$ 

We say that $\vec{w}$ is  **perpendicular** (or *orhogonal*) to $\vec{v}$ if $\langle \vec{v}, \vec{w}\rangle = 0$
***
**Orthonormality**
A set of vectors $\{\vec{u_{1}},\vec{u}_{2}, \dots, \vec{u}_{n}\}$ in an innner product space is orthonormal 
- if $\langle u_{i}, u_{j}\rangle = 0$ for $i\neq j$ and $\langle u_{i}, u_{j}\rangle = 1$ for all $i$

the *Gram-Schmidt orthonormalization* technique works in any vector space!

Similarly, we can compute the projection to a subspace of an innver prodcut spce just as we did in $\mathbb{R}^{n}$
- That is if $\vec{u_{1}},\vec{u}_{2}, \dots, \vec{u}_{d}$ form an orthonormal basis for a subspace $W$ of an inner product space,
	- then the projection of any $\vec{x}\in V$ onto $W$ is:
		- $$\langle\vec{x}, \vec{u}_{1}\rangle\vec{u}_{1}+\langle\vec{x}, \vec{u}_{2}\rangle\vec{u}_{2}+\cdots+\langle\vec{x}, \vec{u}_{d}\rangle\vec{u}_{d}$$
The Projection on $\vec{x}$ to the subspace $W$ *is the closest vector* in $W$ to the vector $\vec{x}\in V$
This is used in spaces of functions,
- (which are inner product spaces using integration) 
	- eg $\langle f, g\rangle = \int_{-4}^{4} f \ g \, dx$)
		- to compute the closet function of a certin nice type.
			- The projection to the subspace $W$ givec the closest function in $W$ to the original
***
**Computing the Determiant**
Determiants are defined only for square matrices.
The determiant of a $1\times 1$ matrix is simply its unique scalar entry
The determiant for a larger size matricies is defined indectively using **Laplace expansion**

The **Laplace expansion along row $i$ of $A$** is the expression
$$\sum_{j=1}^{n} \ (-1)^{i+j} \cdot a_{ij} \cdot \det(A_{ij})$$
where $A_{ij}$ is the submatrix of $A$ obtained by deleting row $i$ and column $j$

Likewise, the **Laplace expansion along the column $j$ of $A$** is the expression
$$\sum_{i=1}^{n} \ (-1)^{i+j}\cdot a_{ij}\cdot \det(A_{ij})$$
Thus, the laplace expansion along any row or column gives the same scalar
***
**Properties of the determinant**
- The determinant of $A$ and $A^{T}$ are equal for any $n\times n$ matrix $A$
- The determinant is **multiplicative**: that is,
	- $\det(AB) = \det(A)\cdot \det(B)$
- The determiant of an *orthogonal matrix* is $\pm 1$ 
- if $A$ is an $n\times n$ matrix, then $\det(kA)= k^{n}\det(A)$ 
- A square matrix is invertible if any only if its determinant is nonzero
***
The following are equivalent about an $n\times n$ matrix $A$

- $\det(A) = 0$
- The *rank* of $A$ is less than $n$
- There is a non-trival relation on the columns of $A$
- There is a non-trival relation on the row of $A$
- $A$ is not invertible
- $0$ is an eigenvalue of $A$
***
**Simillar** matricies have the same *trace* and *determiant*

The *determinant* of a linear transformation $T: V\rightarrow V$
- where $V$ is finite dimensional
	- is the determinant of any matrix $[T]_{\mathcal{B}}$ representing $T$

This definiton makes sense because even though the matriceis $T_{\mathcal{B}}$ and $T_{\mathcal{A}}$ are different for the diffrent chouces of bases $\mathcal{B}$ and $\mathcal{A}$ 
- we know they are similar
	- and so they have the same determinant

Matrix $B$ is simmilar to $A$ is there exists an invertible matrix $Q$ such that $B = Q^{-1}AQ$
***
Let $V$ be a finite dimensional vector space.
A linear transformation $T:V\rightarrow V$ is an *isomorphism* if and only if $\det(T) \neq 0$
***
Let $\mathbb{R}^{n}\rightarrow\mathbb{R}^{n}$ be the linear transformation given by multiplication by the $n\times n$ matrix $A$.
Then the $n$-volume of the *image* of the unit $n$-cube is $|\det(A)|$  
***
The determinant has an important property called **multilinearity** in the rows and columns.
This means that fixing all but one column,
- the determinant is a linear function in the remainig column

*Precisely:*
Fix $n-1$ column vectors $\vec{v}_{1}, \dots, \vec{v}_{n-1} \in \mathbb{R}^{n}$ 
then the fucntion, 
$$\mathbb{R}^{n}\rightarrow\mathbb{R}$$
$$\vec{x}\mapsto \det[\vec{v}_{1} \ \vec{v}_{2} \ \dots \ \vec{v}_{n-1} \ \vec{x}]$$ 
is a linear transformation
The same is true if $\vec{x}$ is inserted as the $j$-column, instead of the $n$-th, for any $j$
A simmialr statemnt holds for the rows

#### Example
Becasue the determinant is linear in  the first column, we have
$$
\det \begin{bmatrix}
1 & 2 & 3 \\ 
4 & 5 & 6 \\ 
7 & 8 & 9
\end{bmatrix} +
\det \begin{bmatrix}
0 & 2 & 3 \\ 
0 & 5 & 5 \\ 
100 & 8 & 9
\end{bmatrix}
= \det \begin{bmatrix}
1 & 2 & 3 \\ 
4 & 5 & 6 \\ 
107 & 8 & 9
\end{bmatrix}
$$
**Note:** two columns are the same, and only the first column has elements being added. 
also 
$$\det \begin{bmatrix}
1 & 2 & 3 \\ 
4 & 5 & 6 \\ 
7 & 8 & 9
\end{bmatrix} +
2\det \begin{bmatrix}
1 & 2 & 3 \\ 
1 & 1 & 1 \\ 
7 & 8 & 9
\end{bmatrix}
= \det \begin{bmatrix}
1 & 2 & 3 \\ 
6 & 7 & 8 \\ 
7 & 8 & 9
\end{bmatrix}$$
by linearity in the middle row.

another property is the **Alternating Property** of the determinant:

Let $A$ be a square matrix.
Let $A'$ be the matrix obtained by swapping two columns, 
Then, $\det(A) = -\det(A')$
Same holds if we swap two rows.

- this implies that if we make $k$ swaps of rows/columns,
	- The determinant is multiplued by $(-1)^{k}$
***
An **eigenvector** of a linear transformation $T: V\rightarrow V$ is any non-zero vector $\vec{v}\in V$ such that 
$T(\vec{v}) = \lambda \vec{v}$ for some scalar $\lambda$ 
The scalar $\lambda$ **eignevalue** of the *eigenvector* $\vec{v}$

**Caution:** Not every transformation has an eigenvector!
***
Let $T: V\rightarrow V$ be a linear transformation.
An **eigenbasis** is a basis for $V$ consisting of *eigenvector* for $T$

**Caution:** Not every transformation has an eigenbasis!
***
Let $T: V\rightarrow V$ be a linear transformation.
It is **diagonalizable** if $V$ admits an eigenbasis for $T$
A matrix $A$ is **diagonalizable** if the linear transformation defined by left multiplication by $A$ is *diagonalizable*

*An equivalent way to define diagonalizable matrix*

The matrix $A$ is *diagonalizable* if and only if there exists invertible matrix $S$ such that 
$S^{-1}AS$ is **diagonal.**
In this case the columns of $S$ form an eigenbasis for $A$

Understand **WHY** tge characterization of a *diagonalizble* matrix is equivalent ti haveing an eigen basis.

Note that using the change of basis formulation, 
- if $\mathcal{B}$ is an eigen basis for $A$ and $\mathcal{U}$ denotes the standard basis, then 
$$[A]_{\mathcal{B}}=S_{\mathcal{U}\rightarrow\mathcal{B}}[A]_{\mathcal{E}}S_{\mathcal{B}\rightarrow\mathcal{E}}=S^{-1}AS$$
where $S$ is the matrix made from the columns of $\mathcal{B}$
***
Let $\lambda$ be an eigenvalue of a linear transformation$T$.
The subset of $V$ 
$$E_{\lambda} = \{\vec{v}\in V \mid T(\vec{v})=\lambda \vec{v}\}$$
is called the $\lambda$-eigen space of $T$
Its dimension is the geometric multiplicity of $\lambda$
$\text{dim}(E_{\lambda}) =$ geometric multiplicity

The $\lambda$-eigenspace is a subspace of $V$
- It consists of all the $\lambda-eigenvalues$ together with the zero vector
***
Fix an eigenvalue $\lambda$ of the $n\times n$ matrix $A$ 
The $\lambda$-eigenspace of $A$ is the space
$$E_{\lambda}=\text{ker}(A-\lambda I_{n})$$

Rank-nullity is useful for computing geometric multiplicity

For transformations $T: V\rightarrow V$ where $V$ is finite dimension $n$, 
the eigenspace and geometric multiplicity can be computed by $\text{ker}(A-\lambda I_{n})$, 
- where $A$ is any $\mathcal{B}$- matrix

Dont Forget! after computing the kernel of this matrix.
that you must reinterpet the elements in $V$ using the basis $\mathcal{B}$
***
Let $T: V\rightarrow V$ be a linear transformation.
where $V$ is $n$-dimensional.
Then, $T$ has an **eigenbasis** if and only if the sum of the geometric multiplicites of all its eigenvalues to $n$ 
***
Let $A$ be an $n\times n$ matrix. 
Then, $A$ is diagonalizable if and only if, the sum of the geometric multiplicites of all its eigenvalues adds up to $n$
***
Consider an $n\times n$ matrix $A$.
The **characteristic polynomial** of $A$ is the degree $n$ polynomial
$$\mathcal{X}_{A}(x)=\det(xI_{n}-A)$$
we can also define is as so,
$$\mathcal{X}_{A}(x)=\det(A-xI_{n})$$
***
#### Example
Suppose that $T: V\rightarrow V$ is diagonalizable.
This means that there exists a basis $\mathcal{B}$ (an eigenbasis) such that
$$
[T]_{\mathcal{B}} = 
\begin{bmatrix}
a_{11} \\ 
& a_{22} \\ 
& & \ddots \\ 
& & & a_{nn}
\end{bmatrix}
$$
The diagonal elements $a_{ii}$ are the eigenvalues of $T$ 
Computing the characteristic polynomial, 
we see that 
$$\mathcal{X}_{T}(x)=(x-a_{11})(x-a_{22})\cdots (x-a_{nn})$$
where $a_{ii}$ are the eigenvlaues of $T$ (possible repeated multiple times)
***
Let $A$ be an $n\times n$ matrix with eigenvalues $c_{1}, \cdots, c_{n}$ (listed more than once, according ti their algebraic multiplicities). Then,
1. The **Trace** of $A$ is the sum $c_{1}+\cdots+c_{n}$ of the eigenvalues
2. The determinat of $A$ is the product $c_{1}\cdot, c_{2}, \dots, \cdot c_{n}$ of the eigenvalues
$$\det(A)=\prod_{j=1}^{m} \ \lambda_{j}, \quad\quad \text{tr}(A) = \sum_{j=1}^{m}\ \lambda_{j}$$
***
Let $T: V\rightarrow V$ be a linear transformation of a finite dimensional vector space $V$.
The **Algebraic multiplicity** of an eigenvalye $\lambda$ is the largest power $r$ such that $(x-\lambda)^{r}$ divides the characteristic polynomial.
***
For each eigenvalue of a linear transformation,
the geometric multiplicity is at most the algebraic multiplicity
$$\text{gemu}(\lambda)\leq \text{almu}(\lambda)$$
***
If a linear transformation of an $n$-dimensional space has $n$ distinct eigenvalues, then it is diagonalizable.
***
A **Symmetric** $n\times n$ matrix always has an orthonormal eigenbasis
- *symmetric matrix* is always diagonalizable!
- all *eigenvalues* of a symmetrix matrix are real
***
The Spectral theorem states: 
Let $A$ be a symmetric $n\times n$ mtrix.
There exists an orthogonal matrix $S$ such that $S^{*}AS$ is diagonal/

**check understanding:** Why do the columns of $S$ form an eigenbasis for $A$, and why the elements on the diagonal of the diagonal matrix are all eigenvalues. 
***
**Non singular matrix**
- A square matrix whoose determinant is non-zero.
- Is invertible

***
**Singular matrix**
- Determinant of a matrix is zero
- inverse does not exist
***
**Adjoint**
- Transpose of a matrix
***
**Complex Conjugate**
- Transpise of a matrix
- and applying a *complex conjugate* on each of the entry
***
**Hermetian** (*self adjoit*)
- complex square matrix that is equal to its own conjugate transpose
- $A = A^{*}\quad for A\in \mathbb{C}^{m\times n}$ 
***
**Unitary** (hermetian adjoint)
- an non-singular (invertible) complex matrix $U$ is *unitary*
	- if its conjugate transpose is also its inverse.
		- $U^{*}U = UU^{*}=UU^{-1}=I$
		- $\langle Ax, y\rangle = \langle x, A^{*}y\rangle$
	- ==Properties==
		- Given two complex vectors $x$ and $y$. Multiplication by $U$ preserves their inner product.
			- $\langle Ux, Uy \rangle = \langle x, y\rangle$
		- $U$ is normal
			- $U^{*}U=U^{*}$
				- has non negative real eigenvalues (positive semidefinite)
		- $U$ is diagonalizable; that is (*unitarlly simillar*) to a diagonal matrix, as consequence of the spectral theorem. 
			- Thus, $U$ has a decomposition of the form $U = VDV^{*}$ 
		- Eigenspaces are orthogonal
	- Equivalent conditons
		(if $U$ is a square complex matrix, then the following conditions ar equivalent)
		- $U$ is unitary
		- $U^{*}$ is unitary
		- $U$ is invertible with $U^{-1}=U^{*}$
		- The columns of $U$ form an **orthonormal basis** of $\mathbb{C}^{n}$ with respect to the usual inner product
			- in other words $U^{*}U=I$
		- $U$ is an **isometry** with respect to the usual norm.
			- that is $\|Ux\|_{2} = \|x\|_{2}$ for all $x\in\mathbb{C}^{n}$ 
				- where $\|x\|_{2}=\sqrt{ \sum_{i=1}^{n} \ \vert x_{i}\vert^{2} }$
		- $U$ is normal matrix 
			- Equivalently there is an orthnnormal basis formed by the eigenvector of $U$
			- with eigenvalues lying on the unit circle.
- Note: an **Orthogonal** matrix is a real square matrix, whose columns and rows are *orthonormal* vectors.
- (*unitrary* but for real numbers)
***
**Invariance**
an object or class of mathematical objects, remains unchanged after operations or transformations of a certin type are applied to the objects.
- The **Spectruem of a matrix** is invariant under change of basis.
	- the *determinant*
		- *trace*
		- *eigenvectors*
		- *eigenvalues*
			- are invariant under a change of basis.
- **Singular values** are invariant under orthogonal transformations.

#### Invariance under Unitary Multiplication
***
One of the many special properties of the matrix $2$ norm is that 
- like the vector $2$-norm.
	- it is invarient under multiplication by unitary matrices.
		- *The same property holds for **Frobenius** norm*

For any $A\in\mathbb{C}^{m\times n}$ and unitary $Q \in \mathbb{C}^{m\times m}$ we have
$$\|QA\|_{2}=\|A\|_{2} \quad \|QA\|_{F}=\|A\|_{F}$$
- *Proof:*
	- Since $\|Qx\|_{2}=\|x\|_{2}$ for every $x$ 
		- by $\|Qx\|=\|x\|$
			- The invariance of inner product meabs that the angles between vectors are preserved, and so are their lengths
		- The invarience in the two norm follows from, 
			- $$\|A\\|_{(m, n)} = \underset{x\in\mathbb{C}^{n}\quad x\neq 0}{\mathbf{sup}} = \cfrac{\|Ax\|_{(m)}}{\|x\|_{(n)}}= \underset{x\in \mathbb{C}^{n} \quad \|x\|_{(n)}=1}{\mathbf{sup}}\|Ax\|_{(m)}$$
	- Remains valid if $Q$ is generalized to a rectuangular matrix with orthonormal columns, 
		- that is, $Q\in\mathbb{C}^{p\times m}$ with $p>m$
	- Analogus identities also hold for multiplicaiton by unitary matricies on the right, 
		- or more generally, by rectangular matricies with orthonormal rows.
*COOl Puzzle: MU puzzle*
***
**Positive Difinite**
A matrix $M$ with real entries is positive-definite is the real number $z^{T}Mz$ is positive for every non zero real column vector $z$ 

A *hermetian matrix* (a comlex matrox equal to its conjugate trannspose) is **positive definite** 
- if the real number $z^{T}Mz$ is positive for every non zero complex column vector $z$

- **Positive Semi-Definite** 
	- matricies are defined similary, 
		- excpet the scalars $z^{T}Mz$ and $z^{*}Mz$ are 
			- required to be positive ==or zero== (that is, nonnegative)

- A matrix $M$ is *positive-definite* if and only if it satsfies <u>any</u> of the following equivalent matricies
	- $M$ is congruant with a diagonal matrix with positive real entries
	- $M$ is symmetric or hermetian, and all its eigenvalues are real and positive
	- $M$ is symmetric or hermetian, and all its leading principal minior are positive
	- There exists an invertible matrix $B$ with a conjugate tanspose $B^{*}$ such that $M = B^{*}B$

Positive-definite and positive-semidefinite real matrices are at the basis of convex optimization,
- since, given a function of several real variables that is twice differentiable,
	- then if its Hessian matrix matrix of its second partial derivatives is positive-definite at a point p, 
		- then the function is convex near p, 
		- and, conversely, if the function is convex near p, 
			- then the Hessian matrix is positive-semidefinite at p.