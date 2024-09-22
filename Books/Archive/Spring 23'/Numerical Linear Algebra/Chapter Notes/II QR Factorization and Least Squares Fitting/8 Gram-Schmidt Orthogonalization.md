The Gram-Schmidt iteration is the basis of one of the two principal numerical algorithms for computing QR factorizations. 

It is a process of "triangular orthogonalization," making the columns of a matrix orthonormal via a sequence of matrix operations that can be interpreted as multiplication on the right by upper triangular matrices.

### **Gram-Schmidt Projections**

Let $A\in \mathbb{C}^{m\times n}, m\geq n$ be a matrix of full rank with columns $\{a_j\}$.
Consider sequence of formulas
$$
\tag{8.1}
q_1 = \cfrac{P_1a_1}{\|P_1a_1\|}, \quad q_2=\cfrac{P_2a_2}{\|P_2a_2\|}, \cdots,\quad q_n= \cfrac{P_na_n}{\|P_na_n\|},
$$
- Each $P_j$ denotes an orthogonal projector.
	- Specifically,$P_j$ is the $m\times m$ matrix of $rank = m -(j-1)$ that projects $\mathbb{C}^{m}$ orthogonally into the space orthogonal to $\langle q_1, \cdots, q_{j-1}\rangle$ 
		- In the case ($j=1$ this prescription reduces to the identity : $P_1 = I$ )
	- Now, 
	- observe that $q_j$ as defined by *(8.1)* is orthogonal to $q_1, \cdots, q_{j-1}$, 
	- lies in the space  $\langle a_1, \cdots, a_{j}\rangle$
	- and has norm $1$ 
Thus we see that *(8.1)* is equivalent to [[7 QR Fractorization#^afd740|7.6]]  - [[7 QR Fractorization#^d787d5|7.7]] - [[7 QR Fractorization#^d787d5|7.8]] 
and hence to Algorithm 7.1. 

The projector $P_j$ can be represented explicitly.
Let $\hat{Q}_{j-1}$ denote the $m\times (j-1)$ matrix containing the first $j-1$ columns of $\hat{Q}$ 
$$
\tag{8.2}
\hat{Q}_{j-1} =
\left[
\begin{array}{c|c|c|c}
& & &\\
q_1  & q_1  & \cdots  & q_{j-1}\\
& & & 
\end{array}
\right]
$$

then $P_j$ is given by 
$$
\tag{8.3}
P_j = I - \hat{Q}_{j-1}\, \hat{Q^*}_{j-1}
$$

*(8.3)* represents the operator applied to $a_j$ in [[7 QR Fractorization#^8bf6ff|(7.5)]]  


# Algorithm 8.1 Modified Gram-Schmidt

```
for i = 1 to n
	v_i = a_i
for i = 1 to n 
	r_ii = ||v_i||
	q_i = (v_i)/(r_ii)
	for j = i + 1 to n 
		r_ij = (q_i^*) (v_j)
		v_j = (v_j) - (r_ij)(q_i)
```




# Gram-Schmidt as Triangular Orthogonalization
***
Each outer step of the modified Gram-Schmidt algorithm can be interpreted
	as a right-multiplication by a square upper-triangular matrix.

For example, beginning with $A$
	the first iteration multiplies from each of the remaining columns $a_j$ 

This is equivalent to the right-multiplication by a matrix $R_1$ :

$$
\left[
\begin{array}{c|c|c|c}
 & & &\\
v_1 & v_2 & \cdots & v_n\\
 & & &
\end{array}
\right]

\begin{bmatrix}
\cfrac{1}{r_{11}} & \cfrac{-r_{12}}{r_{11}} & \cfrac{-r_{13}}{r_{11}} & \cdots\\
& 1 & & \\
&  & 1 & \\
&  & & \ddots \\
\end{bmatrix}

=

\left[
\begin{array}{c|c|c|c}
& & &\\
q_1  & v_1^{(2)}  & \cdots  & v_{n}^{(2)}\\
& & & 
\end{array}
\right]
$$

In general,
	step $i$ of algorithm *8.1* 
		subtracts $\cfrac{r_{ij}}{r{ii}}$ times column $i$ of the current $A$ from columns $j > i$ 
			and replaces column $i$ by $1/r_{ii}$ times itself

this corresponds to multiplication by an upper-triangular matrix $R_i$


$$
R_2 = 
\begin{bmatrix}
1 &  &  & \\
& \cfrac{1}{r_{22}} & \cfrac{-r_{23}}{r_{22}} & \cdots \\
&  & 1 & \\
&  & & \ddots \\
\end{bmatrix}
,

\quad 
R_3 = 
\begin{bmatrix}
1 &  &  & \\
& 1 & & \\
&  & \cfrac{1}{r_{33}} &\cdots \\
&  & & \ddots \\
\end{bmatrix}
,
\quad
\cdots
$$

at the end of the iteration we have 

$$\tag{8.10} \underbrace{A R_1 R_2 \cdots R_n}_{\huge\hat{R}^{-1}}= \hat{Q}$$

this formulation demonstrates 
	that the Gram-Schmidt Algorithm 
		is a method of *triangular orthogonalization*

It applies triangular operations 
	on the right of a matrix 
		to reduce it 
			to a matrix with orthonormal columns

if practice, 
	we do not form the matrices $R_i$ 
		and multiply them **explicitly**


# Exercises

### 8.1
***
Let $A$ be an $m \times m$ matrix.
Determine the exact number of floating point additions, subtractions, multiplications, and divisons
	involved in computing the factorization 
		$A = \hat{Q}\hat{R}$ 
			by algorithm *8.1* 

### 8.2
***
Write R code that computes reduced QR factorization $A = \hat{Q}\hat{R}$ of an $m\times m$ matrix $A$ with $m\leq n$ using modified Gram-Schmidt orthogonalization. 

The output is 
- $Q \in \mathbb{C}^{m\times n}$ with orthonormal columns 
- $R \in \mathbb{C}^{n\times n}$ triangular matrix

### 8.3
***
Each upper-triangular matrix $R_i$ of *p.61* can be interpreted as the product of a diagonal matrix and a unit upper-triangular matrix (i.e., an upper-triangular matrix with 1 on the diagonal). 

Explain exactly what these factors are, and which line of Algo *8.1* corresponds to each.