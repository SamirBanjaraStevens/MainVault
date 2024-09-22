the **complex conjugate** of a scalar $z$.
- Written $\bar{z}$ or $z^{*}$ 
	- is obtained by negating its imaginary part
	- For real $z, \bar{z} = z$

The **Hermitian conjugate**
- or (**adjoint**)
	- of any $m\times n$ matrix $A$, written $A^{*}$, is the 
		- $n\times m$ matrix whose $i, j$ entry is  the 
		- complex conjugate of the $j,i$ entry of $A$

$$
A = 
\begin{bmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}\\
a_{31} & a_{32}
\end{bmatrix}

\rightarrow

A^{*} =
\begin{bmatrix}
\bar{a_{11}} & \bar{a_{21}} & \bar{a_{31}}\\
\bar{a_{12}} & \bar{a_{22}} & \bar{a_{32}}
\end{bmatrix}
$$

if $A = A^{*}$ 
- $A$ is hermitian
- must be square

For real $A$,
- **adjoint** interchanges the rows and columns of $A$ ^c19a1e
- can be thought of as **transpose**
	- denoted $A^{T}$
	- If real matrix is hermitian that is $A = A^{T}$, then it is also **symmetric**


### **Unitary Matrices**

a square matrix $Q\in \mathbb{C}^{m\times m}$ is **unitary **
- in real matrix, we say **orthogonal** 
If $Q^{*} = Q^{-1}$, i.e, 
- if $Q^{*}Q = I$
- or $q_{i}q_{j} = \delta_{ij}$ 
	- The columns of a unitary matrix $Q$ form an orthonormal matrix basis of $\mathbb{C}^{m}$ 


### **Multiplication by a Unitary Matrix**

![[Pasted image 20230221094505.png]]

The process of multiplication by a unitary matrix or its adjoint 
- preserve geometric structure in the Euclidean sense
	- because inner products are preserved. 
	- That is, for Unitary $Q$
$$(Qx)^{*}(Qy) = x^{*}y$$

The invariance of inner products means that angles between vectors are preserved and so are their lengths:
$$\|Qx\| = \|x\|$$
in the real case,
- multiplication by an orthogonal matrix $Q$ corresponds to a rigid rotation (if det $Q=1$ ) or reflection (if det $Q = -1$) of the vector space

