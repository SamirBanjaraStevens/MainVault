## **Q1**
Kira has two kids
- frank
	- frank has a daughter names Sarah
		- Sarah is mother of 
		- Judy 
		- and Ruben
- lola

Kira
	Frank 
		Sarah
			Judy 
			Ruben
	Lola

Write down the relation $R=\{(a, b) \ | \ a \text{ is the parent of } b \}$ 

$A = \{\text{Kira, Frank, Sarah, Judy, Ruben, Lola}\}$  
$\begin{aligned}A\times A = (Kira, Kira), (Kira, Frank), (Kira, Sarah), (Kira, Judy), (Kira, Ruben), (Kira, Lola)&\\ = (Frank, Frank), (Frank, Sarah), (Frank, Judy), (Frank, Ruben), (Frank, Lola)&\\ = (Sarah,Sarah), (Sarah, Judy), (Sarah, Ruben), (Sarah,Lola)&\\ = (Judy, Judy), (Judy, Ruben), (Judy, Lola)&\\ =(Ruben, Ruben), (Ruben,Lola)&\\ = (Lola, Lola)&\end{aligned}$  
As a matrix 
$$
A \times A =
\begin{bmatrix}
(\text{Kira, Kira}) & (\text{Kira, Frank}) & (\text{Kira, Sarah}) & (\text{Kira, Judy}) & (\text{Kira, Ruben}) & (\text{Kira, Lola}) \\
(\text{Frank, Kira}) &(\text{Frank, Frank})& (\text{Frank, Sarah})& (\text{Frank, Judy})& (\text{Frank, Ruben})& (\text{Frank, Lola})\\
(\text{Sarah, Kira}) & (\text{Sarah, Frank}) &(\text{Sarah, Sarah})& (\text{Sarah, Judy})& (\text{Sarah, Ruben})& (\text{Sarah,Lola})\\
(\text{Judy, Kira}) & (\text{Judy, Frank}) & (\text{Judy, Sarah}) & (\text{Judy, Judy})& (\text{Judy, Ruben})& (\text{Judy, Lola})\\
(\text{Ruben, Kira}) & (\text{Ruben, Frank}) & (\text{Ruben, Sarah}) & (\text{Ruben, Judy}) & (\text{Ruben, Ruben})& (\text{Ruben,Lola})\\
(\text{Lola, Kira}) & (\text{Lola, Frank}) & (\text{Lola, Sarah}) & (\text{Lola, Judy}) & (\text{Lola, Ruben}) & (\text{Lola, Lola})\\
\end{bmatrix}
$$

$R = \{(\text{Kira, Frank}), (\text{Kira, Lola}), (\text{Frank, Sarah}), (\text{Sarah, Judy}), (\text{Sarah, Ruben})\}$  
Relation $R$ as a adjacency matrix:
$$R =
\begin{bmatrix}
0 & 1 & 1 & 0 & 0 & 0\\
0 & 0 & 0 & 1 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 1 & 1\\
0 & 0 & 0 & 0 & 0 & 0\\
0 & 0 & 0 & 0 & 0 & 0\\
\end{bmatrix}$$

## **Question 2.1** 

- **Symmetric & AntiSymmetric & Transitive**

Let $R = \{\emptyset\}$ be a relation on a set 𝐴

Prove that
- if $A$ is non-empty, the empty relation is not reflexive on $A$ . 
- The empty relation is symmetric and transitive for every set $A$
Solution:

For a relation to be reflexive: 
- For all elements in $A$, they should be related to themselves.  $xRx$
	- Now in this case there are no elements in the Relation 
		- and as $A$ is non-empty no element is related to itself 
			- *Note:* Would also hold for $A = \emptyset$ 
			- But in that case the empty relation would be reflexive.
		- hence the empty relation is not reflexive.

So, As $A$ is not empty, there exists some element $a\in A$ 
- As $R$ is empty 
	- $aRa$ does not hold
- Hence $R$ is not reflexive
    
- Now for a set to be symmetric and transitive: 
- As these are conditional statements
	- if the antecedent is false the statements would be true. 
		- And as the relation is empty in both cases 
			- the antecedent is false 
		- hence the empty relation is symmetric and transitive.

## **Question 2.2**

- **Reflexive** & **Symmetric** & **Transitive** & **Equivalence Relation**
The complete relation $R = \mathbb{N}\times\mathbb{N}$ 
defined on the natural numbers. 

Imagine that set $\mathbb{N} = \{1, 2, 3, 4, 5. \cdots\} \quad \text{where } a\in\mathbb{N}$ 
then, $$\mathbb{N} \times \mathbb{N} = \begin{aligned}\{&(1,1), (1, 2), (1, 3), (1,\cdots),\\ &(2, 1), (2, 2), (2, 3), (2, \cdots),\\ &(3, 1), (3, 2), (3, 3), (3, \cdots)\}\end{aligned}$$ 
Then the relation $R$ is **Reflexive**, 
- because diagonal entires exists for all elements $a\in A$ 
- $(a, a)$

The relation $R$ is **Symmetric**, 
- because $(a, b) (b,a)$ for all $a$ and $b$

Transitive 
- $(a, b)(b, c)\rightarrow (a, c)$ 

## **Question 2.3**

- **Transitive**

The relation $R$ on integers where $aRb$ means $(a-2)<b$ 

$a$ minus $2$ is less than $b$ 

then $b$ minus $2$ is less than $c$


hence aRc hold true?  yes Transitive


can $aRb$ and $bRa$ hold true? no, hence not symmetric
Definitely not reflexive






## **Question 2.4**

- **Reflexive** & **Transitive**

The relation $R$ on $\{w, x, y, z\}$ where $R = \{(w, w), (x, y), (x, w), (x, x), (x, z), (y, y), (z, y), (z, z)\}$ 

Tabel! transitive and reflexive and symmetric tabel
| Column 1 | Column 2 | Reflexive | Symmetric | Transitive   |
| -------- | -------- | --------- | --------- | ------------ |
| (w, w)   | (w, w)   | (w, w)    |           |              |
| (x, y)   | (y, y)   |           |           | (x, y)       |
| (x, w)   | (w, w)   |           |           | (x, w)       |
| (x, x)   | (x, x)   | (x, x)    |           |              |
| (x, z)   | (z, z)   |           |           | (x, z)       |
| (x, z)   | (z, y)   |           |           | (x, y) |
| (y, y)   | (y, y)   | (y, y)    |           |              |
| (z, y)   | (y, y)   |           |           | (z, y)       |
| (z, z)   | (z, y)   |           |           | (z, y)       |
| (z, z)   | (z, z)   | (z, z)    |           |              |
|          |          | Yes       | No        | Yes             |

Reflexive, 
- Because it contains all (w, w),  (x, x), (y, y), and (z, z)

Symmetric
- Does not contain 

|            |               |     |
| ---------- | ------------- | --- |
| (w, x)     | (x, w)        |     |
| (w, y)     | (y, w)        |     |
| (w, z)     | (z, w)        |     |
| (y, w)     | (w, y)        |     |
| (y, x)     | (x, y)        |     |
| (y, z)     | (z, y)        |     |
| (x, w) (X) | (w, x) (Miss) |     |
| (x, y) (X) | (y, x) (Miss)  |     |
| (x, z) (X) | (z, x) (Miss) |     |
| (z, w)     | (w, z)        |     |
| (z, x)     | (x, z)        |     |
| (z, y) (X) | (y, z) (Miss) |     |

Transitive


## **Question 2.5**

- **Reflexive** & **Symmetric**

$aRb$ means $a^2 = b^2$

$a^2 = b^2$ is equivalent to $a = b$ , 

thus, it can only be reflexive, be the relation can only contian
$$
\begin{bmatrix}
(1, 1) & & & \\
& (2, 2) &  & \\
& & (3, 3) & & \\
& & & (4, 4) & \\
& & & & (5, 5)
\end{bmatrix}
$$

$1^2 = 1^2$
$2^2 = 2^2$
$3^2 = 3^2$ 
thus, the relation  is reflexive. 

is it antisymmetric?
- the definition for 
	- **Antisymmetric :**
		- If $a = b$ whenever $(a,b)\in R$ and $(b, a)\in R$  implies $x = y$

Taking $a^2 = b^2$ we can say that the given relation for set of integers $Z$ is reflexive because $a^2 = a^2$ and $b^2 = b^2$ will always hold true.

The relation is symmetric as well because $a^2 = b^2$ and $b^2 = a^2$
- so $aRb$ and $bRa$ holds 

Not transitive. 



