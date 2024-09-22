Matrix Inverse
Let $A$ be an $n\times n$ matrix.
Then, $A$ is invertible if there exists an $n\times n$ matrix $B$ such that $AB = BA = I_n$ 

Equivalent statements: (fundamental theorem of invertible matrices)
1. $A$ has an inverse of $A^{-1}$ 
2. $\text{rank}(A) = n$ (full rank)
3. $\text{range}(A) = \mathbb{C}^n$ 
4. $\text{null}(A) = \{0\}$ (corresponding homogenous has a trivial solution)
5. $0$ is not an eigenvalue of $A$
6. $0$ is not an singular value of $A$

to calculate the inverse of a matrix, perform elementary row operations, (or find the product of the elementary matrix and augmented matrix), on the augmented matrix:
$$C = (A|I_n)$$ to get $$A^{-1}\,C = (I_n|A^{-1})$$
Let $A$ be the given matrix of size $n\times n$


What is matrix multiplication?

a system of linear equations can be represented as such,
$$A\vec{x}=\vec{b}$$
$A$ -$m\times n$ matrix (coefficient matrix of the system)(lienar map)
$\vec{x}$ - solution (vector) we are trying to find, $n \times 1$ matrix
$\vec{b}$ $m\times 1$ matrix

thus the system $A\vec{x}=\vec{b}$ can be represented as such
$$
\begin{bmatrix}
a_{11}& \cdots & a_{1n} \\
\vdots & \ddots & \vdots\\
a_{m_1} & \cdots & a_{mn}
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
=
\begin{bmatrix}
a_{11}x_1 + \cdots + a_{1n}x_n\\
\vdots\\
a_{m1}x_1+ \cdots + a_{mn}x_n
\end{bmatrix}
$$the product of two matrices can be defined as a linear operator where the linear map $A$ maps the column vector $x$ to get the matrix product which is vector $\vec{b}$ 

linear map $A$ from a vector space of dimension $n$ into vector space of dimension $m$ maps a column vector $\vec{x}$ onto matrix product $\vec{b}$


taking dot product from row $i$ of $A$ and column  $j$ of $\vec{b}$ which it corresponds to the $i$ and $j$ th element of the matrix product $\vec{b}$ 