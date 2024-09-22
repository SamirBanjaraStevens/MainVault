## Definition and applications
 Let $A$ be a real $n \times n$ matrix
 We say that the $n \times n$ matrices $L$ and $U$ are an LU *factorization* of $A$
	 if, $L$ is a lower triangular (i.e., $L_{ij} = 0, i<j$) 
	 and, $U$ is upper triangular, (i.e., $U_{ij} = 0, i>j$)
	 and, $A = LU$

**Application 1:** Calculation of a determinant: 
$$\det(A) = (\det L)(\det U) = ()\Pi_{k=1}^{n}  \ L_{kk})\dot(\Pi_{k=1}^{n} \ U_{kk})$$

**Application 2:** Testing for nonsingularity: 
$A = LU$ is nonsingular $\iff$ (iff) all the diagonal elements of $L$ and $U$ are nonzero.

**Application 3:** Solution of linear systems:
Let $A = LU$ and suppose we wish to solve $Ax = b$ 
This is the same as $L(Ux) = b$,
Which decompose into 
- $Ly = b$
- $Ux = b$

Both latter systems are triangular and can be easily calculated.

Thus, $L_{1}y_{1} = b_{1}$ gives $y_{1}$
next, $L_{21}y_{1} + L_{22}y_{2} = b_{2}$ yields $b_{2}$ 

Having found $y$ we solve for $x$ by reversing the order:
$U_{nn}x_{n} = y_{n}$ gives $x_{n}$
$U_{(n-1)(n-1)}x_{(n-1)(n-1)}+U_{(n-1),n}x_{n} = y_{n-1}$ produces $x_{n-1}$ and so on.
This requires $\Omega(n^{2})$computationss operations

**Application 4:** The inverse of $A$:
Devise a direct way of calculating the inverse of triangular matrices subsequently forming $A^{-1} = U^{-1}L^{-1}$

## 1.2 The Calculation of LU Factorization

We denote the columns of $L$ by $l_{1}, l_{2}, \dots ,l_{n}$ 
and rows of $U$ by $u_{1}, u_{2}, \dots, u_{n}$, hence
$$\tag{1.1} A = LU = \left[\begin{array}{llll}
l_{1} & l_{2} & \dots & l_{n}
\end{array}\right]
\begin{bmatrix}
u_{1} \\ 
u_{2} \\ 
\vdots \\ 
u_{n}
\end{bmatrix}
= \sum_{k=1}^{n} \ l_{k}u_{k}
$$
Since the first $k-1$ components of $l_{k}$ and $u_{k}$ are all zero,
	Each rank-one matrix $l_{k}u_{k}$ has zeros in its first $k-1$ rows and columns

Assume that the factorization exists (hence the diagonal elements of $L$ are nonzero) 
	and that $A$ is nonsingular

Sincem $l_{k}u_{k}$ stays the same if we replace $l_{k}\mapsto \alpha l_{k}, \quad u_{k}\mapsto \alpha^{-1}u_{k}$ where $\alpha \neq 0$ 
we may aussumme w.l.o.g. that all disgonal elements of $L$ are equal to one.

In other words, 
the $k$-th row of $l_{k}u_{k}$ is $u_{k}$ and its $k$-th column is $U_{kk} \times l_{k}$ 

We begin our calculation by extracting $l_{1}$ and $u_{2}$ from $A$,
	and then proceed similarly to extract $l_{2}$ and $u_{2}$

*Note :* that since the leading $k-1$ elements of $l_{k}$ and $u_{k}$ are zero for $k\geq 2$, it follows from (1.1) that $u_{1}$ is the first row of $A$ and $l_{1}$ is the first column of $A$, divided by $A_{11}$ (so that $L_{11} = 1$)

Next, having found $l_{1}$ and $u_{1}$ 
form the matrix $A-l_{1}u_{1} = \sum_{k=2}^{n} \ l_{k}u_{k}$ 

The first row and column of $A$ are nonzero, and it follows that $u_{2}$ is the second row of $A-l_{1}u_{1}$ 
while $l_{2}$ is its second column scaled so that $L_{22} = 1$ 

#### The LU algorithm:
*** 
Set $A_{0} = A$ 
For all $k = 1, 2, \dots, n$ set $u_{k}$ to the $k$-th row of $A_{k-1}$ and $l_{k}$ to the $k$-th column of $A_{k-1}$, scaled so that $L_{kk} = 1$ 
Further calculate $A_{k} := A_{k-1}-l_{k}u_{k}$ before incrementing $k$

*Note :* All elements in the first $k$ rows and columns of $A_{k}$ are $0$ 

Hence, we can use the storage of $A$ to accumulate $L$ and $U$

The full factorization require $\Omega(n^{3})$ computational operations

## Relation to Gaussian-elimination

## Pivoting

# Factorization of Structured Matrices
***

## Symmetric Matrices

## Symmetric Positive Definite Matrices

## Sparce Matrices

# Iterative Methods for Linear Systems

## Basic iterative schemes

## Necessary and Sufficient Conditions for Convergence

# QR Factorization of Matrices

## Scalar Products, Norms, and Orthogonality


## The QR Factorization


## The Gram-Schmidt Algorithm

## Orthogonal Transformations

## Householder Transformations 

# Linear Least Squares

## Statements of the Problem

## Normal Equations

## QR and Least Square

# Polynomial Interpolation

# Orthogonal Polynomials

# The Peano kernel theorem
