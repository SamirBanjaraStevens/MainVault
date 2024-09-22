The other method for computing QR factorizations
Numerically more stable than Gram-Schmidt or Orthogonalization
	(insensitivity to rounding number)
Lacks applicability as a basis for iterative methods
a process of "<u>Orthogonal Triangulation</u>", 
	Making a matrix triangular by a sequence of unitary matrix operations


# Householder and Gram-Schmidt
***
The Gram-Schmidt iteration applies a succession of elementary triangular matrices $R_k$ on the right of $A$
	so that the resulting matrix 
		$$\underbrace{A R_1 R_2 \cdots R_n}_{\hat{R}^{-1}} = \hat{Q}$$
			has orthonormal columns.

The product $\hat{R} = R_n^{-1} \cdots R_2^{-1} R_n^{-1}$ 
	is upper triangular
		and thus, $A = \hat{Q}\hat{R}$ is a reduced QR factorization of $A$

In contrast, 
	the Householder method applies 
		a succession of elementary unitary matrices $Q_k$ 
			on the left of $A$ 
				so that the resulting matrix 
					$$\underbrace{Q_n \cdots Q_2 Q_1 A}_{\hat{q}^{*}} = Q$$
						is upper-triangular

The product $Q = Q_n \cdots Q_2 Q_1$  
	is unitary 
		and thus, $A = QR$ is a full factorization of $A$ 

Summarized as follows :

- Gram-Schmidt : <u>triangular orthogonalization</u>
- Householder : <u>orthogonal triangulazation</u> 

# Triangularizing by Introducing Zeros
***
We are essitentaly design the unitary matrix $Q_k$ 
	so that $Q_n\cdots Q_2 Q_1$ 
		is upper-triangular

The matrix $Q_k$ 
	is chosen to introduce zeros below the diagonal 
		in the k-th column 
			while preserving all the zeros previously introduced

For example, 
	in $5\times 3$ 
		three operations $Q_k$ are applied.

In these matrices,
	the symbol $\times$ represents an entry that is not necessarily zero
		and bold facing indicates an entry that has just been changed.
			Blank entries are zero.

$$
\tag{10.1}
\underset{\huge A}{
\begin{bmatrix}
\times & \times & \times\\
\times & \times & \times\\
\times & \times & \times\\
\times & \times & \times\\
\times & \times & \times\\
\end{bmatrix}
}
\overset{Q_1}{\longrightarrow}
\underset{\huge Q_1 A}{
\begin{bmatrix}
\times & \times & \times\\
0 & \times & \times\\
0 & \times & \times\\
0 & \times & \times\\
0 & \times & \times\\
\end{bmatrix}
}
\overset{Q_2}{\longrightarrow}
\underset{\huge Q_2 Q_1 A}{
\begin{bmatrix}
\times & \times & \times\\
 & \times & \times\\
 & 0 & \times\\
 & 0 & \times\\
 & 0 & \times\\
\end{bmatrix}
}
\overset{Q_3}{\longrightarrow}
\underset{\huge Q_3 Q_2 Q_1 A}{
\begin{bmatrix}
\times & \times & \times\\
 & \times & \times\\
 &  & \times\\
 &  & 0\\
 &  & 0\\
\end{bmatrix}
}
$$
First, 
	$Q_1$ operates on rows $1, \dots, 5$  
		introducing zeros in position $(3,2), (4, 2), (5, 2)$ 
			but not destroying the zero introduced by $Q_1$

Finally, 
	$Q_3$ operates on rows $3, \dots, 5$ 
		introducing zeros in position $(4, 3), (5, 3)$
			without destroying any zeros introduced earlier

In general, 
	$Q_k$ operates on rows $k, \dots, m$

At the beginning of step $k$,
	there is a block of zeros in the first $k-1$ columns of these rows 

The application of $Q_k$ forms a linear combination of these rows, 
	and the linear combinations of the zero entries remain zero

After $n$ steps, 
	all the entries below the diagonal have been eliminated and $Q_n \cdots Q_1 Q_1 A = R$ is upper triangular

# Householder Reflectors
***
How do we construct unitary matrices $Q_k$ to introduce zeros as indicated in *10.1*?

Each $Q_k$ is chosen to be a unitary matrix of the form, 
$$\tag{10.2} Q_k = \begin{bmatrix}I & 0\\ 0 & F\end{bmatrix}$$
	where $I$ is the $(k-1) \times (k-1)$ identity and,
		$F$ is an $(m-k+1) \times (m-k+1)$ unitary matrix

Multiplication by $F$ must introduce zeros into the k-th column. 

The Householder algorithm chooses $F$ to be a 
	particular matrix, called the *Householder reflector*

![[Pasted image 20230323143158.png]]

Suppose, at the beginning of step $k$
	the entries $k, \dots, m$ of the k-th column
		are given by the vector $x \in \mathbb{C}^{m-k+1}$ 

To introduce the correct zeros into the k-th column,
	the house holder reflector $F$ should effect the following map:
$$
\tag{10.3}
x = 
\begin{bmatrix}
\times\\
\times\\
\times\\
\vdots\\
\times\\
\end{bmatrix}
\overset{F}{\longrightarrow}
\quad
Fx = 
\begin{bmatrix}
\|x\|\\
0\\
0\\
\vdots\\
0
\end{bmatrix}
= 
\|x\|e_1
$$

The reflector $F$ 
	will reflect the space $\mathbb{C}^{m-k+1}$ 
		across the hyperplane $H$ 
			orthogonal to $v=\|x\| e_1 -x$ 

***
*Note :* 

*hyperplane* is the higher dimensional generalization of a two-dimensional (subspace) plane in in a thee-space

can be characterized as the set of points orthogonal to a fixed non zero vector. 

In figure, *10.1* that vector is $v = \|x\| e_1 - x$ 
	think of the dashed line as a depiction of $H$ viewed "edge on"
***


When the reflector is applied,
	every point on one side of the hyper plane $H$ 
		is mapped 
			to its mirror image on the other side

In particular, 
	$x$ is mapped
		to $\|x\|e_1$ 

the formula for this reflection is below. 
In [[Projectors#^bf2070|6.11]] we have seen that for any $y \in \mathbb{C}^m$, the vector is the orthogonal projection of $y$ into the space $H$
To reflect $y$ across $H$, we must go twice as far in the same direction. 
The reflection $Fy$ should be,
$$Fy = \left(I - 2\cfrac{vv^*}{v^*v}\right)y = y-2v\left(\cfrac{v^*y}{v^*v}\right)$$
hence the matrix $F$ is,
$$\tag{10.4} F = I - 2\cfrac{vv^*}{v^*v}$$

*Note :* that the projector $P$ (rank $m-1$ ) and the reflector $F$(full rank, unitary) differ only in the presence of a factor $2$

![[Pasted image 20230323145914.png]]

# The Better of Two Reflectors 
***
In *(10.3)* and figure 10.1
we have simplified matters
there are many Householder reflections that will introduce the zeros needed. 
The vector $x$ can be reflected to $z\|x\|e_1$ 
	where $z$ is any scalar with $\|z\| = 1$ 

In the complex case, there are two alternatives,
	represented by refections across two diffrent hyper planes

$H^+$ and $H^-$ in figure 10.2

Mathematically,
	either choice of sign is satisfactory

However, 
	this is a case where the goal of numerical stability (insensitivity to rounding number)
		dictates that once choice should be taken rather than the other.

It is desirable to reflect $x$ to the vector $z\|x\|e_1$ that is not too close to $x$ itself.

To achieve this,
	we can choose $z = -\text{sign }(x_1)$ 
		where $x_1$ denotes the first component of $x$ 
			so that the reflection vector becomes $v = -\text{sign }(x_1)\|x\|e_1-x$ 
				or upon the clearing the factors $-1$
					$$\tag{10.5}v = \text{ sign }(x_1) \ \|x\| \ e_1 + x$$
we may arbitrarily impose the convention that $\text{sign}(x_1) = 1$ if $x_1 = 0$ 

It is not hard to see why the choice of sign makes a difference for stability

Suppose that in figure 10.2 
	the angle between $H^+$ and the $e_1$ axis is very small.

Then the vector $v = \|x\| \ e_1 - x$ 
	is much smaller 
		than $x$ or $\|x\| \ e_1$ 
			thus, the calculations of $v$ represents a subtraction of nearby quantities and will tend to suffer from cancellation errors.  

If we pick the sign as in *(10.5)* 
	we avoid such effects by ensuring that $\|v\|$  is never smaller than $\|x\|$ 

# The Algorithm
***
$\textbf{For } k = 1 \textbf{ to }n \textbf{ do:}$
- $x = A_{k:m, \ k}$ 
- $v_{k} = \text{ sign }(x_1) \ \|x\| \ e_1 + x$ 
- $v_k=\cfrac{v_k}{\|v_k\|_2}$ 
- $A_{k:m, \ k:n} = A_{k:m, \ k:n} - 2v_k(v_k^* A_{k:m, \ k:n})$ 

## Implicit calculation of a product $Q^{*}b$
***
sequence of n operations applied to $b$ the same operations that were applied to $A$ to make it triangular
***
$\textbf{For } k = 1 \textbf{ to } n \textbf{ do:}$
- $b_{k : m} = b_{k:m} - 2v_{k}(v_{k}^{*}b_{k:m})$ 


## Implicit calculation of a Product $Qx$
***
Computation of a product $Qx$ can be achieved by the same process in reverse order
***
$\textbf{For } k = n \textbf{ down to } 1 \textbf{ do:}$
- $x_{k:m} = x_{k:m} - 2v_{k}(v_{k}^{*}x_{k:m})$ 
