1. Recall that the span of set $S$ of vectors is the collection of all vectors obtainable as linear combinations of the elements of $S$. Is the vector $\vec{v}$  below in the Span of the set of vectors $S$ bellow
	- Use Row reduction methods to answer the question and justify your answer.

*Sol :*
- $\text{range}(S)=\text{ column}(S)=\text{ span}(S) = \text{ span}\{s_1,\cdots,s_n\}$ 

From set $S$ of vector $\vec{v}$ we obtain augmented matrix $M$
$$M =
\left(
\begin{array}{ccc|c}
1 & 2 & -1 & 1\\
3 & 0 & 3 & -9\\
-1 & 4 & -5 & 11
\end{array}\right)
$$
we obtain the RREF of matrix $M$ as follows:
$$
RREF(M) =
\left(
\begin{array}{ccc|c}
1 & 0 & 1 & -3\\
0 & 1 & -1 & 2\\
0 & 0 & 0 & 0
\end{array}
\right)
$$
Hence, vector $\vec{v}$ can be represented as such
$$\vec{v} = -3(s_1) + 2(s_2)+ 0(s_3)$$
more preciscely, 
$$
\begin{bmatrix}
1\\ -9\\ 11
\end{bmatrix}
=
-3
\begin{bmatrix}
1\\ 3\\ -1
\end{bmatrix}
+
2
\begin{bmatrix}
2\\ 0\\ 4
\end{bmatrix}
+
0 
\begin{bmatrix}
-1\\ 3\\ -5
\end{bmatrix}
$$

Thus vector $\vec{v}$ is a span of the vectors in $S$. 


## **Question 2**

Consider the matrix $H$
$$H = \left(\begin{array}{ccc|c}1 & 4 & 7 & a\\
2 & 5 & 8 & b\\ 3 & 6 & 9 & c\end{array}\right)$$
- *(a).* Write a system of linear equations in the traditional form, using unknowns name from the sequence $\{x, y, z, \cdots\}$, which corresponds to the augmented matrix $H$
	- *Solution : *

 $$
\left\{
\begin{array}{cccc}
1x+4y+7z=a\\
2x+5y+8z=b\\
3x+6y+9z=c
\end{array}
\right\}$$

- *(b).* Find RREF of matrix $H$
	- *Solution : *

elementary row operations applied to obtain RREF of matrix $H$:
$-2I+II \rightarrow II$
- $-2x-8y-14z=-2a$
- $2x+5y+8z=b$
- $=$
	- $0x-3y-6z=(-2a+b)$

$-3I+III\rightarrow III$ 
- $-3x-12y-21z=-3a$
- $3x+6y+9z=c$
- $=$
	- $0x-6y-12z=(-3a+c)$

$$H = \left(\begin{array}{ccc|c}1 & 4 & 7 & a\\
0 & -3 & -6 & (-2a+b)\\ 0 & -6 & -12 & (-3a+c)\end{array}\right)$$

Then, 
$-2II+III\rightarrow III$
- $0x+6y+12z=-2(-2a+b)=(4a-2b)=(2a-b)$
- $0x-6y-12z=(-3a+c)$
- $+ =$
	- $0x+0y+0z=(2a-b)+(-3a+c)$


- *(c).* For which values of the right hand side (RHS) entries a,  b, c, does $H$ denote a consistent system?
	- *Solution : *
		- only if a-2b+c=0
- *(d).** Describe the full solution set of the system if the $RHS$ has $a=9, b=6, c=3$
	- *Solution : *
- *(e).* Are there values of $a, b, c$ for which the system has a unique solution?
	- *Solution : *
		- because matrix H is not of full rank, no!
		- $$\text{full rank } \iff \text{linear independence} \iff \text{ basis } \iff \text{ unique coordinates }$$



(i)
	"If the system $A\vec{x} = \vec{b}$ has a unique solution for one RHS vector $\vec{b}$
	it has a unique solution for *every*  RHS vector $\vec{b}$"

If there is a unique solution for matrix $A$, the matrix $A$ is of full rank. 
But it could have linearly dependent row vectors, so that for a particular $\vec{b}$ there is no solution (inconsistent).

for example, the matrix 
$$
\left(\begin{array}{ccc|c}
1 & 0 & 0 & 1\\
0 & 1 & 0 & 1\\
0 & 0 & 1 & 1
\end{array}\right)
$$
has a unique solution $x = 1, y = 1, z = 1$ 
but it RHS $\vec{b}$ was not $\begin{pmatrix}1\\1\\1\end{pmatrix}$ , 
and instead it had  
$$
\vec{b} = 
\begin{pmatrix}
1\\
1\\
0
\end{pmatrix}$$
then the system $A\vec{x}=\begin{pmatrix}1\\1\\0\end{pmatrix}$, has no solution, and is inconsistent, thus it can not have a unique solution for every vector $\vec{b}$



(ii)
	"If the system $A\vec{x} = \vec{b}$ has a multiple solutions for one RHS vector $\vec{b}$ it has multiple solutions for every RHS vector $\vec{b}$" 

$$
\left(\begin{array}{ccc|c}
1 & 0 & 0 & 5\\
0 & 1 & 0 & 3\\
0 & 0 & 0 & c
\end{array}\right)
$$
if $c = 0$ then this system has solutions $x = 5, y= 3$ and $z$ arbitrary. 
	Thus in this particular solution results in infinitely many solutions.
If $c\neq 0$ then this system is inconsistent. 
	
(iii) 
	"If the system $A\vec{x} = \vec{b}$  has multiple solutions for one RHS vector $\vec{b}$ it has  no unique solutions for $\vec{b}$"
	**False**
- if $A\vec{x} = \vec{b}$ has multiple solutions for one particular RHS $\vec{b}$ 
	- then $RREF(A)$ has at least one linearly dependent column. 
- For any other RHS $\vec{b}$ 
	- if the system $A\vec{x} = \vec{b}$ is consistent, it will have a free variable, and hence many solutions

