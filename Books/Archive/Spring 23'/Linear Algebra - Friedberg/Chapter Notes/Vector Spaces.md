# 1.2 Vector Spaces
##### Definitions 
A **Vector Space** (or linear space) **V** over a $\text{feild}^{2}$ in *F* consists of a set on which two operations (called addition and scaler multiplication) are defined so that for each pair of elements $x, y$, in **V** there is a unique element $x + y$ in **V** and each element *a* in *F* and each element *x* in *V* is a unique element $ax$ in **V** 

**Scalars** : Elements of field **F**

**Vectors** : Elements of vector space **V**
(does not describe physical entity)

**n-tuple** : Object of form $\,(a_1, a_2, ... , a_n\,)$ where the entries are elements of a field *F*.
	The elements are called components. 

Two n-tuples $A = \,(a_1, a_2, ... , a_n)$ and $B = \,(b_1, b_2, ... , b_n\,)$ with entries from a field F are called equal if $a_i = b_i \: \text{for} \:i = 1, 2, ..., n$

Vectors in $F^{n}$ can be written as **column vectors**
$$ 
\begin{pmatrix}   
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{pmatrix}
$$

& row vectors are represented as such 
$$ 
\begin{pmatrix}   
a_{1} &   a_{2} & \ldots & a_{n}   
\end{pmatrix}
$$
# 1.3 Subspaces

A subset **W** of a vector space **V** over a field *F* is called a subspace of **V** if **W** is a vector space over *F* with the operations of addition and scalar multiplication defined on **V**.

The **Transpose** $A^{t}$ of a $m\times n$ matrix *A* is the $n\times m$ matrix obtained from A by interchanging the rows with the columns; that is, 
$$\,(A^{t}\,)_{ij} = A_{ji}$$

For example, 
$$
\begin{pmatrix} 
1 & -2 & 3 \\
0 &  5 & -1 
\end{pmatrix}^{t} 
= 
\begin{pmatrix} 
1 &  0 \\
-2 &  5 \\
3 & -1 
\end{pmatrix}
$$

An  $m \times n$ matrix *A* is called **Upper Triangular** if all it's entries lying below the diagonal entires are zero, that is $A_{ij} = 0$ whenever $i > j$ 

An $n\times n$ matrix *M* is called a **Diagonal Matrix** if $M_{ij} = 0$ whenever $i\ne j$

### Theorem 1.4 
#### Any Intersection of subspaces of a vector space **V** is a subspace **V**.

**Notes every subspace contains the zero vector**

Let *C* be a collection of subspaces of **V**, and let **W** denote the intersection of the subspaces in *C*. 
Since, every subspace contains the zero vector $0\in W$. 
Let $a\in F$ and $x, y\in W$. 
Then $x$ and $y$ are contained in each subspace in *C*. 
Because each subspace in *C* is closed under addition and scalar multiplication, it follows that $x + y$ and *ax* are contained in each subspace in *C*. 
Hence, $x + y$ and *ax* are also contained in **W**, so that **W** is a subspace of **V**.

# 1.4 Linear Combinations and Systems of Linear Equations


Equation of the plane through three non-collinear points **A, B, and C** in space is $x = A + su + tv$, where *u* and *v* denote the vectors beginning at **A** and ending at **B** and **C**, and *s* and *t* represent some arbitrary real numbers.

if **A** is the origin, equation of the plane simplifies to $x = su + tv$, and the set of all points in this plane is a subspace of $\mathbb{R}^{3}$.

##### Definitions 

**Linear Combination** :
Let **V** be a vector space and *S* a non empty subset of **V**. A vector $v\in V$ is called a **Linear Combination** of vectors of *S* if there exist a finite number of vectors $u_{1}, u_{2}, \dots ,u_{n}$ in *S* and scalars $a_{1}, a_{2},\dots ,a_{n}$ in *F* such that $v = a_{1}u_{1} + a_{2}u_{2} +\dots + a_{n}u_{n}$
And so *v* is a linear combination of $u_{1}, u_{2}, \dots ,u_{n}$ and call $a_{1}, a_{2},\dots ,a_{n}$ the coefficients of the linear combinations.

**Observe** that in any vector space **V**, $0v = 0$ for each $v\in V$.
Thus the zero vector is a liner combination of any nonempty subset of **V**.

**Span** : 
Let *S* be a nonempty subset of a vector space **V**. 
Denoted span(*S*), is the the <ins>set consisting of all linear combinations</ins> of the vectors in *S*. 

In $\mathbb{R}^{3}$ the span of set $\{ \,(1, 0, 1\,), \,(0, 1, 0\,)\}$ consists of all vectors in $\mathbb{R}^{3}$ that have the form $a\,(1, 0, 1\,) + b\,(0, 1, 0\,) = \,(a, b, 0\,)$ for some scale *a* and *b*. 
Thus, the span of $\{ \,(1, 0, 1\,), \,(0, 1, 0\,)\}$ contains all the points in the *xy-* plane. 
In this case, the span of the set is a subspace of $\mathbb{R}^{3}$

### Theorem 1.5
#### The span of any subset *S* of a vector space **V** is a subspace of **V** that contains *S*. Moreover, any subspace **V** that contains *S* must also contain the span of *S*.

**Generates (or Spans)** : a subset *S* of a vector space *V* **generates** *V* if **span(S) = V**.
In this case, we also that that the vectors of *S*, which are linear combinations of vector space *V* is equal tot the vectors of *V*. 


##### Example 

The vectors $(1, 1, 0)$, $(1, 0, 1)$ and $(0, 1, 1)$ **generate** $\mathbb{R}^{3}$ since an arbitrary vector $(\, a_{1}, a_{2}, a_{3} \,)$ in $\mathbb{R}^{3}$ is a linear combination of the three given vectors; in fact the scalars $r, s, \, \text{and}\, t$ for which 
$$ r\,(1, 1, 0 \,) + s\,(1, 0, 1 \,) + t \,(0,1, 1 \,) = \,(a_{1}, a_{2}, a_{3}\,)$$
are 

$$r = \frac{1}{2}\,(a_{1} + a_{2} - a_{3}\,) \quad s = \frac{1}{2}\,(a_{1} - a_{2} + a_{3}\,) \quad \text{and} \quad t = \frac{1}{2} \,(-a_{1} + a_{2} + a_{3}\,)$$

# 1.5 Linear Dependence and Independence

Suppose that *V* is a vector space over an infinite field and that *W* is a subspace of *V*. 

Unless *W* is the zero subspace, *W* is an infinite set. 

It is desirable to find a "small" finite subset *S* of *W* that generates *W* because we can then describe each vector in *W* as a linear combination of the finite number of vectors in *S*.

Smaller *S*, fewer number of computations  required to vectors in *W* as such linear combinations. 

Consider subspace *W* of $\mathbb{R}^{3}$ generated by $S = \{u_{1}, u_{2}, u_{3}, u_{4}\}$, where $u_{1} = \,(2, -1, 4\,), u_{2} = \,(1, -1, 3\,), u_{3} = \,(1, 1, -1\,), u_{4} = \,(1, -2, -1\,)$ 

**Find a proper subset of *S* that also generates *W***
are some vectors in *S* a linear combinations of the other vectors in *S*?

and so,$u_{4}$ is a linear combination of the other vectors in *S* if and only if there are scalars $a_{1}, a_{2}, a_{3}$ such that, 

$$u_{4} = a_{1}u_{1} + a_{2}u_{2} + a_{3}u_{3}$$

that is, if and only there are scalars $a_{1}, a_{2}, a_{3}$ satisfying 

$$\,(1, -2, -1\,) = \,(2a_{1} + a_{2} + a_{3}, -a_{1} - a_{2} + a_{3}, 4a_{1} + 3a_{2} - a_{3}\,)$$

Thus, $u_{4}$ is a linear combination of $u_{1}, u_{2}, u_{3}$ if and only if the system of linear equations 

$$\begin{align} 2a_{1} + a_{2} + a_{3} & = 1 \\ -a_{1} - a_{2} + a_{3} & = -2 \\ 4a_{1} - 3a_{2} - a_{3} & = -1 \end{align}$$ 

has a solution. 

it can be shown $u_{3} = 2u_{1} - 3u{2} + 0u_{4}$. 

checking some vector in s is a linear combination of the other vectors in *S* could require that we solve several different linear equations before we determine which, if any, of $u_{1}, u_{2}, u_{3}, u_{4}$ is a linear combination of of the other.

since, $u_{3} = 2u_{1} - 3u{2} + 0u_{4}$, we have,

$$-2u_{1} + 3u_{2} + u_{3} - 0u_{4} = 0$$ 
the zero vector can be expressed a linear combination of the vectors in *S* using coefficients that are not all zero. 

converse is also true : 
**If the the zero vector can be written as a linear combination of the vectors in *S*,  in which not all coefficients are zero, 
then some vector in *S* is a linear combination of others** 

**Linearly Dependent** : A subset *S* of a vector space *V* is called **<u>Linearly Dependent</u>** if there exists a finite number of distinct vectors $u_{1}, u_{2}, \cdots, u_{n}$
in *S* and scalars $a_{1}, a_{2}, \cdots, a_{n}$, not all zero, such that $$$$$$a_{1}u_{1} + a_{2}u_{2} + a_{n}u_{n} = 0.$$
in this case we say that the vectors of *S* are linearly dependent
 
There must exist a non trivial representation of 0 (or zero vector) as a linear combination of $u_{1}, u_{2}, \cdots, u_{n}$ (vectors) in the set.

### Theorem 1.6 

#### Let V be a vector space, and let $S_{1}  \subseteq S_{2} \subseteq V$. If $S_{1}$ is linearly dependent, then $S_{2}$ is linearly dependent. 

##### Corollary : Let $V$ be a vector space, and let $S_{1}  \subseteq S_{2} \subseteq V$. If $S_{2}$ is linearly independent, then $S_{1}$ is linearly independent. 


The issue of weather *S* if the smallest generation set for its span is related to the question of weather *S* is linearly dependent.

# 1.6 Bases and Dimensions

if *S* is a generating set for a subspace *W* and no proper subset of *S* is a generating set for *W*, then *S* must be linearly independent. 

A linearly independent generating set for *W* posses a very useful property
	- Every vector in *W* can be expressed in one and only one way as a linear combination of the vectors in the set. 
		- Makes Linearly independent generating sets the building blocs of vector spaces.

### Definition

**Basis** : 
- $\beta$ for a vector space *V* is a <u>Linearly independent</u> subset of *V* that generates *V*. 
- If $\beta$ is a basis for *V*, we also sat that the vectors of $\beta$ form a basis for *V*. 

#### Example 2
In $F^{n}$, let $e_{1} = \,(1, 0, 0, \cdots, 0\,), e_{2} = \,(0, 1, 0, \cdots, 0\,), e_{n} = (\,0, 0, \cdots, 0, 1\,);$ 
$\{e_{1}, e_{2}, \cdots, e_{n}\}$ is the basis for $F^{n}$ and is called the **Standard Basis** for $F^{n}$.

### Theorem 1.8

#### Let $V$ be a vector space and $u_{1}, u_{2}, \cdots, u_{n}$ be distinct vectors in $V$. Then $\beta =  \{u_{1}, u_{2}, \cdots, u_{n}\}$ is a basis for $V$ if and only if each $v \in V$ can be uniquely expressed as a linear combination of vectors of $\beta$, that is, can be expressed in the form.,$$v = a_{1}u_{1} + a_{2}u_{2} + \cdots + a_{n}u{n}$$ For unique scalar $a_{1}, a_{2}, \cdots, a_{n}$.

**Proof:** 
Let set $\beta$ be a basis for $V$, 
If $v \in V$, then $v\in \text{span}\,(\beta\,)$, 
because $\text{span}\,(\beta\,) = V$,
Thus, $v$ is a linear combination of the vectors of $\beta$ 

If vectors $u_{1}, u_{2}, \cdots, u_{n}$ form a basis $\beta$ (set) for a vector space $V$, then every vector in $V$ can be uniquely expressed in the form $$v = a_{1}u_{1} + a_{2}u_{2} + \cdots + a_{n}u_{n}$$
for appropriately chosen scalars $a_{1}, a_{2}, \cdots , a_{n}$
Thus, $v$ determine a unique n-tuple of scalar $\,(a_{1}, a_{2}, \cdots, a_{n}\,)$ and, conversely each n-tuple of scalar determines a unique vector $v \in V$ by using the entries of the n=tuple as the coefficients of a linear combination of $u_{1}, u_{2}, \cdots, u_{n}$  . 

this suggests that $V$ is like the vector space $F^{n}$, where n is the numbers of vectors in the basis for $V$. 

<u>A finite spanning set for V can be reduced to a basis for V</u>

### Theorem 1.10 (Replacement Theorem)
#### Let $V$ be a vector space that is generated by a set $G$ containing exactly $n$ vectors, and let $L$ be a linearly independent subset of $V$ containing exactly $m$ vectors. Then $m \leq n$ and there exists a subset $H$ of $G$ containing $n-m$ vectors such that $L \cup H$ generates $V$.  








# 1.7 Maximal Linearly Independent Subsets


