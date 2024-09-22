1. Label the following statements as true or false. Assume that the underlying inner product spaces are finite-dimensional.
	- (*a*).  All Projections are self-adjoint.
		- *Solution :* **False**
			- Orthogonal projections are self-adjoint, according to Theorem 6.24. 
			- However, an arbitrary projection and an orthogonal projection are not the same.
				- To be an orthogonal projection, the linear operator must be self-adjoint
				- However, to be an arbitrary projection, the linear operator, does not need to be self-adjoint.
	- (*b*). An orthogonal projection is uniquely determined by its range.
		- *Solution :* **True**
			- Unlike an ordinary projection, an orthogonal projection $T$ on $V$ ensures that 
				- $$R(T)^\perp = N(T) \quad \text{ and } \quad N(T)^\perp = R(T)$$
				- which combined with the fact that 
				- $$V = R(T) \oplus N(T)$$
				- Implies that an orthogonal projection is uniquely determined by it's range. 
	- (*c*). Every self-adjoint operator is a linear combination of orthogonal projections.
		- *Solution :* **True**
			- Every self-adjoint operator is a normal operator. 
			- Therefore, according to (5). of spectral theorem (6.25) 
				- it follows that every self-adjoint operator is a linear combination of orthogonal projections
	- (*d*). If $T$ is a projection on $W$, then $T(x)$ is the vector in $W$ that is closest to $x$ 
		- *Solution :* **False**
			- If $T$ is an **orthogonal projection** on $W$, then $T(x)$ is the closest vector to $x$ in $W$.
				- Because in the case of an orthogonal projection $T$
					- $T(x)$ is perpendicular to $x$  (belongs to $W^\perp$)
			- However, in the case of a arbitrary projection, as the question specifies, 
				- if $T$ is an arbitrary projection, 
					- we can be sure that $T(x) \in W^\perp$ 
						- or ($T(x)$ is perpendicular to $x$ )
	- (*e*). Every orthogonal projection is a unitary operator
		- *Solution :*
			- According to Theorem 6.24, 
				- $T$ is an orthogonal operator if and only if 
					- $T = T^* = T^2$
				- However, this does not imply that $T$ is invertible and its inverse if $T^*$ 
					- For $T$ to be invertible, 
						- we need $T$ to be one-to-one 
							- $N(T) = \{0\}$
						- which we don't necessarily know about an orthogonal operator

2. Let $V = \mathbb{R}^2$ 
	- $W = \text{ span}(\{(1,\, 2)\})$ 
	- and $\beta$ be the standard ordered basis for $V$ 

		- Compute $[T]_\beta$, where $T$ is the orthogonal projection of $V$ on $W$ 
			- *Solution :*
				- In order to compute $[T]_\beta$, 
					- we need to find the images of vectors from the standard basis $\beta$ by the orthogonal projection $T$ onto $W$ 
					- Then, represent the images of vectors and represent then as linear combination of the vectors form $\beta$
					- and then, put the coefficients along the vectors from $\beta$ into corresponding columns of the matrix $[T]_\beta$ 
				- So, lets find orthogonal projections $w_1, w_2$ 
					- of $e_1 = (1, 0)$ and $e_2=(0, 1)$ 
					- onto $W = \text{ span}\{1, 2\}$ 
				- If we denote $b = (1, 2)$ we get the following,
				- $$\begin{aligned}w_1 &= \cfrac{\langle e_1, b\rangle}{\langle b, b\rangle}b\\ &= \cfrac{1 \cdot 1 + 0 \cdot 2}{1 \cdot 1 + 2 \cdot 2}(1, 2)\\ &= (\frac{1}{5},\frac{2}{5})\\ &= \frac{1}{5}e_1 + \frac{2}{5}e_2\end{aligned}$$
				- and, $$\begin{aligned}w_2 &= \cfrac{\langle e_2, b\rangle}{\langle b, b\rangle}b\\ &= \cfrac{0 \cdot 1 + 1 \cdot 2}{1 \cdot 1 + 2 \cdot 2}(1, 2)\\ &= (\frac{2}{5},\frac{4}{5})\\ &= \frac{2}{5}e_1 + \frac{4}{5}e_2\end{aligned}$$
				- Now, by putting these coefficients of $w_1 = T(e_1) \text{ and } w_2 = T(e_2)$ 
					- along $e_1$ and $e_2$ 
					- as entries of its respective columns we get the matrix $[T]_\beta$ 
						- $$[T]_\beta=\begin{bmatrix}\cfrac{1}{5} & \cfrac{2}{5}\\ \cfrac{2}{5} & \cfrac{4}{5}\end{bmatrix}$$
						- 
		- Do the same for $V = \mathbb{R}^3$ and $W = \text{ span}(\{(1,\, 0,\, 1)\})$ 



3. For each matrices $A$ in Exercise 2 of section 6.5:
	1. Verify that $L_A$ posses a spectral decomposition.
	2. For each eigenvalue of $L_A$, 
		- Explicitly define the orthogonal projection on the corresponding eigenspace.
	3. Verify your results by using the spectral theorem.


4. Let $W$ be a finite-dimensional subspace of an inner product space $V$. 
	- Show that if $T$ is the orthogonal projection of $V$ on $W$, 
		- then $I-T$ is the orthogonal projection of $V$ on $W^\perp$ 


5. Let $T$ be a linear operator on a finite-dimensional inner product space $V$. 
	- (a). If $T$ is an orthogonal projection, 
		- prove that $\|T(x)\|\leq \|x\|$ for all $x \in V$ 
		- Give an example of a projection for which this inequality does not hold. 
		- What can be concluded about a projection for which the inequality is actually an equality for all $x \in V$?
	- (b). Suppose that $T$ is a projection such that $\|T(x) \leq \|x\|$ for all $x \in V$ 
		- prove that $T$ is an orthogonal projection. 


6. Let $T$ be a normal operator on a finite-dimensional inner product space.
	- Prove that $T$ is a projection, 
		- then, $T$ is also an orthogonal projection


7. Let $T$ be a normal vector operator on a finite-dimensional complex inner product space $V$. 
	- Use the spectral decomposition  of $T$ 
		- $\lambda_1\, T_1 + \lambda_2\, T_2 + \cdots + \lambda_k\, T_k$
	- to prove the following results. 
		- (a)
			- If $g$ is a polynomial, then 
				- $$g(T) = \sum_{i=1}^k \ g(\lambda_i)\, T_i$$
		- (b)
			- If $T^n = T_0$ for some $n$, 
				- then, $T = T_0$ 
		- (c)
			- Let $U$ be a linear operator on $V$
				- Then $U$ commutes with $T$ 
					- if and only if $U$ commutes with each $T_i$
		- (d)
			- There exists a normal vector operator $U$ on $V$ such that $U^2 = T$
		- (e)
			- $T$ is invertible if and only if, 
				- $\lambda_i \neq 0 \quad \text{ for }1\leq i \leq k$
		- (f)
			- $T$ is a projection if and only if,
				- every eigenvalue of $T$ is $1$ or $0$
		- (g)
			- $T = -T^*$ if and only if,
				- every $\lambda_i$ is an imaginary number.


8. Use *Corollary 1* of spectral theorem to show that
	- if $T$ is a normal operator on a complex finite-dimensional inner product space
	- and, $U$ is a linear operator that commutes with $T$
		- then, $U$ commutes with $T^*$ 


9. Referring to Exercise 20 of Section 6.5,
	- prove the following facts about a partial isometry $U$ 
		- (a). $U^*U$ is orthogonal projection on $W$ 
		- (b). $UU^*U = U$ 


10. *Simultaneous diagonalization* Let $U$ and $T$ be norm operators on a finite-dimensional complex inner product space $V$ such that $TU = UT$ 
	- Prove that there exists an orthonormal basis for $V$ 
		- consisting of vectors that are eigenvectors of both $T$and $U$ 
			- *Hint :* Use the hint of Exercise 14 of Section 6.4 along with Exercise 8.


11. Prove (3) of the spectral theorem (Theorem 6.25).
	- [Solution](https://goo.gl/utQ9Pb) 