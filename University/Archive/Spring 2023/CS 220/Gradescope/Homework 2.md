Proofs

## Question 1
### Provide A direct proof for the following theorem.
#### If $x$ and $y$ are positive real numbers and $x < y$, then $x^2 < y^2$.
##### Proof: 
$$\,(\,(x, \,y \in \mathbb{R}^{+}\,) \land \,(x < y\,)\,) \rightarrow \,(x^{2} < y^{2}\,)$$

Since, $x^{2}$ is positive multiply both side of the the inequality $x < y$ by $x$ to get $x^{2} < xy$

Since, $y^{2}$ is positive multiply both sides of the inequality $x < y$ by $y$ to get $xy < y^{2}$

Therefore, $x^{2} < xy < y^{2} = x^{2} < y^{2}$
QED 

## Question 2
### Provide an indirect proof of the following theorem.
#### For every integer $n$, if $n^{2}$ if not divisible by 4, then $n$ is odd.
##### Proof: by contra positive.
$p \rightarrow q$  : *if $n^{2}$ if not divisible by 4, then $n$ is odd*
$p  :$ n^2 is not divisible by 4, (  $4\nmid n^{2}$ )
$q :$ n is odd, ( $n = 2k+1$ )

Contrapositive : **$\lnot q \rightarrow \lnot p$**
So, $\lnot p : 4 \mid n^{2}$ ("4 divides $n^{2}$")
and, $\lnot q : n = 2k$ (n is even)

Prove of contrapositive :

Assume $n$ is even,
then, $n^2$ is divisible by $4$, given by contrapositive.

Since n is even, $n = 2k$ for some integer $k$, by definition of parity for even integers.
Substitute $2k$ for $n$ in $n^{2}$
$(2k)^{2} = 4 \cdot k^{2}$

Since, k is an integer so is $k^{2}$, by product of integer
because there exists some integer, $c$ such that $b = ac$. 

$n^{2}$ is 4 times some integer $k^{2}$, $n^{2}$ is divisible by 4. 
QED


## Question 3
### Is it true that the sum of two positive irrational numbers is also irrational? Prove your answer.
##### Proof:
let $a$ be $\sqrt{3}$ and $b$ be $3 - \sqrt{3}$, both $a$ and $b$ are irrational.
The sum of of $a$ and $b$, $\sqrt{3} + \,(3 - \sqrt{3}\,) = 3$.
3 is a rational number, because it can be expressed as $\frac{a}{b}$ where $a$ or $b$ doesn't equal 0. 
The sum of two positive irrational numbers can be irrational, but it can also be rational. QED

## Question 4 
### If integers $x$ and $y$ have the same parity, then $x + y$ is even
#### NotesL the parity of a number tells whether the number is odd or even. If x and y have the same parity, they are either both even or both odd.
##### Proof:

Case 1: let $x$ and $y$ be even. 
$x = 2k_{1}$ and $y = 2k_{2}$, for some $k_{1}$ and $k_{2}$ elements of all integers.
$x + y = 2k_{1} + 2k_{2}$, 
which can be written as $x + y = 2 (k_{1} + k_{2})$,
let $k_{1} + k_{2} = m$
therefore, $x + y = 2(m)$, which is formula for even number 

Case 2: Let $x$ and $y$ be odd, 
$x = 2(k_{1})+1$ and $y = 2(k_{2})+1$, for some $k_{1}$ and$k_{2}$ elements of all integers.
$x + y = (2k_{1} + 1) + (2k_{2} +1)$ 
$x + y = 2k_{1} +2k_{2} + 2$
$x + y = 2\,(k_{1} + k_{2} + 1\,)$, 
let $k_{1} + k_{2} + 1 = m$ 
Therefore, $x + y = 2m$, which is formula for even number
