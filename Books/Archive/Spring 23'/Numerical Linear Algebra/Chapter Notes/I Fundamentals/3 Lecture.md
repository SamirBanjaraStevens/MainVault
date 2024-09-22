
Norms measure approximations and convergence.

A **norm** is a function $\|\cdot\|:\mathbb{C}^{m}\rightarrow\mathbb{R}$ 
	that assigns a real-valued length to each vector.

In order to conform to a resonable notion of length, 
	a norm must satisfy the following three conditions.
		For all vectors $x$ and $y$ and for all scalars $\alpha \in\mathbb{C}$ 
			- $\|x\|\geq 0, \quad \text{ and } \|x\|=0 \text{ only if } x=0$ 
				- the norm of a nonzero vector is positive
			- $\|x+y\|\leq\|x\|+\|y\|$
				- the norm of a vector sum does not exceed the sum of the norms of its parts
					- (the triangle inequality)
						-  the sum of the lengths of any two sides 
							must be greater than or equal to the length of the remaining side
			- $\|\alpha x\| = |\alpha| \ \|x\|$
				- scaling a vector scales its norm by the same ammount


**The Closed Unit Ball**
	$\{  x \in\mathbb{C}^{m}:\|x\|\leq 1 \}$
		corresponding to each norm

$$
\tag{3.2}
\begin{align}
\|x\|_{1} &= \sum_{i=1}^{m} | x_{i}| \\
\|x\|_{2} &= \left( \sum_{i=1}^{m} |x_{i}|^{2}\right)^{\frac{1}{2}} = \sqrt{ x^{*}x } \\
\|x\|_{\infty} &= \underset{1\leq i\leq m}{\text{max}} \ |x_{i}| \\
\|x\|_{p} &=\left( \sum_{i=1}^{m} |x_{i}|^{p} \right)^{\frac{1}{p}} \quad (1 \leq p \leq \infty) \\
\end{align}
$$

**Weighted p-norms**
	Each of the coordinates of a vector space is given its own weight.
	In general, given any norm $\|\cdot\|$ 
		a weighted norm can be written as 
			$$\tag{3.3}\|x\|_{W}=\|Wx\|$$
	Here $W$ is the diagonal matrix 
		in which the $i$th diagonal entry is the weight $w_{i}\neq 0$
	For Example, a weighted $2-$norm $\|\cdot\|_{W}$ on $\mathbb{C}^{m}$ is specfied as follows:
		$$\tag{3.4}\|x\|_{W}=\left( \sum_{i=1}^{m} |w_{i}x_{i}|^{2} \right)^{\frac{1}{2}}$$
	One can also generalize the idea of a weighted norms 
		by allowing $W$ to be an arbitrary nonsingular matrix, 
			(not necessarily diagonal)


## Matrix Norms Induced by Vector Norms

An $m\times n$ matrix can be viewed as a vector in an $mn$-dimensional spaace:
	each of the $mn$ entries of the matrix is an independent coordinte.

Any $mn-$dimensional norm can there fore be used for measuring 'size' of such a matrix.

However, in dealing with a space of matricies, certain special norms are more useful
	than the vector norm $(3.2)-(3.3)$ already discussed.

These are the *induced matrix norms* 
	defined in terms of the behaviour of a matrix
		as an operator between its normed domain and range spaces.

Given vector norms $\|\cdot\|_{(n)}$ and $\|\cdot\|_{(m)}$ 
	on the domain and the range of $A \in\mathbb{C}^{m\times n}$ 

The induced matrix norm $\|A\|_{(m, n)}$ is the smallest number $C$ for which the following inequality holds for all $x \in \mathbb{C}^{n}$ 
$$\tag{3.5}\|Ax\|_{(m)}\leq C\|x\|_{(n)}$$
In orther words, 
	$\|A\|_{(m,n)}$ is the supremum of the ratios $\frac{\|Ax\|_{(m)}}{\|x\|_{(n)}}$ over all vectors $x \in\mathbb{C}^{n}$ 
		the maximum factor by which $A$ can 'Steach' a vector $x$ 

We say that $\|\cdot\|_{(m,n)}$ is the matrix norm induced by $\|\cdot\|_{(m)}$ and $\|\cdot\|_{(n)}$

Because of scalar condition *(3)* of *Eq (3.1)* 
	the action of $A$ is determined by its actions on unit vectors.

Therefore, the matrix norm can be defined equivalentlly in terms of the images of the unit vectors under $A$:
$$\tag{3.6}\|Ax\|_{(m,n)}=\underset{\underset{x\neq 0}{x \in\mathbb{C}^{n}}}{\text{sup}}\cfrac{\|Ax\|_{(m)}}{\|x\|_{(n)}}=\underset{\underset{\|x\|_{(n)}=1}{x \in\mathbb{C}^{n}}}{\text{sup}}\|Ax\|_{(m)}$$

## Example 3.3 The 1-Norm of a Matrix
#### $\|A\|_{1}$ is equal to the "maximum column sum" 
##### Proof:

write $A$ in terms of its colums 
$$\tag{3.8}A=\left[ a_{1}\mid\dots \mid a_{n} \right] $$
where each $a_{j}$ is an $m$ vector

Conside the 1-norm unit unit ball, 
	this is the set 
		$$\left\{  x \in\mathbb{C}^{n}:\sum_{j=1}^{n} \ |x_{j}| \ \leq 1 \right\}$$
Any vector $Ax$ in the image of this set satsfies,
$$\|Ax\|_{1}=\left\|\sum_{j=1}^{n}x_{j}a_{j}\right\|_{1}\leq \sum_{j=1}^{n}|x_{j}|\|a_{j}\|_{1}\leq\underset{1\leq j\leq n}{\text{max}}\|a_{j}\|_{1}$$
Therefore, the induced matrix 1-norm 
	satsfies $\|A\|_{1}\leq \text{max}_{1\leq j\leq n}\|a_{j}\|_{1}$
By choosing $x=e_{j}$,
	where $j$ maximixes $\|a_{j}\|_{1}$, 
		we attain thisbound and thus the matrix norm is,
			$$\tag{3.9}\|A\|_{1}=\underset{1\leq j\leq n}{\text{max}}\|a_{j}\|_{1}$$
By the same argument we can show the $\infty$-norm is equal to the "maximum row sum"
	and the $2$-norm is equal to the "maximum eigenvalue"


The most important norm which is not induced by a vector norm is the *Hilbert-Schmidt* or the *Frobenius norm*, defined by
$$\tag{3.16} \|A\|_{F}=\left( \sum_{i=1}^{m}\sum_{j=1}^{m} |a_{ij}|^{2} \right)^{\frac{1}{2}}$$
*observe* that this is the 
	same as the $2$-norm of the matrix 
		when viewwed as an $mn$-dimensional vector

Written in terms of indivisual rows or columns,
	for example, if $a_{j}$ is the $j$th column of $A$, we have,
		$$\tag{3.17}\|A\|_{F}\left( \sum_{j=1}^{n}\|a_{j}\|_{2}^{2} \right) ^{\frac{1}{2}}$$

This identity,
	as well as the analogous result based on rows insted of columns,
		can be expressed compactaly by the equation, 
			$$\tag{3.18} \|A\|_{F}=\sqrt{ \mathrm{Tr}(A^{*}A) }=\sqrt{ \mathrm{Tr}(AA^{*}) }$$
				where $\mathrm{Tr}(B)$ denotes the *trace* of $B$ 
					(the sum of its diagonal entries)


### **Invariance Under Unitary Multiplication**

special property of the matrix 2-norm
- like the vector 2-norm,
it is invariant under multiplication by unitary matrices.
- Same property holds for Frobenius norm 

#### **Theorem 3.1**
- For Any $A\in\mathbb{C}^{m\times n}$ and unitary $Q\in \mathbb{C}^{m\times m}$ we have
	- $\|QA\|_{2} = \|A\|_{2}, \quad \|QA\|_{F} = \|A\|_{F}$

*Proof*: 
Since $\|Qx\|_{2} = \|x\|_{2}$ for every $x$, by (2.10)
the invariance in the 2-norm follows from (3.6)
For the Frobenius norm we may use (3.18)

Theorem 3.1 remains valid if $Q$ is generalized to a rectangular matrix with orthonormal columns,
- that is $Q\in \mathbb{C}^{p\times m}$ with $p>m$ 