
## Question 1 
Let $\|A\|_{m,n}=\text{sup}_{x\neq 0}\cfrac{\|A\|_{m}}{\|x\|_{n}}$ be the operator (induced) norm and let $\|A\|_{F} =\sqrt{  \left( \sum\mid a_{ij}\mid^{2}\right)}$ be the Frobenius norm of the matrix $A$.
We denote the transpose of the matrix by $A^{T}$ and the adjoint by $A^{*}$

**Show that:**

- (a) $\|A\|_{\infty}=\text{sup}_{x\neq 0}\cfrac{\|A\|_{\infty}}{\|x\|_{\infty}}=\text{max}_{i}\sum_{j}|a_{ij}|=\text{ maximum absolute row sum }$
	- 
- (b) $\|A\|_{1}=\text{sup}_{x\neq 0}\cfrac{\|A\|_{1}}{\|x\|_{1}}= \|A^{T}\|_{\infty} =\text{max}_{j}\sum_{i}|a_{ij}| =\text{ maximim absolute column sum }$
- (c) $\|A\|_{2}= \text{sup}_{x\neq 0}\cfrac{\|A\|_{2}}{\|x\|_{2}}=\sqrt{ \lambda_{max}(A^{*}A)}$, where $\lambda_{max}$ denotes the maximum eigenvalue.
	- 
- (d) $\|A\|_{2}=\sigma_{2}$ where $\sigma_{1}$ is the largest singular value of $A$ 
- (e) $\|A\|_{2}=\|A^{T}\|_{2}$
- (f) If $A$ is normal ($A^{*}=A^{*}A=I$), then$\|A\|_{2}=\text{max}_{i}\lambda_{i}(A)$ 
- (g) $\|QAZ\|=\|A\|$ if $Q$ and$Z$ are orthogonal (or unitary) for the Frobenius and the induced 2-norm
- (h) $\|A\|_{F}=\sqrt{ tr(A^{*}A) }=\sqrt{ tr(AA^{*}) }$
- (i) if $A$ is diaginal, then $\|A\|_{2}=\text{max}_{i} \ |a_{ii}|$

## Question 2

Let $A=\begin{bmatrix} 1 & 1\\ 1 & 1\end{bmatrix}$ 
- (a) Calculate the 2-norm of $A$ using the definition
- (b) Calcuate the Singular Value Decomposition of $A$ 

## Question 3

Let $A\in\mathbb{C}^{m\times m}$ be a square matrix with SVD $A = U\Sigma V^{*}$ and let $H = \begin{bmatrix}0 & A^{*}\\ A & 0\end{bmatrix}$ 

Show that the eigenvalues and eigenvectors of $H$ are $\pm \sigma_{i}$ and $\cfrac{1}{\sqrt{ 2 }}\left[\begin{array}{} u_{i}\\ \pm u_{i}\end{array}\right]$, where $\sigma_{i}$ are diagonal elements of $\Sigma$ and $u_{i}$ are columns of $U$ 

## Question 4

Let $A$ be an $m\times n$ matrix with distinct eigenvalues $\lambda_{1}, \dots, \lambda_{k}$ and their corresponding eigenspaces $E_{\lambda_{1}}, \dots, E_{\lambda_{1}}$ 
Let $\mathbb{B}_{i}$ be a basis for $E_{\lambda_{i}}$ 
Show that the set $\mathbb{B}=\mathbb{B}_{i}\cup \dots \cup \mathbb{B}_{k}$ is linearly independent

## Question 5

Let $A$ be an $m\times m$ Hermetian (self-adjoint) matrix ($A=A^{*}$) 
Show that:
- Eigenvalues of $A$ are real
- Eigenspaces corresponding to distinct eigencalues are orthogonal
- $A$ is non-defective
	- i.e., $A$ has $m$ lineraly independent eigenvectors. 
- Conclude that $A$ is orthogonally diagonalizable.

## Question 6

Show that if $A = A^{*}$, then singular values of $A$ are absolute value of eigen values of $A$ 

## Question 7

Let $A = \begin{bmatrix}2 & 1 & 0\\ 1 & 2 & 1\\ 0 & 1 & 2\end{bmatrix}$.
Is $A$ diagonalizable?

## Question 8

Let $P = P^{2}$ be a projection.
If $S_{1}=Range(P)$ and $S_{2}=Null(P)$, we say that $P$ is the projector onto $S_{1}$ along $S_{2}$ 
If $S_{1}$ and $S_{2}$ are orthognal $(S_{1}\perp S_{2})$, then $P$ is called an orthogonal projection,

**Show that:** 
- (a) $S_{1}\cup S_{2}=0$
- (b) $I-P$ is a projection.  $(I - P)$ is called the complementary projection
- (c) $Range(I-P)=Null(P)$
- (d) $P$ is orthogonal if and only if $P=P^{*}$
- (e) Let $q$ be a unit vector. Show that $P_{q}=qq^{*}$ is a rank 1 orthogonal projector. What can you say about $P_{\perp q}=I-qq^{*}$. Generalize this to arbitrary non unit (non-zero) vectors.
- (f) Let $Q$ be a unitary (orthonormal in real case) matrix ($Q^{*}Q=QQ^{*}=I$) with columns $\{ q_{q}, \dots, q_{n} \}$. Show that $P=QQ^{*}$ is the orthogonal projection onto the range of $Q$ 
- (g) For a given full rank matrix $A$, the orthogonal projection onto the $Range(A)$ is given by $P=A(A^{*}A)^{-1}A^{*}$ 
- (h) If $P$ is orthogonal, then $I-2P$ is unitary
- (i) $\|P\|_{2}\geq 1$ with equality if and only if $P$ is orthogonal.

## Question 9

Let $A$ an $m\times n$ full rank matrix with $m\geq n$ with columns $\{ a_{j} \}$. 
Orthogonal vectors produced by Gram-Schmidt can be written in terms of projections:
$$q_{1}=\cfrac{P_{1}a_{1}}{\|p_{1}a_{1}\|}, q_{2}=\cfrac{P_{2}a_{1}}{\|P_{2}a_{2}\|}, \dots ,q_{n}=\cfrac{P_{n}a_{n}}{\|P_{n}a_{n}\|}$$
where $P_{1}=I$ and $P_{j}$ for $j>1$ is the orthogonal projection into the space orthogonal to the range of $Q_{j-1}=[q_{1}\mid \dots \mid q_{j-1}]$

**Show that:**
- (a) $P_{j}=I-Q_{j-1}Q^{*}_{j-1}=P_{\perp q_{j-1}}\dots P_{\perp q_{2}}P_{\perp{q_{1}}}$ 
- (b) Calculate $v_{j}=P_{\perp q_{j-1}}\dots P_{\perp q_{2}}P_{\perp{q_{1}}}$
- (c) Explain why the Modified Gram-Schidmit is more stabel than Classic Gram-Schmidt
- (d) Let 
$$A=\begin{bmatrix}
1 & 1 & 1 \\ 
\epsilon & 0 & 0 \\ 
0 & \epsilon & 0 \\ 
0 & 0 & \epsilon
\end{bmatrix}$$
	Where $\epsilon$ is so small that $1+\epsilon =1$ within $4$ roundoff errors.
	Calculate $q_{2}^{T}q_{3}$ using both MGS and CGS. Describe observations

## Question 10

Show that $GS$ can be viewed as an orthogonal triangulization approach $AR_{1}\dots R_{n}=Q$ where $R_{i}$'s are triangular matrices
$$[v_{1}\mid \dots \mid v_{n}]=\begin{bmatrix}
\cfrac{1}{r_{ii}} & \cfrac{-r_{12}}{r_{11}} & \dots \\ 
& 1 & \\ 
& & 1 \\ 
& & & \ddots
\end{bmatrix}[q_{1}\mid v_{2}^{(2)} \mid\dots \mid v_{n}^{(2)} ]$$

Derive the recursions and write pseudo-code for the QR factorization using the GS.
Calcuate the complexity of the algorithim

## Question 11

Householder algorithm constructs a sequence of unitary matricies $Q_{k}$ so that $Q_{n}\dots Q_{2}Q_{1}A=R$ is upper triangular. Here
$$Q_{k}=\begin{bmatrix}
I & 0 \\ 
0 & F
\end{bmatrix}$$
where $I$ is $(k-1)\times(k-1)$ identity matrix and $F$ is an $(m-k+1)\times(m-k+1)$ unitary matrix that reflects the space $\mathbb{C}^{m-k+1}$ across the hyperplane $H$ orthogonal to $v= \|x\|e_{1}-x$ 

- (a) Describe the geometry of the Householder Algorithm
- (b) Derive a formula for the Householder reflector $F (F=I-2\cfrac{vv^{*}}{v^{*}v})$
- (c) Write the psuedo-code of the Householder QR factorization. What is the algorithm complexity?










