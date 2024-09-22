A projector is a square matrix $P$ that satisfies
$$\tag{6.1} P^{2} = P$$

- also known as *impotent*
	- definition includes both orthogonal projectors and nonorthogonal 
		- We use *oblique projector* to refer nonorthogonal projectors

Projector
- thoughts of as arising from the notion that if one were to shine a light onto the subspace *range(P)* from the right direction
	- then $P_{v}$ would be the shadow projected by the vector $v$ 

Observe that if $v\in range(P)$, then it lies exactly in its own shadow,
- and applying the projector results in $v$ exactly
	- mathematically, we have $v= Px$ for some $x$ and
	- $$Pv = P^{2}x = Px = v$$
from what direction does the light shine when $v\neq Pv$ ?
- depends on $v$
- but for any particular $v$ drawing the line from $v$ to $Pv$, 
	- $Pv - v$. is the projector
Applying the projector to this vector gives the zero result
$$P(Pv-v) = P^2v - Pv = 0$$

- this means that $Pv-v \in null(P)$ 
	- that is the direction of the light may be different for different $v$
		- but is always described by a vector in null($P$)

![[Pasted image 20230303055915.png]]

### **Complementary projectors**

if $P$ is a projector
- $I-P$ is also a projector, for it is also idempotent:
	- $$(I-P)^2 = I-2P+P^2 = I - P$$
the matrix $I-P$ is called the complementary projector to $P$

Onto what space does $I-P$ project?
- the null space of $P$

$null(P)\subseteq range(I-P)$
- because if $Pv = 0$ 
	- we have $(I-P)v = v$

conversely $range(I-P) \subseteq null(P)$
- because for any $v$, we have $(I-P)v = v-Pv \in null(P)$ 
	- Therefore, for any projector $P$ 
		- $$\tag{6.2}range(I-P)=null(P)$$
		- By writing $P=I-(I-P)$ we derive the fact
			- $$\tag{6.3} null(I-P) = range(P)$$
	- We can also see that $null(I-P)\cap null(P) = \{0\}$ : 
		- any vector $v$ in both sets satisfies $v=v-Pv=(I-P)v = 0$
			- $$\tag{6.4} range(P)\cap null(P) = \{0\}$$
Computations show that  **Projector separate  $\mathbb{C}^m$ into two spaces**
- conversely, let $S_1$ and $S_3$ be two subspaces of $\mathbb{C}^m$ 
	- such that $S_1\cap S_2 = {0}$  
	- and $S_1 + S_2 = \mathbb{C}^m$ 
		- where $S_1+S_2$ denotes the span of $S_1$ and $S_2$ 
			- that is the set of vectors $s_1+s_2$ with $s_1\in S_1$ and $s_2\in S_2$ 
			- such a pair are *complementary subspaces*
- Then there is a projector $P$ such that the range$(P) = S_1$ 
	- we say that P is the projector into $S_1$ along $S_2$
	- the projector and its complement can be seen as unique solution to the following problem

Given $v$. find vectors $v_1 \in S_1$ and $v_2\in S_2$ such that $v_1+v_2=v$ 

the projection $Pv$ gives $v_1$ 
and the complementary projection $(I-P)v$ gives $v_2$
- these vectors are unique because all solutions must be of the form
$$(Pv+v_3)+((I_P)v-v_3)=v,$$
- where it is clear that $v_3$ must be in both $S_1$ and $S_2$ i.e, $v_3=0$ 

Suppose an $m\times m$ matrix $A$ has a complete set of eigenvectors ${v_j}$ as in 5.1, meaning that $\{v_j\}$ is a basis of $\mathbb{C}^m$ 

given $x \in \mathbb{C}^m$ for example
- what is the component of $x$ in the direction of a particular eigenvector $v$?
	- The answer is $Px$, where $P$ is a certain rank-one projector

#### **Orthogonal Projectors**

 an *Orthogonal Projector* is one that projects onto a sub space $S_1$ along space $S_2$, where $S_1$ and $S_2$  are orthogonal
 - **Orthogonal projectors are not Orthogonal Matrices**
- An orthogonal projector is any projection that is hermitian satisfying $P^* = P$ as well as (6.1) 

### **Theorem 6.1** 
- A projector $P$ is orthogonal if and only if $P^* = P$ 

*Proof:* 
If $P = P^*$ (hermitian), 
- then the inner product between a vector $Px\in S_1$ 
- and a vector $(I-P)y \in S_2$ is zero:
- $$x^*P^*(I-P)y = x^*(P-P^2)y = 0$$
Thus the projector is **orthogonal**,
- providing the proof in the **"if"** direction.

For **"only if"** we can use the SVD.
- Suppose $P$ projects onto $S_1$ along $S_2$, 
	- where $S_1 \perp S_2$ and $S_1$ has dimension $n$.
- Then an SVD of $P$ can be constructed as follows.
	- Let $\{q_1, q_2,\cdots, q_m\}$ be an orthonormal basis for $\mathbb{C}^m$ 
		- where $\{q_1, q_2,\cdots, q_n\}$ is a basis for $S_1$ 
		- and $\{q_{n+1},\cdots, q_m\}$ is a basis for $S_2$.
	- For $j \leq n$, 
		- we have $Pq_j = q_j$ 
	- and for $j > n$,
		- we have $Pq_j = 0$
- Now let $Q$ be the unitary matrix whose $j^{th}$ column is $q_j$ 
we then have,
$$
PQ =
\left[
\begin{array}{c|c|c|c}
 & & & & \\
q_1 & \cdots & q_n & 0 & \cdots\\
 & & & & \\
\end{array}
\right]
$$
so that, 
$$
Q^*PQ = 
\begin{bmatrix}
1 & & & & \\
 & \ddots & & & \\
 & & 1 & & \\
 & & & 0 & \\
 & & & & \ddots
\end{bmatrix}
=\Sigma
$$

A diagonal matrix with ones in the first $n$ entries and zero everywhere else.
Thus, we have constructed a singular value decomposition of $P$:
$$\tag{6.5} P  = Q\Sigma Q^*$$

*Noted:* 
This is also an eigenvalue decomposition **(5.1)**.
From here we see that $P$ is hermitian, since 
$$
\begin{aligned}
P^* &= (Q\Sigma Q^*)\\
&=Q\Sigma^* Q^*\\
&=Q\Sigma Q^*\\
&=P
\end{aligned}
$$ 
### **Projection with an Orthonormal Basis**

Since an orthogonal projector has some singular values equal to zero(excpet in the trival case $P = I$ )
- natural to drop the the silet columns of $Q$ in 6.5 
- and use the reduced rather than the full SVD
we obtain $$\tag{6.6} P = \hat{Q}\hat{Q^*}$$
- where columns of $\hat{Q}$ are orthonormal

In 6.6. the matrix $\hat{Q}$ need not come from an SVD.
Let $\{q_1,\cdots , q_n\}$ be any set of $n$ orthonormal vectors in $\mathbb{C}^m$ 
and let $\hat{Q}$ be the corresponding $m\times n$ matrix 

we know that $$v = r + \sum_{i=1}^{n}(q_iq_i^*)v$$
represents a **decomposition of a vector** $v\in \mathbb{C}^m$ **into a component in the column space** of $\hat{Q}$ plus a **component in the orthogonal** space.
Thus the map
$$
\tag{6.7}
v \rightarrow \sum_{i=1}^n (q_iq_i^*)v
$$   
is an **orthogonal projector onto the range**$(\hat{Q})$
and in matrix form it can be written as $y = \hat{Q}\hat{Q}^*v$ 

Thus any product $\hat{Q}\hat{Q}^*$ is always a **projector onto the column space of $\hat{Q}$** 
- regardless of how $\hat{Q}$ was obtained
	- as long as its columns are orthonormal

The **complement of an orthogonal projector** is also an **orthogonal projector**.(**Proof: $I-\hat{Q}\hat{Q^*}$ is hermitian)**
- and the **complement projects onto the space orthogonal to range**$\hat{(Q)}$ 


An important special case of orthogonal projectors is the rank-one orthogonal projector that isolates the component in a single direction $q$ , which can be written
$$\tag{6.8} P_q = qq^*$$
these are the pieces from which higher rank projectors can be made,
as in (6.7).
- their complements are the rank $m-1$ orthogonal projectors that eliminate the component in the direction of $q$: 
- $$\tag{6.9} p_{\perp q} = I - qq^*$$ 
- these equations assume that q is a unit vector
- For arbitrary nonzero vectors $a$, 
	- the analogous formula are
	- $$\tag{6.10} P_a = \cfrac{aa^*}{a^*a}$$
	- $$\tag{6.11} P_{\perp \, a} = I - \cfrac{aa^*}{a^*a} $$ ^bf2070


#### **Projection with an Arbitrary Basis**

An orthogonal projector onto a subspace of $\mathbb{C}^m$ can also be 
- constructed beginning with an arbitrary basis, (non necessarily orthogonal)

Suppose that the subspace is spanned by the linearly independent vectors $\{a_1, \cdots, a_n\}$ 
and let $A$ be the $m\times n$ matrix 
- whose $j^{th}$ columns is $a_j$.

In passing from $v$ to its orthogonal projection $y\in range(A)$  
- the difference $y-v$ must be orthogonal to $range(A)$
This is equivalent to the statement that $y$ must satisfy $a_j^*(y-v) = 0$ for every $j$, 
- or equivalently, $A^*(Ax-v) = 0$ or $A^*Ax = A^*v$ 
Since $A$ has full rank, $A^*A$ is nonsingular.
Therfore,
$$\tag{6.12} x = (A^*A)^{-1} A^* v$$
Finally, the projection of $a, y = Ax$ is $y = A(A^*A)^{-1}A^*v$ 
Thus, the orthogonal projector onto $range(A)$ can be express by the formula,
$$\tag{6.13} P = A(A^*A)^{-1}A^*$$
*Note :* 
this is a multidimensional generalization of *6.10* 
In the orthonormal case $A = \hat{Q}$, 
- the term in thee parentheses collapses to the identity and we recover *6.6*


# **Exercises**

### **6.1**
***
If $P$ is an orthogonal projector, then $I-2P$ is unitary.
Prove this algebraically, and give geometric interpretation. 
***
*Solution :*
If $P$ is a projector
	then $I-2P$ is also a projector
		for it is also idempotent: from definition above
$$
\begin{aligned}
(I-2P)^2&= I- 4P + 4P^2\\
&= I-2P
\end{aligned}$$

Are we tryin to say that the complementary projector to $P$ is unitary? 

Assuming $P$ is orthogonal,
	Thus, we are assuming that 
		$P = P^*$ 

If $P = P^*$
	then the inner product between vector $Px \in S_1$ and a vector $(I- P)y\in S_2$ is zero. 

### **6.2**
Let $E$ be the $m\times n$ matrix that extracts the "even part" of an $m-\text{vector}$ :
$Ex = \cfrac{(x+Fx)}{2}$, 
- where F if the $m \times m$ matrix that flips $(x_1, \cdots, x_m)^*$ to $(x_m, \cdots, x_1)^*$.
Is $E$ an orthogonal projector, an oblique projector, or not a projector at all? 
What are it's entries?

*Solution :*

### **6.3**
Given  $A\in\mathbb{C}^{m\times m}$ with $m\gew n$, Show that $A^*A$ is non singular if and and only if $A$ has full rank.

*Solution :*

### **6.4**
Consider the matrices, 
$$
A = 
\begin{bmatrix}
1 & 0\\
0 & 1\\
1 & 0
\end{bmatrix},
\quad
\quad
B = 
\begin{bmatrix}
1 & 2\\
0 & 1\\
1 & 0
\end{bmatrix}
$$
(a) What is the orthogonal projector $P$ onto $range(A)$, 
and what is the image under $P$ of the vector $(1, 2, 3)^*$?

*Solution :*

(b) Same question for $B$

*Solution :*

### **6.5**
Let $P\in\mathbb{C}{m\times m}$ be nonzero projector.
Show that $\|P\|_2 \geq 1$, 
with quality if and only if $P$ is an orthogonal projector. 

*Solution :*