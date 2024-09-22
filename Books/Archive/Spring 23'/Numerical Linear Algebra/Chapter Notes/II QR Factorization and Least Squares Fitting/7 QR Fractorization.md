Reduced QR Factorization
#### **Gram-Schmidt Orthogonalization** 

given $a_1,a_2,\cdots,$ 
we can construct vectors $q_1, q_2, \cdots,$ 
and entries$r_{ij}$ 
by a process of successive orthogonalization

The process work like this.
At the $j^{th}$ step, we wish to find a unit vector $q_j \in \langle a_1, \cdots, a_j\rangle$ orthogonal to $q_1,\cdots,q_{j-1}$ 
- we have already considered the necessary orthogonalization technique in 2.6
From that equation, we see that 
$$\tag{7.5} v_j = a_j-(q_1^*a_j)q_1-(q_2^*a_j)q_2-\cdots - q_{j-1}^*a_j)q_{j-1}$$
is a un normalized vector of the kind we need ^8bf6ff 

If we divide by $\|v_j\|_2$ the result is a suitable+
vector $q_j$ 

$$
\tag{7.6}
\begin{align}
q_1 &= \frac{a_{1}}{r_{11}}\\
q_2 &= \frac{a_{2}-r_{12}q_{1}}{r_{22}}\\
q_3 &= \frac{a_{3}-r_{13}\,q_{1}-r_{23}q_{2}}{r_{33}}\\
&\vdots\\
q_n &= \frac{a_n-\sum_{i=1}^{n-1}\,r_{in}\,q_i}{r_{nn}}
\end{align}
$$

^afd740

definitions for coefficients $r_{ij}$ 
$$\tag{7.7} r_{ij} = q_i^{*}a_j\quad (i\neq j)$$$$\tag{7.8} |r_{jj}| = \left \|a_j-\sum_{i=1}^{j-1}r_{ij}q_{i}\right\|_{2}$$ ^d787d5
- Note: sign of $r_{jj}$ is not determined.
- Arbitrarily, we may choose $r_{jj} > 0$ ,
- in which case, we finish with a factorization $A=\hat{Q}\hat{R}$ in which $\hat{R}$ has positive entries along the diagonal. 

### **Theorem 7.1**

^7f5652

- Every $A\in \mathbb{C}^{m\times n}\, (m\geq n)$ has a full QR factorization, hence also a reduced QR factorization. 

*Proof :*
Suppose first that $A$ has full rank and that we want just a reduced QR factorization. 
In this case, a proof of existence is provided by the Gram-Schmidt algorithm. 
By construction, this process generates orthonormal columns of $\hat{Q}$ and entries of $\hat{R}$ such that (7.4) holds.
Failure can occur only if at some step, $v_j$ is zero and thus cannot be normalized to produce $q_j$ .
However, this would imply $a_j\in \langle q_1,\cdots , q_{j-1}\rangle = \langle a_1,\cdots , a_{j-1}\rangle$,  contradicting the assumption that $A$ has full rank. 

Suppose that $A$ does not have full rank. Then at one or more steps $j$, we shall find that (7.5) gives $v_j = 0$.
Pick $q_j$ arbitrarily to be any normalized vector orthogonal to $\langle q_1,\cdots , q_{j-1}\rangle$ and then continue the Gram-Schmidt process.

Finally, the full, QR Factorization of an $m\times n$ matrix with $m>n$ can be constructed using arbitrary orthonormal vectors in the same way. 
Follow G-S process through step $n$, 
- then continue additional $m-n$ steps, 
- introducing $q_j$ at each step.

Now we turn to **Uniqueness**.

Suppose$A=\hat{Q}\hat{R}$ is a reduced QR Factorization. 
If the $i^{th}$ column of $\hat{Q}$ is multiplied by $z$ 
and the $i^{th}$ row of $\hat{R}$ is multiplied by $z^{-1} 
for some scalar $z$ with $|z| = 1$,
we obtain another QR factorization of $A$. 
The next theorem asserts that if $A$ has *full rank* 
- this is the only way to obtain distinct reduced QR factorizations.

### **Theorem 7.2**
Each $A\in\mathbb{C}^{m\times m}$ of full rank has a unique reduced QR factorization $A=\hat{Q}\hat{R}$ with $r_{ij} > 0$ 

*Proof :*
Provided by Gram-Schmidt iteration.
From (7.4), the orthonormality of the columns of $\hat{Q}$,
and the upper-triangularity of$\hat{R}$,
- it follows that any reduced QR factorization of $A$ must satisfy *(7.6)-(7.8)*
By the assumption of full rank,
- the denominators *(7.8)* of *(7.6)* are nonzero 
	- and thus at each successive step $j$, 
		- these formulas determine $r_{ij}$ 
		- and $q_j$fully,
		- except the sign of $r_{ij}$ 
	- once this is fixed by the condition $r_{ij} > 0$ as in algo *7.1*, the factorization is determined. 

## **When Vectors Become continuous Functions**
*** 


The QR factorization has an analogue for orthonormal expansion of functions **rather** than 

Suppose we replace $\mathbb{C}^{m}$ by $L^2[-1,1]$ , 
- a vector space of complex valued functions on $[-1,1]$ .
Inner product of $f$ and $g$ are now:
- $$\tag{7.9} (f, g) =\int_{-1}^1\overline{f(x)}g(x)dx$$

Consider the "*matrix*" whose "*columns*"  are the monomials $x_{j}$ 
$$
\tag{7.10}
A=
\begin{bmatrix}
1 & | & x & | & x^2 & | & \cdots & | & x^{n-1}\\ 
\end{bmatrix}
$$
each column if a function in $L^2[-1,1]$, 
- and thus, whereas $A$ is discrete in the horizontal direction., 
- and continuous in vertical direction.
- It is a continuous analogue of the Vandermonde matrix (1.4) of Example 1.1.

The **"continuous QR factorization"** of $A$ takes the form 

$$
A = QR =

\left[
\begin{array}{c|c|c|c}
 & & &\\
q_0(x) & q_1(x) & \cdots & q_{n-1}(x)\\
 & & &
\end{array}
\right]
\begin{bmatrix}
r_{11} & r_{12} & \cdots & r_{1n}\\
 & r_{22} & & \vdots\\
 & & \ddots &\\
 & & & r_{nn}
\end{bmatrix},
$$

where columns of $Q$ are functions of $x$,
- orthonormal with respect to the inner product (7.9):
$$
\int_{-1}^1\overline{q_i(x)}q_j(x)\,dx = \delta_{ij} = 
\left\{
\begin{array}{ll}
      1, & \mbox{if $i=j$},\\
      0, & \mbox{if $i\neq j$}.
    \end{array}
  \right.
$$
$q_j$ is a polynomial with degree $j$ 
- the polynomials  are scalar multiples of Legendre polynomials, $P_j$, 
- which are conventionally normalized so that  $P_{j}(1) = 1$
- The first few $P_j$ are,
$$
\tag{7.11}
P_0(x) = 1,\quad P_1(x) = x,\quad P_2(x) = \frac{3}{2}x^2-\frac{1}{2},\quad P_3(x) = \frac{5}{2}x^3-\frac{3}{2}x
$$
like the monomials $1, x, x^2, \cdots,$ 
- this sequence of polynomials **spans** the spaces of polynomials **of successively higher degree**. 
However.
- $P_0(x), P_1(x), P_2(x),\cdots$ 
	- are **orthogonal**
		- computations with such polynomials form the basis of **spectral methods** (technique for the numerical solution of partial differential equations)

what is the "**Projection Matrix**" $\hat{Q}\hat{Q^*}$ **(6.6)** associated with $\hat{Q}$?
- it is a "$[-1,1] \times [-1,1]$ matrix"
	- that is, an integral operator mapping function in $L^2[-1,1]$ to functions in $L^2[-1,1]$ 
$$
\tag{7.12}
f(x) \mapsto \sum_{j=0}^{n-1} q_j(\cdot)\, \int_{-1}^1 \overline{q_j(x)}f(x)dx
$$

![[Pasted image 20230223065623.png]]

### **Solution of $Ax=b$  by QR Factorization**

Suppose we wish to solve $Ax=b$ for $x$, where $A\in\mathbb{C}^{m\times m}$ is nonsingular. 
If $A=QR$ is a QR factorization, 
- then we can write $QRx=b$ or 
$$\tag{7.13} Rx = Q^*b$$
The **RHS** of this equation is easy to compute,
- if $Q$ is known.
and the system of linear equations implicit in the **LHS** is also easy to solve,
- because it is triangular.

Method for computing the solution to $Ax = b$ 
1. Compute a QR factorization $A = QR$
2. Compute $y = Q^*b$
3. Solve $Rx = y$ for $x$



# **Exercises**

### **7.1**
Consider again the matrices $A$ and $B$ of Exercise 6.4

(a) Using any method you like, **determine a reduced QR factorization** $A=\hat{Q}\hat{R}$ and a **full factorization** $A = QR$

*Solution :*

- **Reduced QR Factorization**
$r_{11} = \|a_1\|_{2} = \sqrt{2},$ 
$r_{12} = q_1^*\,a_2 = 0,$ 
$r_{22} = \|a_2-r_{12} \ q_1\|_2 = 1,$ 
$q_1 = \cfrac{a_1}{r_{11}} = \cfrac{\sqrt{2}}{2}\begin{bmatrix}1\\ 0\\ 1\end{bmatrix}$ 
$q_2 = \cfrac{a_2-r_{12}q_1}{r_{22}} = a_2 = \begin{bmatrix}0\\ 1\\ 0\end{bmatrix}$
$$A = q_1\,q_2 =
\begin{bmatrix}
1 & 0\\
0 & 1\\
1 & 0
\end{bmatrix}
= 
\begin{bmatrix}
\cfrac{\sqrt{2}}{2} & 0\\
0 & 1\\
\cfrac{\sqrt{2}}{2} & 0
\end{bmatrix}
\begin{bmatrix}
\sqrt{2} & 0\\
0 & 1
\end{bmatrix}
$$
(b)Determine reduced and full QR factorization of $B= \hat{Q}\hat{R}$

*Solution :*

### **7.2**
Let $A$ be a matrix with the property that columns $1, 3, 5, 7,\cdots$ are orthogonal to columns $2, 4, 6, 8,\cdots$
In a reducedQR factorization $A=\hat{Q}\hat{R}$, what special structure does $R$ possess?

*Solution :*

### **7.3**
Let $A$ be an $m\times m$ matrix, and let $a_j$ be it's $j^{th}$ column.
Give an algebraic proof of Hadamard's inequality.
$$|det\,A| = \Pi_{j=1}^m \|a_j\|_2$$
Also give and geometric interpretation of this result,
making use of the fact that the determinant equals the volume of the parallelepiped.

*Solution :*

### **7.4**
Let $x^{(1)}, y^{(1)}, x^{(2)}, \text{ and } y^{(2)}$ be nonzero vectors in $\mathbb{R}^3$ with the property that $x^{(1)}$ and $y^{(1)}$ are linearly independent and so are $x^{(2)}$ and $y^{(2)}$ .
Consider the two planes in $\mathbb{R}^3$ ,
$$
P^{(1)} = \left\langle x^{(1)}, y^{(1)}\right\rangle, \quad
P^{(2)} = \left\langle x^{(2)}, y^{(2)}\right\rangle
$$
Suppose we wish to find a nonzero vector $v\in\mathbb{R}^3$ that lies in thee intersection $P = P^{(1)}\cap P^{(2)}$.
Devise a method for solving this problem by reducing it to the computation of QR factorizations of three $3\times 2$ matrices.

*Solution :*

### **7.5**
Let $A$ be an $m\times n$ matrix $(m\geq n)$, 
and let $A = \hat{Q}\hat{R}$ be a reduced QR factorization.
(a) Show that $A$ has rank $n$ if and only if all the diagonal entries of $\hat{R}$ are nonzero 

*Solution :*

(b) Suppose $\mathbb{R}$ has $k$ nonzero diagonal entries from some $k$ with $0\leq k\leq n$ .
What does  this imply about the rank of $A$? Exactly $k$? At least $k$?
At most $k$? 
Give a precise answer, and prove it. 

*Solution :* 
 

