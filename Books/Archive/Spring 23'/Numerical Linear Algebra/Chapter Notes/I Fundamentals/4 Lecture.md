The singular value decomposition **(SVD)** is a matrix factorization 

## Geometric Observation.

SVD is motivated by the following geometric fact:
		- The image of the unit sphere under any $m \cdot n$ matrix is a hyperellipse.
		- Applicable to both real and complex matrices. 
			- However, in describing geometric interpretation
				- We assume as usual that the matrix is real

**Hyperellipse** : $m$-dimensional generalization of an ellipse. 
- In $\mathbb{R}^{m}$ , hyperellipse is defined as the surface obtained by stretching the unit sphere , sphere of radius one around a given center, set of points of distance 1 from a fixed centre point, where different norms can be used as general notions of "distance" , in $\mathbb{R}^{m}$ by some factors $\sigma_{1}, \cdots, \sigma_{m}$ (possibly zero) in some orthogonal directions $u_{1}, \cdots, u_{m}\, \in \mathbb{R}^{m}$  
	- Let $u_{i}$ be unit vectors, i.e, $||u_{i}||_{2} = 1$ 
		- The vectors $\{\sigma_{1}\, u_{i}\}$ are the **principal semiaxes** of the hyperellipse, with lengths $\sigma_{1}, \cdots, \sigma_{m}$. 
- If  $A$ has rank $r$, exactly $r$ of the lengths $\sigma_{i}$ will turn out to be nonzero, and in particular, if $m \geq n$, at most $n$ of them will be non zero.

By the unit sphere, we mean the Euclidean sphere in $n$-space, i.e., the unit sphere in the 2-norm; denoted by $S$.
-   Then, $AS$, the image of $S$ under the mapping of $A$, is a hyperellipse

Let $S$ be the unit sphere in $\mathbb{R}^{n}$ , and take and $A\in \mathbb{R}^{m\times n}$  with $m\geq n$ .
- Suppose That $A$ has full rank $n$.
- The image $AS$ is a hyperellipse in $\mathbb{R}^{m}$ 

Properties of $A$ in terms of the shape of $AS$ 

**$n$ singular values** of $A$
- Lengths of the $n$ principal semiaxes of $AS$, written $\sigma_{1}, \cdots, \sigma_{m}$ .
	- Conventional to assume, singular value numbered in descending order, $\sigma_{1}\geq \sigma_{m}\geq \cdots \geq \sigma_{n} > 0$ 
**$n$ left singular vectors** of $A$ (orthonormal, since they are unit vectors they have size 1) ^ceb613
- Unit vectors $\{u_{1}, u_{2}, \cdots, u_{n}\}$ oriented in the direction of the principal semiaxis of $AS$, numbered to correspond with the singular values. 
	- Thus the vector $\sigma_{i}\, u_{i}$ is the largest principal semiaxis of $AS$
**$n$ right singular vectors** of $A$ (orthonormal, since they are unit vectors they have size 1) ^c8bd95
- Unit vectors $\{v_{1}, v_{2}, \cdots, v_{n}\} \in S$ that are the pre-images of the principal semiaxes of $AS$ 

- Numbered so that $Av_{j} = \sigma_{j}\, u_{j}$ 

**Left** - **Right** notion comes from the position of the the factors $U$ and $V$ 


## Reduced SVD

Equation relating to right singular vectors $\{v_{j}\}$ and left singular vectors $\{u_{j}\}$ can be written,
$$\tag{4.1} Av_{j} = \sigma_{j}u_{j}, \quad 1\leq j\leq n$$ 
this collection of vector quantities can be expressed as a matrix equation, $AV = \hat{U} \hat{\Sigma}$ 
- $\hat{\Sigma}$ is an $n\times n$ diagonal matrix with positive real entries
	- since, $A$ was sussumed to have full rank $n$
- $\hat{U}$ is an $m\times n$ matrix with orthogonal columns
- $V$ is an $n\times n$ matrix with orthonormal columns
	- Thus $V$ is unitary
	- And we can multiply on the right by its inverse $V^{*}$ to obtain,
	- $$\tag{4.2} A = \hat{U} \hat{\Sigma} V^{*}$$
- This factorization of $A$ is called a *Reduced Singular Value Decomposition*, or <u>reduced SVD</U> , of $A$ 
- 
**Note** : hat denotes reduced SVD

![[Pasted image 20230207095503.png]] 

## Full SVD

Columns of $\hat{U}$ are $n$ orthonormal vectors in the $m$-dimensional space $\mathbb{C}^{m}$ 
- Unless $m=n$
	- Then, they do not form a basis of $\mathbb{C}^{m}$, nor is $\hat{U}$ a unitary matrix.
	- However, adjoining an additional $m - n$ orthonormal columns,
		- $\hat{U}$ can be extended to a unitary matrix (full basis) for $\mathbb{R}^{m}$ 
			- Denoted arbitrarily as $U$ 

*Full* SVD of $A$ ($m \geq n$) :
- $$\tag{4.3} A = U \, \Sigma \, V^{*}$$ 
Here,
- $U$ is $m\times m$ and unitary
- $V$ is $n\times n$ and unitary
- $\Sigma$ is $m\times n$ and diagonal with positive real entries. 

![[Pasted image 20230207095533.png]]

Dashed lines indicated the "*Silent*" columns of $U$ and rows of $\Sigma$ that are discarded in passing from *(4.3)* to *(4.2)*. 

If we disregard assumption, A is full rank,
- if A is rank-deficient, the factorization *(4.3)* is still appropriate.
	- Now only $r$ of the left singular vectors of $A$ are determined by the geometry of the hyperellipse. 
- To construct the unitary matrix $U$,
	- Introduce $m - r$ instead of $m - n$ additional arbitrary orthonormal columns.
- Matrix $V$ will also need $n-r$ arbitrary orthonormal columns to extend the $r$ columns determined by the geometry.
- Matrix $\Sigma$ will have $r$ positive diagonal entries,
	- with remaining $n-r$ equal to zero
The reduced SVD (4.2) also applies for matrices if $A$ of less than full rank.
- take $\hat{U}$ to be $m\times n$, 
- with $\hat{\Sigma}$ of dimensions $n\times n$, with some zeros on the diagonal, 
- or, further compress, so $\hat{U}$ is $m\times r$ and $\hat{\Sigma}$ is $r\times r$ and strictly positive on the diagonal.

## Formal Definition

Let $m$ and $n$ be arbitrary;
- $m\geq n$ not required.

Given $A\in \mathbb{C}^{\,m\, \times \, n}$, (not necessarily of full rank)
- *singular value decomposition*    **(SVD)** of $A$ is a factorization, 
	- $$\tag{4.3} A = U\,\Sigma\, V^{*}$$

Where,
$$\begin{align} U &\in \mathbb{C}^{\, m\, \times \, m} \quad &\text{is unitary,} \\ V &\in \mathbb{C}^{\, n\, \times \, n} \quad &\text{is unitary,} \\ \Sigma &\in \mathbb{R}^{\, m\, \times \, n} \quad &\text{is diagonal.} \end{align}$$

Assumed that the diagonal entries $\sigma_{j}$ of $\Sigma$ are non-negative and in non-increasing order; that is, $\sigma_{1}\geq \sigma_{2}\geq \cdots \geq \sigma_{p}\geq 0,$ 
- where $p=min(m,n)$

**Note :** diagonal matrix $\Sigma$ has the same shape as $A$ even when $A$ is not square, 
- but $U$ and $V$ are always square unitary matrices. 

Image of the unit sphere in $\mathbb{R}^{n}$ under a map $A=U\,\Sigma\,V^{*}$ must be a hyperellipse in $\mathbb{R}^{m}$

Unitary map $V^{*}$ 
- preserves the sphere
	- the diagonal matrix $\Sigma$ stretches the sphere into a hyperellipse aligned with the canonical basis, 
	- and the final unitary map $U$ rotates or reflect the hyperellipse without changing its shape.

Thus, if we prove <u>every matrix has an <b>SVD</b></u>, : we shall prove that <u>the image of the unit sphere under any linear map is a hyperellipse</u>

## Existence and Uniqueness

### Theorem 4.1
- *Every matrix $A\in \mathbb{C}^{\, m\, \times \, n}$ has a singular value decomposition **(4.4)**.
- *Furthermore, the singular values $\{\sigma_{j}\}$ are uniquely determined* 
- *and, if $A$ is square and the $\{\sigma_{j}\}$ are distinct, the **left** and **right** singular vectors $\{u_{j}\}$ and $\{v_{j}\}$ are uniquely determined up to complex signs (i.e., complex scalar factors of absolute value 1).*



### example

$$
`A =
\begin{pmatrix}
1 & 2 \\
0 & 2
\end{pmatrix}`
$$
$A: \mathbb{R}^{2} \rightarrow \mathbb{R}^{2}$

$$
Ax =
\begin{bmatrix}
1 & 2 \\
0 & 2
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
x+2y \\
2y
\end{bmatrix}
$$

(notes from lecture)

**Proof :** 
- To prove existence of **SVD** isolate the direction of the largest action of $A$,
- and, then by induction on the dimensions of $A$.
- Set $\sigma_{1} = \|A\|_{2}$ , 
- By compactness argument, there must be a vector $v_{1}\in \mathbb{C}^{n}$ with $\|v_{1}\|_{2} = 1$ and  $\|u_{1}\|_{2} = \sigma_{1}$ , where $u_{1} = Av_{1}$ 
- Consider, 
	- extensions of $v_{1}$ to an orthonormal basis $\{v_{j}\}$ of $\mathbb{C}^{n}$ ,
	- and of $u_{1}$  to an orthonormal basis $\{u_{j}\}$ of  $\mathbb{C}^{n}$, 
	- and let $U_{1}$ and $V_{1}$ denote the unitary matrices with columns $u_{j}$ and $v_{j}$, respectively. 
- Then we have, 
	- $$\tag{4.5} U_{1}^{*}\, A \, V_{1} = S = \begin{bmatrix}\sigma_{1} & w^{*} \\ 0 & B\end{bmatrix},$$

		- where $0$ is a column vector of dimension $m-1$ 
		- $w^{*}$ is a row vector of dimension $n-1$ 
		- $B$ has dimensions $\,(m-1\,) \, \times\, \,(n-1\,)$ 
- Furthermore, (Cauchy Schwarz inequality)
 $$
\left\|
\,\begin{bmatrix}\sigma_{1} & w^{*} \\ 0 & B\end{bmatrix} \,\begin{bmatrix}\sigma_{1} \\ w\end{bmatrix}
\,
\right\|_{2}
\ \geq \
\sigma_{1}^{2} + w^{*}w \ = \ (\sigma_{1}^{2} + w^{*}w)^{\frac{1}{2}}
\
\left\|
\begin{bmatrix}
\sigma_{1}\\
w
\end{bmatrix}
\right\|_{2}
 $$
  Implying $\|S\|_{2}\ \geq \ (\sigma_{1}^{2} + w^{*}w)^{\frac{1}{2}}$ 

Since $U_{1}$ and $V_{1}$ are unitary, we know that $\|S\|_{2} = \|A\|_{2} = \sigma_{1},$

Which implies $w = 0$
 If $n=1$ or $m=1$, we are done
Otherwise, the submatrix $B$ describes the action of $A$ on the subspace orthogonal to $v_{1}$ 
	- By the induction hypothesis, 
		- $B$ has an **SVD** $B = U_{2}\,\Sigma_{2}\,V_{2}^{\,*}$
			- It is how easily verified,
$$
A \ =\ U_{1} \
\begin{bmatrix}
\
1 & 0 \\
0 & U_{2}
\
\end{bmatrix}

\begin{bmatrix}
\
\sigma_{1} & 0 \\
0 & \Sigma_{2}
\
\end{bmatrix}

\begin{bmatrix}
\
1 & 0 \\
0 & V_{2}
\
\end{bmatrix}^{*}
V_{1}^{\,*}
$$
is an SVD of $A$

For Uniqueness  
- the geometric justification if straightfordward:
	- if the semiaxis lengths of a hyperelipse are disticnt,
		- then the semiaxes themselves are determied by the geometry up to signs,
- Algebraically we cab argue,
	- First $\sigma_{1}$ is uniquely determined by the condition that it is equal to $\|A\|_{2}$, as follows from (4.4)
	- Now suppose that in addition to $v_{1}$ there is another linearly independent vector $w$ with $\|w\|_{2} = 1$ and $\|Aw\|_{2} =\sigma_{1}$ 
		- define a unit vector $v_{2}$, orthogonal to $v_{1}$, as a linear combination of $v_{1}$ and $w$ 
$$v_{2} = \frac{w - (v_{1}^{*} \, w)v_{1}}{\|w-(v_{1}^{*}\,w)v_{1}\|_{2}}$$



Since $\|A\|_{2} = \sigma_{1}, \quad \|Av_{2}\|_{2} \leq \sigma_{1}$ 
but this must be an equality, for otherwise,
since $w = v_{1}c + v_{2}s$ for some constants of $c$ and $s$ with $|c|^{2} + |s|^{2} = 1$ 
we would have $\|Aw\|_{2} < \sigma_{1}$ 

This vector $v_{2}$ is a second right singular vector of $A$ corresponding to the singular value of $\sigma_{1}$
- it will lead to the appearance of a vector $y$ (equal to the last $n-1$ components of $V_{1}^{*}v_{2}$) with 
	- $\|y\|_{2} = 1$ and $\|By\|_{2} = \sigma_{1}$ 

we conclude that, if the singular vector $v_{1}$ is not unique then the corresponding singular value $\sigma_{1}$ is not simple 

to complete the uniqueness proof, we note that, as indicated above, 
- once $\sigma_{1}, v_{1}, u_{1}$ are determined, the remainder of the SVD is determined by the action of $A$ on the space orthogonal to $v_{1}$
- Since $v_{1}$ is unique up to sign, this orthogonal space is uniquely defined, and tge uniqueness of the remaining singular values and vectors now follows by induction. 