# LU Factorization
***
Gaussian Elimination transforms a full linear system into an upper-triangular linear system
- By applying simple linear transformations on the left

In this respect it is analogous to Householder triangularization for computing QR factorizations

The diffrence is that the transformations apllied in gaussian elimination are not unitary.
- So the transformation applied in the Householder Method is unitary.

Let $A \in \mathbb{C}^{m\times m}$ be a square matrix. 
- (The algo can also be applied to rectuanglar matricies too)

The idea is to transform $A$ into an $m \times m$ upper triangular matric $U$ by introducing zeros below the diagonal,
- First in column 1
	- then column 2
		- and so and so forth
(Just as in Householder)

This is done by subtracting multiples of each row from subsequent rows.

This "elimination" process is equivalent to multiplying $A$ by a sequence of lower triangular matricies on the left;
$$
\tag{20.1}
\underbrace{L_{m-1} \cdots L_{2} L_{1}A}_{L^{-1}} = U
$$
Setting $L = L_1^{-1}L_{2^{-1}} \cdots L_{m-1}^{-1}$ gives $A = LU$
thus we obtain an *LU Factorizationon* of A
$$\tag{20.2} A= LU$$

$U$ - Upper Triangular
$L$ - Unit lower-Triangular, 
- (all of the diagonal entries are equal to 1)

$$
\begin{aligned}
\textbf{Gram-Scmidt: } A &= QR \textbf{ by triangular orthogonalization}\\
\textbf{Householder: } A &= QR \textbf{ by oethogonal triangularization}\\
\textbf{Gaussian Elimination: } A &= LU \textbf{ by triangular triangularization}
\end{aligned}
$$

## Example 
***
Suppose we start with a $4 \times 4$ matrix
$$
A =
\begin{bmatrix}
2 & 1 & 1 & 0 \\
4 & 3 & 3 & 1 \\ 
8 & 7 & 9 & 5 \\ 
6 & 7 & 9 & 8 
\end{bmatrix} 
$$

The first step of Gaussian Elimination looks like this:
$$
L_{1} A = 
\begin{bmatrix}
1 & & & \\ 
-2 & 1 & & \\ 
-4& & 1 & \\ 
-3& & & 1
\end{bmatrix}
\begin{bmatrix}
2 & 1 & 1 & 0 \\
4 & 3 & 3 & 1 \\ 
8 & 7 & 9 & 5 \\ 
6 & 7 & 9 & 8 
\end{bmatrix} 
=
\begin{bmatrix}
2 & 1 & 1 & 0 \\ 
& 1 & 1 & 1 \\ 
& 3 & 5 & 5 \\ 
& 4 & 6 & 8
\end{bmatrix}
$$
In words we have subtracted the first row from  the second, 
four times the first row from the third
and  threetimes the firdt row from the fourth

Continue the steps for each column


Thus
$$
\begin{bmatrix}
2 & 1 & 1 & 0 \\
4 & 3 & 3 & 1 \\ 
8 & 7 & 9 & 5 \\ 
6 & 7 & 9 & 8 
\end{bmatrix}_{A}
=
\begin{bmatrix}
1 & & &  \\ 
2 & 1 & &  \\ 
4 & 3 & 1 &  \\ 
3 & 4 & 1 & 1
\end{bmatrix}_{L}
\begin{bmatrix}
2 & 1 & 1 & 0  \\ 
& 1 & 1 & 1 \\ 
& & 2 &2 \\ 
& & &2
\end{bmatrix}_{U}
$$

## General Formulas and Two Strokes of Luck
***
Here are general formulas for an $m \times m$ matrix.
Suppose $x_{k}$ denotes the $k$-th column of the matrix at beginning of step $k$:
Then the transformation $L_{k}$ must be chosen so that that the $k$-th column
$$
x_{k}
= 
\begin{bmatrix}
x_{1k} \\
\vdots \\ 
x_{kk} \\ 
x_{k+1, k} \\ 
\vdots \\ 
x_{mk}
\end{bmatrix}
\overset{L_{k}}{\mapsto}
L_{k}x_{k} = 
\begin{bmatrix}
x_{1k} \\ 
\vdots \\ 
x_{kk} \\ 
0 \\ 
\vdots \\ 
0
\end{bmatrix}
$$
To do this we wish to subtrack $\mathcal{l}_{jk}$ times row $k$ from row $j$ where $l_{jk}$ is the multiplier
$$
\tag{20.6}
l_{jk} = \cfrac{x_{jk}}{x_{kk}} \quad (k<j\leq m)
$$
the matrix $L_{k}$ takes form 
$$
L_{k}
\begin{bmatrix}
1 & & & & & \\ 
& \ddots & & & & \\ 
& & 1 & & & \\ 
& & -1l_{k+1, k} & 1 & & \\ 
& & \vdots & & \ddots & \\ 
& & l_{mk} & & &1
\end{bmatrix}
$$
with the nonzero subdiagonal entries situated in column $k$.

This is analogus to (10.2) for the Householder triangularization 

- $L_{k}$ can be inverted by negating its subdiagonal emties (20.4) 
- and that $L$ can be formed by collecting the entires $l_{jk}$ in the appropriate places (20.5)

Lets explain, 

>$L_{k}$ can be inverted by negating its subdiagonal emties

define $l_{k}$
$$
l_{k} = 
\begin{bmatrix}
0 \\ 
\vdots \\ 
l_{k+1, k} \\ 
\vdots \\ 
l_{m, k}
\end{bmatrix}
$$
Then $L_{k}$ can be written $L_{k} = I - l_{k}e^{*}_{k}$ 
- where $e_{k}$ is the column vector with 1 in position $k$ and $0$ elsewhere

The sparsity pattern of $l_{k}$ implies $e_{k}^{*}l_{k} = 0$
- and therfore $(I - l_{k}e_{k}^{*})(I+l_{k}e_{k}^{*}) = I-l_{k}e_{k}^{*}l_{k}e_{k}^{*} = I$
	- in other words, the inverse of $L_{k}$ is $I+l_{k}e_{k}^{*}$ as in (20.4)

>$L$ can be formed by collecting the entires $l_{jk}$ in the appropriate places

Consider the product $L_{k}^{-1}L_{k+1}^{-1}$
From the sparsity pattern of $l_{k+1}$, 
	we have $e_{k}^{*}l_{k+1} = 0$
		and therfore,
			$L_{k}^{-1}L_{k+1}^{-1} = (I+l_{k}e_{k}^{*})(I+l_{k+1}e_{k+1}^{*}) = I + l_{k}e_{l}^{*}+l_{k+1}e_{k+1}^{*}$
Thus $L_{k}^{-1}L_{k+1}^{-1}$ is just the unit lower triangular matrix with the entires of both $L_{k}^{-1}$ and $L_{k+1}^{-1}$ inserted in their usual places below the diagonal.

when we take the profuct of all these matricies to from $L$ 
	we have the same conveient property everywhere below the diagonal:
		$$\tag{20.7}L = L_{1}^{-1}L_{2}^{-1}\cdots L_{m-1}^{-1} = \begin{bmatrix}
1& & & & \\ 
l_{21} & 1 & & & \\ 
l_{31} & l_{32} & 1 & & \\ 
\vdots & \vdots & \ddots & \ddots & \\ 
l_{m1} & l_{m2} & \dots & l_{m, m-1} & 1
\end{bmatrix}$$

## Solution of $Ax = b$ by LU Factorization
***
(solving linear system of equations with LU factorization)

If $A$ is factored into $L$ and $U$, a system of equations $Ax = b$ is reduced to the form $LUx = b$

Thus, it can be solved by solving two triangular systems:
- First $Ly = b$ for the unknown $y$ (fordward substitution)
- then, $Rx = y$ for the unknown $x$ (back substitution)

<u>why is Gaussian-Elimination used rather than QR factorizationto solve square systems of equations?</u>

- The factor of 2
- (histiricoal stupid resons)

## Instability of Gaussian Elimination w/o Pivoting
***
Not backward stable
- and attempts division by zero

degree of rounding will get to large
- when we attempt to compute the product $\hat{L}\hat{U}$

