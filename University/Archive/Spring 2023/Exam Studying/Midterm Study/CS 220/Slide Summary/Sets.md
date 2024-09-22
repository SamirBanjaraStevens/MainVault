Natural numbers : $\mathbb{N} = \{0, 1, 2, 3, \cdots\}$
Integers : $\mathbb{Z} = \{\cdots, -2, -1, 0, 1, 2, \cdots\}$
Real Numbers $\mathbb{R} = \{47.3, -12, \pi, 5, \cdots\}$ 
Rational Numbers $\mathbb{Q} = \{1.5, 2.6, -3.8, 15, \cdots\}$


If a set $B$ contains $5$ elements then
- its <u>cardinality</u> is $5$

The Power of Sets

$2^A$ or $\mathcal{P}(A)$  
$A = \{x, y, z\}$ 
$2^A \text{ or } \mathcal{P}(A) = \{\emptyset, \{x\}, \{y\}, \{z\}, \{x, y\}, \{x, z\}, \{y, z\}, \{x, y, z\}\}$ 

$A = \emptyset$
- $|A| = 0$
$2^A = \{\emptyset\}$ 
- $|2^A| = 1$

how many elements in a power set ? 
- $2^n$ where $n$ is number of elements in set $A$ 

So is set $A$ has 3 elements $\{x, y, z\}$
- then there will be $2^3 = 2\cdot 2\cdot 2 =  8$ elements'



Two sets are disjoint is they share no elements 
- $A \cap B = \emptyset$ 

Cartesian Product 
$A = \{x, y, z\}$
$A \times A = \{(x,x), (x, y), (x, z), (y, x), (y, y), (y, z), (z, x), (z, y), (z, z)\}$ 

Partition of a set $S$ is 
- a collection of disjoint (two sets do not share an element) 
	- non empty subsets of $S$  that have $S$ as their union

A collection of subsets $A_i \in I$
- Forms a partition of $S$ if and only if
	1. $A_i \neq \emptyset$ for $i \in I$ 
		-  (subsets are not empty)
	2. $A_I \cap A_j = \emptyset$ if $i \neq j$ 
		-  (subsets are disjoint)
	3. $\bigcup_{i\in I} A_i = S$ 
		-  (S is their union)

$S = \{u, m, b, r, o, c, k, s\}$

$m = \{\{m, o, c, k\}, \{r, u, b, s\}\}$ 
- Subsets are not empty
- Subsets are disjoint
- $S$ is their union