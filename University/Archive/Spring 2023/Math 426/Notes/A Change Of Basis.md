## **I. Coordinates**

Let $V$ be a vector space with basis $\beta = \{\vec{v}_1, \cdots , \vec{v}_n\}$  
- Every element $\vec{x}$ can be written *uniquely*  as a linear combination of the basis elements:
$$\vec{x} = a_1\vec{v}_1 + a_2\vec{v}_2+\cdots +a_n\vec{v}_n$$
**Coordinate Column Vector of $\vec{x}$ with respect to the basis $\beta$ :**
- The scalars $a_i$  recored in a column vector 
$$[\vec{x}]=\begin{bmatrix}a_1\\ a_2\\ \vdots\\a_n\end{bmatrix}$$
- *$\beta$-coordinate* of $\vec{x}$

Every vector $\vec{x}$ correspond to *exactly one* such column vector in $\mathbb{R}^n$ and 
vice-versa.
- the vector space $V$ with the more familiar space  $\mathbb{R}^n$ 

### **Example 1:**
- The vector space $\mathcal{P}_2$ of polynomials of degree $\leq 2$ consists of all expression of the form $a+bx+cx^2$ . 
- Here the choice of basis $\{1, x, x^2\}$ gives an isomorphism identifying $\mathcal{P}_2$ with $\mathbb{R}^3$.
$$\mathcal{P}_2 \rightarrow \mathbb{R}^3 \quad a+bx+cx^2 \mapsto \begin{bmatrix}a\\ b\\ c\end{bmatrix}$$
- The formal statement is that the mapping 
$$V \mapsto \mathbb{R}^n \quad \vec{x} \mapsto [\vec{x}]_\beta$$
- is an *isomorphism of vector spaces*. 

Summary of example #1: 
- By choosing a basis,
	- A vector space of dimension $n$ can be identified with $\mathbb{R}^n$


## **II. Comparing Coordinates in Diffrent Bases**
What if we choose a different basis $\mathcal{A} = \{\vec{u}_1, \cdots , \vec{u}_{n}\}$  for $V$?
- This gives us different identification of $V$ in $\mathbb{R}^n$ 
	$$V \mapsto \mathbb{R}^n \quad \vec{x} \mapsto [\vec{x}]_{\mathcal{A}}$$
- Now there are two different ways of writing each vector $\vec{x}$ in $V$ as a column vector, namely
$$[\vec{x}]_\mathcal{A} \quad \text{ and } \quad [\vec{x}]_\beta$$

**Change of basis matrix from $\beta$ to $\mathcal{A}$**
- **"change of coordinates matrix" might be better name, Because it the coordinates we actually change**
- denoted by matrix $S$
	- or $S_{\beta \mapsto \mathcal{A}}$ (to emphasize that $S$ operates on $\beta$-coordinates to 
	 produce $\mathcal{A}$-coordinates)

- The change of basis matrix from $\beta$ to $\mathcal{A}$ is the $n \times n$ matrix $S_{\beta \mapsto \mathcal{A}}$ 
	- whose columns are the elements of $\beta$ expressed in $\mathcal{A}$
	- That is, 
$$S_{\beta \mapsto \mathcal{A}} = [ \ [\vec{v}_1]_\mathcal{A} \ \ [\vec{v}_2]_\mathcal{A} \ \cdots \ [\vec{v}_n]_\mathcal{A} \ ]$$

How are these columns related?
- There is an $n\times n$ matrix $S$ such that 
$$S[\vec{x}]_\beta = [\vec{x}]_\mathcal{A}$$
- Think of matrix $S$ as a machine that takes the $\beta$-coordinate column of each vector $\vec{x}$ and converts it (by multiplication) into the $\mathcal{A}$-coordinate column of $\vec{x}$ 

<u>How do we find the change of basis?</u> $S_{\beta \mapsto \mathcal{A}}$ 

### **Example 2**
Another basis for $\mathcal{P}_2$ is $\mathcal{A} = \{x+1, x-1, 2x^2\}$ 
- the change of basis matrix from $\beta = \{1, x, x^2\}$ to $\mathcal{A}$ is
$$S = 
\begin{bmatrix}
\cfrac{1}{2} & \cfrac{1}{2} & 0\\
-\cfrac{1}{2} & \cfrac{1}{2} & 0\\
0 & 0 & \cfrac{1}{2}
\end{bmatrix}
$$
- consider the element $f = a+bx+cx^2$ 
- Then, $[f]_\beta = \begin{bmatrix}a\\ b\\ c\end{bmatrix}$ and ,
$$[f]_\mathcal{A} = S[f]_\beta = 
\begin{bmatrix}
\cfrac{1}{2} & \cfrac{1}{2} & 0\\
-\cfrac{1}{2} & \cfrac{1}{2} & 0\\
0 & 0 & \cfrac{1}{2}
\end{bmatrix}
\begin{bmatrix}a\\ b\\ c\end{bmatrix}
= 
\begin{bmatrix}
\cfrac{(a+b)}{2}\\
\cfrac{(b-a)}{2}\\
\cfrac{c}{2}
\end{bmatrix}
$$
- This represents the fact that $f$ can also be written as $\cfrac{a+b}{2}(x+1) + \cfrac{b-a}{2}(x-1) + \cfrac{c}{2}(2x^2)$ 

We could convert from $\mathcal{A}$-coordinates to $\beta$-coordinates in the way,
but the matrix that does this, denoted $S_{\mathcal{A} \mapsto \beta}$ is not the same matrix as  $S_{\beta \mapsto \mathcal{A}}$ 
<u>Understand why!</u>
$$S_{\beta \mapsto \mathcal{A}} = S_{\beta \mapsto \mathcal{A}}^{-1}$$ 
Why is the change of coordinates mapping
$$\mathbb{R}^n \mapsto \mathbb{R}^n \quad [\vec{x}]_\beta \mapsto [\vec{x}]_\mathcal{A}$$
given by matrix multiplication?
- *How do we know that is is a linear transformation?*

The points is that the change-of0coordinates maps is the composition oof the maps
$$
\begin{aligned}
&\mathbb{R}^n \mapsto V \mapsto \mathbb{R}^n\\
&[\vec{x}]_\beta \mapsto x \mapsto [\vec{x}]_\mathcal{A}
\end{aligned}
$$
- both of these identifications are *isomorphism* 
	- so their composition is also an isomorphism
		- (prove)
	- In particular, it is a linear transformation $\mathbb{R}^n \mapsto \mathbb{R}^n$ 
	- And, every linear transformation $\mathbb{R}^n \mapsto \mathbb{R}^n$ is given by matrix multiplication

Compute columns of S "change of coordinate(basis) matrix"
- remember that $S_{\beta \mapsto \mathcal{A}}$ "eats" $\beta$-coordinates and "spits out" $\mathcal{A}$-coordinates via the matrix multiplication 
$$S_{\beta \mapsto \mathcal{A}}[\vec{x}]_\beta = [\vec{x}]_\mathcal{A}$$
so in particular, for each basis element of $\vec{v}_j$ in $\beta$ we have 
$$S_{\beta \mapsto \mathcal{A}} [\vec{v_j}]_\beta = [\vec{v_j}]_\mathcal{A} $$
but what is $[\vec{v}_j]_\beta$ 
- *It is the standard unit column vector $\vec{e}_j$*
	- So, the basis element is an unit vector
This says 
$$S_{\beta \mapsto \mathcal{A}} \ \vec{e}_j = [\vec{v}_j]_\mathcal{A}$$
but for any matrix, including $S_{\beta \mapsto \mathcal{A}}$, multiplying by $\vec{e}_j$ will produce its $j^{th}$ column.
- this confirms that $j^{th}$ column of $S_{\beta \mapsto \mathcal{A}}$ is precisely $\vec{v}_j$ expressed in $\mathcal{A}$-coordinates

Summary of example 2: 
- The change of coordinate (basis) matrix $S_{\beta \mapsto \mathcal{A}}$ is the matrix whose $j^{th}$ column is $[\vec{v}_j]_\mathcal{A}$ 
	- where $\vec{v}_j$ is the $j^{th}$ basis element of $\beta$ 
- For every vector $\vec{x}$ in $V$, we have 
	- $$S_{\beta \mapsto \mathcal{A}} [ \vec{x}]_\beta = [\vec{x}]_\mathcal{A}$$

## **III. Using Bases to Represent Transformations**

Let $T : V \mapsto V$ be a linear transformation 
The choice of $\beta$ (basis) for $V$(vector space) identifies both the source and target of $T$ with $\mathbb{R}^n$ 
- thus, $T$ gets identified with a linear transformation $\mathbb{R}^n \mapsto \mathbb{R}^n$, and hence with a matrix multiplication.
- <u>Thus,</u>  this matrix is called the **Matrix of $T$ with respect to the basis $\beta$** 

*The matrix of $T$ in the basis $\beta = \{\vec{v}_1, \cdots , \vec{v}_n\}$ is the $n\ times n$ matrix*
$$[T]_\beta = [[T(\vec{v}_1)]_\beta \ \ [T(\vec{v}_2]_\beta, \ \cdots \ , [T(\vec{v}_n]_\beta]$$
- whose columns are the vectors $T(\vec{v}_i)$ expressed in the basis $\beta$ 

This matrix is helpful for computation. 
Take any $\vec{x} \in V$ 
- to compute $T(\vec{x})$ 
	- convert $\vec{x}$ to the column vector $[\vec{x}]_\beta$,
	- then multiply by the $n\times n$ matrix $[T]_\beta$ 
		- this gives a column vector which represents the element $T(x)$ in the basis $\beta$. That is,
		- $$[T(\vec{x})]_\beta = [T]_\beta\, [\vec{x}]_\beta$$
### **Example III**
Consider the transformation $D : \mathcal{P}_2 \mapsto \mathcal{P}_2$ 
- that sends $f$ to $\cfrac{df}{dx}$ 
- the matrix of $D$ in the basis $\beta = \{1, x, x^2\}$ is
- $$\begin{bmatrix}0 & 1 & 0\\ 0 & 0 & 2\\ 0 & 0 & 0 \end{bmatrix}$$
- So the differentiation is identified with the matrix multiplication: 

$$[D(a+bx+cx^2)]_\beta = [D]_\beta [a+bx+cx^2]_\beta = \begin{bmatrix}0 & 1 & 0\\ 0 & 0 & 2\\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix}a\\ b\\ c\end{bmatrix} = \begin{bmatrix}b\\ 2c\\ 0\end{bmatrix}$$
This represent the fact that $\cfrac{d}{dx} (a+bx+cx^2) = b + 2cx$ 

For $[T]_\beta$ verify the formula,
$$[T(\vec{x})]_\beta = [T]_\beta [\vec{x}]_\beta$$
for all vectors $\vec{x}$ in vector space $V$ 
- good first step is to check this formula for the elements $\vec{v}_i$ in the basis $\beta$ 
- do you see why knowing the formula for the basis elements implies it for all vectors $x$?

Summary III:
- Let $T : V \mapsto V$  be a linear transformation.
- the choice of basis $\beta$ identfies both the source and target with $\mathbb{R}^n$ 
	- and therefore, mapping $T$ with matrix multiplication by $[T]_\beta$ 
	- The matrix $[T]_\beta$ is easy to remember :
		- its $j^{th}$ column is $[T(\vec{v}_j)]_\beta$ 

## **IV. Comparing Matrices of a transformation in Different Bases**

## **V. Choosing Bases wisely**
Is the basis $\mathcal{A} = \{u_1, u_2, \cdots, u_n\}$ is orthonormal, 
- then we can write vectors in the basis of $\mathcal{A}$ 
The coordinates of $\vec{x} \in \{u_1, u_2, \cdots , u_n\}$ will be 
$$[\vec{x}]_\mathcal{A} = 
\begin{bmatrix}
\vec{x}\cdot \vec{u}_1\\
\vec{x}\cdot \vec{u}_2\\
\vdots\\
\vec{x}\cdot \vec{u}_n
\end{bmatrix}
$$
But if we tried to write $\vec{x}$ in a non-orthonormal basis, it would be hard to find coordinates.
- orthonormal basis is helpful for computing projections
the change of basis matrix $S_{\beta \mapsto \mathcal{A}}$ from any basis $\beta$ to an orthonormal basis is easy  to find: 
- the $ij^{th}$ entry will be $\vec{u}_i\cdot\vec{v}_j$ 
- and if we used Gram Schmidt process to get the new basis, the change of basis matrix will appear upper triangular. 

### **Example 5**

Let $V$ be the subspace of $\mathbb{R}^3$ spanned by $v_1 = \begin{bmatrix}3\\ 0\\ 4\end{bmatrix}$ and $v_2 = \begin{bmatrix}1\\ 1\\ 1\end{bmatrix}$.
Using Gram Schmidt Orthogonalization process, we find new basis 
$$\{u_1, u_2\} = \left\{\begin{bmatrix}\cfrac{3}{5}\\ 0\\ \cfrac{4}{5}\end{bmatrix},
\cfrac{1}{\sqrt{26}}\begin{bmatrix}\cfrac{3}{5}\\ 5\\ -\cfrac{3}{5}\end{bmatrix}\right\}$$
which is *orthonormal*

The change of basis from $\{v_1, v_2\}$ to $\{u_1, u_2\}$ is easy to find,
$$
S = 
\begin{bmatrix}
\vec{v}_1\cdot\vec{u}_1 & \vec{v}_2\cdot\vec{u}_1\\
\vec{v}_1\cdot\vec{u}_2 & \vec{v}_2\cdot\vec{u}_2
\end{bmatrix}
=
\begin{bmatrix}
5 & \cfrac{7}{5}\\
0 & \cfrac{\sqrt{26}}{5}
\end{bmatrix}
$$
We can write the vector $\vec{v} = \begin{bmatrix}2\\ -1\\ 3\end{bmatrix}$,  for example as a column using $\{v_1, v_2\}$ or $\{u_1, u_2\}$
In the basis $\{v_1, v_2\}$, this is easy:
- $$[\vec{v}]_{\{v_1, v_2\}} = \begin{bmatrix}1\\ -1\end{bmatrix}$$  
In the basis $\{u_1, u_2\}$, we cna use
$$
[\vec{v}]_{\{v_1, v_2\}} = S[\vec{v}]_{\{v_1, v_2\}} = 
\begin{bmatrix}
\cfrac{1}{5} & \cfrac{7}{5}\\
0 & \cfrac{\sqrt{26}}{5}
\end{bmatrix}
\begin{bmatrix}1\\ -1\end{bmatrix}
=
\begin{bmatrix}-\cfrac{8}{5}\\ -\cfrac{\sqrt{26}}{5}\end{bmatrix}
$$

This represents the fact that $\vec{v}$ can be written as 
$$\cfrac{-8}{5}\vec{u}_1+\cfrac{-\sqrt{26}}{5}\vec{u}_2$$
 

Another nice basis is an *eigenbasis* 
- for a linear transformation $T : V \mapsto V$ is one in which the matrix is **Diagonal**
- If the matrix of $T$ is diagonal in a basis $\beta = \{v_1, v_2, \cdots, v_n\}$ 
$$
[T]_\beta =
\begin{bmatrix}
\lambda_1 & 0  & \cdots & 0\\
0 & \lambda_2  & \cdots & 0\\
\vdots & & \ddots & \vdots\\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$
This this says exactly that $T(v_i) = \lambda_i v_i$ 
- That is that the basis $\beta$ consists of eigenvectors for $T$ 
	- *Proof Why*
Geometrically, we see $T$ is stretching (or contracting) $v_i$ by the scalar $\lambda_i$ 
The **directions** of the stretching are the **eigenvectors** and the **stretching factors** $\lambda_i$ are **eigenvalues**


### **Example 5** 
Let $T: \mathbb{R}^n \mapsto \mathbb{R}^n$ be multiplication by the $n\times n$ matrix $A$
Suppose that $\beta = \{v_1, \cdots, v_n\}$ is an eigenbasis for $T_A$ with eigenvalues $\lambda_1, \cdots, \lambda_n$ then, 
$$[T]_\beta =
\begin{bmatrix}
\lambda_1 & 0  & \cdots & 0\\
0 & \lambda_2  & \cdots & 0\\
\vdots & & \ddots & \vdots\\
0 & 0 & \cdots & \lambda_n
\end{bmatrix}$$
is a diagonal matrix.
Comparing the matrices of this transformation in the standard basis $\mathcal{A} = \{e_1, \cdots e_n\}$ and eigenbasis $\beta = \{v_1, \cdots, v_n\}$ we have,
$$[T]_\beta = S_{\mathcal{A} \mapsto \beta} \ \ [T]_\mathcal{A} \ \ S_{\beta \mapsto \mathcal{A}}$$
$S_{\beta \mapsto \mathcal{A}} = [v_1 \cdots v_n]$ and that $S_{\mathcal{A} \mapsto \beta}$ is its inverse.
and $[T]_\mathcal{A} = A$ 
- make sure why! *proof*

and so, we can say 
$$
[T]_\beta = S_{\mathcal{A} \mapsto \beta} \ \ [T]_\mathcal{A} \ \ S_{\beta \mapsto \mathcal{A}}\\
$$
or 
$$
S^{-1}AS = D
$$
where $D$ is the diagonal matrix formed by the eigenvalues of $A$ 
and $S$ is the matrix formed by the corresponding (linearly independent eigenvectors).

Writing an expression like this is called **Diagonalizing** the matrix $A$
(**Note:** not every matrix can be diagonalized because not every transformation has an eigenbasis!)

Summary of V:
Depending on the problem we are trying to solve, the choice of a orthonormal basis can make things cleaner and easier.

Orthonormal bases (always exist) are nice because it is easy to find the coordinates of any vector in an orthonormal basis (by using dot product)

An eigenbasis is nice for analyzing a given transformation $T$, because the matrix of $T$ in an eigenbasis will be diagonal. However some transformations do not have eigenbasis.



## **VI. Another Use of The Change of Basis Matrix**

The change of coordinate (basis) matrix has a special use where vector space $V$ is a subspace of $\mathbb{R}^d$ 

Suppose $V$ is a subspace of $\mathbb{R}^d$ with basis $\beta = \{v_1, \cdots,v_n\}$
- each $\vec{v}_j$ is a column vector, 
	- so we can line them up in a $d \times n$ matrix $[v_1, \cdots, v_n]$ 

Another basis for $V$, 
- $\mathcal{A} = \{u_1, \cdots, u_n\}$, will give another $d\times n$ matrix $[u_1, \cdots, u_n]$  

What is the relationship between these two $d\times n$ matrices?

Let $S$ be the change of basis matrix from $\beta$ to $\mathcal{A}$ 
Then we have the matrix equality
$$[v_1 \ \cdots \ v_n] = [u_1 \ \cdots \ u_n] S_{\beta \mapsto \mathcal{A}}$$
on <u>RHS</u> we are taking the product of a $d\times n$ and $n\times n$ matrix  

Example $VI:$ 
The space $V \subset \mathbb{R}^3$ has basis 
$$\beta  = \{v_1, v_2\} = \left\{\begin{bmatrix}3\\ 0\\ 4\end{bmatrix}, \begin{bmatrix}1\\ 1\\ 1\end{bmatrix}\right\}$$ and 
$$\{u_1, u_2\} = \left\{\begin{bmatrix}\cfrac{3}{5}\\ 0\\ \cfrac{4}{5}\end{bmatrix},
\cfrac{1}{\sqrt{26}}\begin{bmatrix}\cfrac{3}{5}\\ 5\\ -\cfrac{3}{5}\end{bmatrix}\right\}$$
So we have matrix equation,

$$
\begin{bmatrix}
3 & 1\\
0 & 1\\
4 & 1
\end{bmatrix}
=
\begin{bmatrix}
\cfrac{3}{5} & \cfrac{4}{5\sqrt{26}}\\
0 & \cfrac{5}{5\sqrt{26}}\\ 
\cfrac{4}{5} & -\cfrac{3}{5\sqrt{26}}
\end{bmatrix}
\begin{bmatrix}
5 & \cfrac{7}{5}\\
0 & \cfrac{\sqrt{26}}{5}
\end{bmatrix}
$$
Because the basis $\{u_1, \cdots, u_n\}$ is obtained from $\{u_1, \cdots, u_n\}$ by *Gram Schmidt*, this is the **QR factorization**.
Note : the change of basis matrix $R$ is *upper triangular*, (this was $S$ previously, but because we are calling QR factorization, we say $R$)

Valid for only subspaces of $\mathbb{R}^d$ 

*Proof :*
We use dot multiplication.
The row $[u_1, \cdots, u_n]$ times the $j^{th}$ column of $S$ (change of basis matrix)
- is the $j^{th}$ column of the product.
Say the $j^{th}$ column of $S$ is $\begin{bmatrix}a_{1j}\\ a_{2j}\\ \vdots \\ a_{nj}\end{bmatrix}$ 
- then the $j^{th}$ column of the product is $a_{1j}u_1 + a_{2j}u_2 + \cdots + a_{nj}u_n$ 
	- but this is exactly $v_j$ by the definition of $S$
Remember that by the definition, the $j^{th}$ column of $S$ is the coordinate column of $v_j$ expressed in $\mathcal{A}$ 





