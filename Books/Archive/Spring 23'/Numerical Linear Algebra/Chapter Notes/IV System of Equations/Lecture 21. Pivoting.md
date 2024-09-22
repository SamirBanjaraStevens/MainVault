Instability of Gaussian elimination can be controlled by permuting the order of the rows of the marix beingoperated on, an operation called *Pivitiong*

## Pivots
At step $k$ of Gaussian elimintion,
- multiple of row $k$ are subtracked from rows $k+1, \dots , m$ of the working matrix $X$ in order to introduce zeros in entry $k$ of these rows

in this operation,
- row $k$, 
- column $k$ and especially the 
- entry $x_{k, k}$
 play special roles.

$x_{kk}$ - *Pivot*

From every entry in the submatrix $X_{k+1:m, k:m}$ is subtracted the product of a number in row $k$ and a number in column $k$, divide dby $x_{kk}$

However, there is no reason why the $k$-th row and column must be chosen for the elimination.

We could just introduce xeros in the column $k$ by adding multiples of some row $i$ with $k<i\leq m$ to other rows $k,\dots ,m$ 

In this case the entry, $x_{ik}$ would be the pivot


Gaussian Elimination with partial pivoting is equivalent to the folowwing prodcedure:
1. Permute the rows of $A$ accroding to $P$
2. Apply Gaussian elimintaion without pivoting to $PA$ 

#### Algorithm 21.1 Gaussian Elimination w/ Partial Pivoting
***
$U = A$
$L = I$
$P = I$
$\textbf{For } \text{k = 1} \textbf{ to } \text{ m - 1}\textbf{ do:}$ 
	$\text{Select } i\geq k \text{ to maximixe } \|u_{ik}\|$
	$u_{k, k:m} \leftrightarrow u_{i, k:m} \quad\text{ (intercgange two rows)}$  
	