# A change of basis

The SVD makes it possible for us to say that every matrix is diagonal - if only one uses the proper bases for the domain and range spaces.

Here is how the change of bases works. 
Any $b \in \mathbb{C}^{m}$ can be expanded in the basis of the [[4 Lecture#^ceb613 | left singular vector]] of $A$ (columns of $U$) 

And any $x \in \mathbb{C}^{n}$ can be expanded in the basis of [[4 Lecture#^c8bd95 | right singular vectors]] of $A$ (columns of $V$) 

The coordinate vectors for these expansions are 
$$b^{'}=U^{*}b,\quad x^{'}=V^{*}x$$

the relation $b = Ax$ can be expressed in terms of $b^{'}$and $x^{'}$ :
$$b = Ax \iff U^{*}b = U^{*}Ax = U^{*}U\Sigma V^{*}x \iff b^{'} = \Sigma x^{'}$$

when ever $b = Ax$ we have $b^{'} = \Sigma x^{'}$.
thus $A$ reduces to the diagonal matrix $\Sigma$
when the range is expressed in the basis of columns of $U$ 
and the domain is expressed in the basis of columns of $V$.

## **SVD vs. Eigenvalue Decomposition** 
diagonalizing a matrix and expressing it in terms of a new basis

A non defect square matrix $A$ can be expressed as a diagonal matrix of eigenvalues $\Delta$  
- if the range and domain are represemnte in a basis of eigenvectors.

If the columns of a matrix $X \in \mathbb{C}^{m\times m}$ 
- contains linearly independent eigenvectors of $A \in \mathbb{C}^{m\times m}$
- the *Eigenvalue Decomposition* of $A$ is 
- $$A = X\Delta x^{-1}$$
	- where $\Delta$ is an $m\times m$ diagomnal matrix whose entries are the eigenvalues of $A$.
	- This implies that if we define,  for $b, x \in\mathbb{C}^{m}$ satisfying $b=Ax$,
	- $$b^{'} = X^{-1}b, \quad x^{'} = X^{-1}x,$$
	- Then the newly expanded vectors $b^{'} \text{ and } x^{'}$ satsfies $b^{'} = \Delta x^{'}$ 

**Differences between SVD and Eigenvalue Decomposition**
- SVD uses two different bases (sets of left and right singular vectors)
	- Eigenvalue decomp uses use one (eigenvectors)
- SVD uses orthonormal bases, 
	- Eigenvalue decomp use a basis that is not generally orthogonal
- Not all matrices (even square ones) have an eigenvalue decomp
	- But all matrices (even rectangular) have a singular value decomposition

Eigenvalues are relevant to problems involving the behavior of iterated forms of $A$ 
- Such as matrix powers $A^{k}$ or exponentials $e^{tA}$ 
	- whereas singular vectors tend to be relevant to problems involving the behavior of $A$ itself, or its inverse.   

### **Matrix Properties via the SVD**

Aussume that $A$ has dimensions of $m\times n$. Let $p$ be the minimum of $m$ and $n$, let $r\leq p$ denote the number of nonzero singular values of $A$, and let $\langle x, y, \cdots, z \rangle$ denote the space spanned by the vectors $x, y, \cdots, z$ 

### **Theorem 5.1** 

#### The rank of $A$ is $r$, the number of non-zero singular values. 

*Proof*: The rank of $A$ diagonal matrix is equal to the number of its nonzero entries, and in the decomposition $A = U\Sigma V^{*}$ , $U$ and $V$ are of full rank. 

Therefore, $rank(A) = rank(\Sigma) = r$ 

### **Theorem 5.2** 
$$range(A) = \langle u_{1}, \cdots, u_{r} \rangle$$  and $$null(A) = \langle v_{r+1}, \cdots , v{n} \rangle$$ 

*Proof*: This is a consequence of the fact that $$range(\Sigma) = \langle e_{1}, \cdots e_{r}, \rangle \subseteq \mathbb{C}^{m}$$ 
and $$null(\Sigma) = \langle e_{r+1}, \cdots ,e_{n} \rangle \subseteq \mathbb{C}^{m}$$ 

### **Theorem 5.3** 
$$\|A\|_{2} = \sigma_{1} \text{ and } \|A\|_{f} = \sqrt{\sigma_{1}^{2}+\sigma_{2}^{2}+\cdots +\sigma_{r}^{2}}$$  
*Proof:* The first result was already establish in the proof of Theorem 4.1: Since$A=U\Sigma V^{*}$ with unitary $U$ and $V$, $\|A\|_{2} = \|\Sigma\|_{2} = max\{|\sigma_{j}|\} = \sigma_{1}$, by Theorem 3.1. For the second note that by Theorem 3.1 and the remark following, the Frobenius norm is invariant under unitary multiplication, so $\|A\|_{F} = \|\Sigma\|_{F}$, and by (3.16), this is given by the stated formula. 

### **Theorem 5.4**
The nonzero singular values of $A$ are the square roots of the nonzero eigenvalues of $A^{*}A$ or $AA^{*}$. (These matrices have the same nonzero eigenvalues.)


*Proof*:{};
From the calculation
$$A^{*}A=(U\Sigma V^{*})^{*}\,(U\Sigma V^{*}) = V\Sigma^{*}U^{*}U\Sigma V^{*} = V(\Sigma^{*}\Sigma)V^{*}$$  
we see that $A^{*}A$ is similar to $\Sigma^{*}\Sigma$ and hence has the same $n$ eigenvalues
The eigenvalues of the diagonal matrix $\Sigma^{*}\Sigma$ are $\sigma_{1}^{2}+\sigma_{2}^{2}+\cdots +\sigma_{p}^{2}$  with $n-p$ additional zero eigenvalues if $n>p$. A similar calculation applies to the $m$ eigenvalues of $A^{*}A$ 

### **Theorem 5.5**
If $A = A^{*}$, then the singular values of $A$ are the absolute values of the eigenvalues of $A$  



*Proof*: 
As is well known (Exercise 2.3), a hermitian matrix has a complete set of orthogonal eigenvectors, and all of the eigenvalues are real. An Equivalent statement is that (5.1) holds with $X$ equal to some unitary matrix $Q$ and $\Delta$ a real diagonal matrix. But then we can write 
$$
A = Q\Delta Q^{*} = Q|\Delta|\text{ sign }(\Delta)Q^{*},
$$
where, $|\Delta|$ and sign($\Delta$) denote the diagonal matricies whoseentries are the numbers $|\lambda_{j}|$ and sign($\lambda_{j}$), respectively.
- (we could equally have well put the factor sign($\Delta$) on the left of $|\Delta|$ instead of the right.)

Since sign$(\Delta)Q^{*}$  is a unitary whenever $Q$ is unitary (5.2) is an SVD of $A$, with the singular values equal to the diagonal entries of $|\Delta|$, $|\lambda_{j}|$
If desired, these number can be put into nonincreasing order by inserting suitable permutation matrices as factors in the left-hand unitary matrix (5.2), $Q$, and the right-hand unitary matrix sign$(\Delta)Q^{*}$. 


### **Theorem 5.6**
For $A\in \mathbb{C}^{m\times m}, \ |\text{ det }(A)| = \Pi_{i=1}^{m} \sigma_{i}$ 

*Proof*: 
The determinant of a product of square matrices is the product of the determinants of the factors. 
Furthernore, the determinant of a unitary matrix is always $1$ in absolute value; this follows from the formula $U^{*}U=I$ and the property $|det(A)| = |det(U\Sigma V^{*})| = |det(U)|\, |det(\Sigma)|\, |det(V^{*})| = |det(\Sigma)| = \Pi_{i=1}^{m}\sigma_{i}$ 

### Low Rank Approximations 

But what is the SVD?  
- consider how a matrix A might be represented as a sum of rank-one matrices.

#### **Theorem 5.7** 
- $A$ is the sum of $r$ rank-one matrices
$$\tag{5.3} A = \sum_{j=1}^{r}\sigma_{j}\,u_{j}\,v_{j}^{*}$$

*Proof :*
If we write $\Sigma$ as a sum of $r$ matrices $\Sigma_{j}$, where $\Sigma_{j} = diag(0, \cdots, 0, \sigma_{j}, \cdots, 0)$ then 5.3 follows from 4.3


Many ways to express a $m\times n$ matrix $A$ as a sum of rank-one matrices.
- For example, $A$ could be written as sum of its $m$ rows
	- or its $n$ columns
	- or its $mn$ entries
- Another example is, Gaussian elimination reduces $A$ to the sum of full, rank-one matrix, 
	- a rank-one matrix whose first row and column are zero,
	- a rank-one matrix whose first twi rows and columns are zero and so on.

 
 However *(5.3)* represents a decomposition into rank-one matrices with a deeper property
 - **The $v^{th}$ partial sum captures as much of the energy of $A$ as possible** 
	 - energy is defined as either 2-norm or the Frobenius norm 
We can make it precise by formulating a problem of best approximation of a matrix $A$ by matrices of lower rank.


#### **Theorem 5.8** 
- for ant $v$ with $0\leq v\leq r$, define 
$$\tag{5.4} A_{v} = \sum_{j=1}^{v}\sigma_{j}\,u_{j}\,v_{j}^{*}$$

if $v = min\{m, n\}$, define $\sigma_{v+1} = 0$
then 
$$\|A-A_{v}\|_{2} = inf \|A-B\|_{2} = \sigma_{v+1}$$

*Proof :*

### **Computation of SVD**
computing SVD can be done by variants of algorithms to calculate eigenvalues

best method for computing rank of a matrix is to count the number of singular values greater then a judiciously chosen tolerance (Theorem 5.1)

to find orthonormal basis of a range or null space is via Theorem 5.2

QR factorization provides alternative algorithms that are faster but not always accurate. 

Theorem 5.3 represents the standard method for computing $\|A\|_{2}$ 

theorem 5.8 and 5.9, the standards for computing low rank 
approximations with respect to $||\cdot||_{2}$ and $\|\cdot\|_{F}$ 

SVD is also ingredient in robust algos for 
- least squares fitting
- intersection of subspaces
- regularization

# **Exercises**

### **5.1**
In *Example 3.1* we considered the matrix *(3.7)* and asserted, among other things, that its 2-norm is approximately *2.9208*.
Using the SVD, work out (on paper) the exact values of $\sigma_{min}(A)$ and $\sigma_{max}(A)$ for this matrix. 

*Solution :*

### **5.2**
Using the SVD, prove that any matrix in $\mathbb{C}^{m\times n}$  **is the limit of a sequence of matrices of full rank**. 
In other words, **prove that the set of full-rank matrices is a dense subset of $\mathbb{C}^{m\times n}$ .**
Use the *2-norm* for your proof. 
(The norm doesn't matter, since al norms on a finite-dimensional space are equivalent.)

*Solution :*

### **5.3**
Consider the matrix 
$$A = \begin{bmatrix}-2 & 11\\ -10 & 5\end{bmatrix}$$

(a) Determine, a real SVD of $A$ in the form $A = U\Sigma V^T$ 
The SVD is not unique, so find the one has minimal number of minus signs in $U$ and $V$. 

*Solution :*

(b) List the singular values, left singular vectors, and right singular vectors of $A$.
Draw a careful labeled picture of the unit ball in $\mathbb{R}^2$ and its image under $A$, 
- together with the singular vectors, 
- with the coordinates of their vertices marked. 

*Solution :*

(c) What are the $1-, 2-, \infty -$, and Frobenius norms of $A$?


(d) Find $A^{-1}$ not directly but via SVD

(e) Find eigenvalues $\lambda_1, \lambda_2$ of $A$.


(f) Verify that $detA = \lambda_1 \, \lambda_2$ and $|detA| = \sigma_1 \, \sigma_2$ 

(g) What is the area of the ellipsoid onto which $A$ maps the unit ball of $\mathbb{R}^2$ 


### **5.4**
Suppose $A\in\mathbb{C}^{m\times m}$ has an SVD $A = U\Sigma V^*$.
Find an eigenvalue decomposition *(5.1)* of the $2m\times 2m$ hermitian matrix.
$$\begin{bmatrix}0 & A^*\\ A & 0\end{bmatrix}$$

*Solution :*