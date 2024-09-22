# **Proofs Involving Divisibility Of Integers**

$a$   **Divides**   $b$ 
- if there is an integer $c$ such that 
	- $b = ac$
	- we write $a\vert b$ 
		- $b$ is a **multiple** of $a$ (linear combination)
		- $a$ is a **divisor** of $b$

#### **Result 4.1**

Let $a, b$ and $c$ be integers 
- with $a\neq 0$ and $b\neq0$ 
If $a\vert b$ and $b\vert c$ then $a\vert c$ 

*Proof :* 
Assume, that  $a\vert b$ and $b\vert c$ 
Then $b = ax$ and $c = by$ , where $x, y\in\mathbb{Z}$ 
Therefore, 
$$
\begin{aligned}
c &= by\\
&= (ax)y\\
&= a(xy)
\end{aligned}
$$
Since, $xy$ is an integer $a\vert c$ 

#### **Result 4.2**

Let $a, b$ and $c$ be integers 
- with $a\neq 0$ and $b\neq0$ 
If $a\vert c$ and $b\vert d$ then $ab\vert cd$ 

*Proof :*
Let $a\vert c$ and $b\vert d$
Then, $c = ax$ and $d = by$, where $x, y\in\mathbb{Z}$ 
Then,
$$
\begin{aligned}
cd &= (ax)(by)\\
&= (ab)(xy)
\end{aligned}
$$
Since, $xy$ is an integer, $ac\, \vert \, cd$ 

#### **Result 4.3**

Let $a, b, c, x, y\in\mathbb{Z}$, where $a\neq 0$ 
If, $a\vert b$ and $a\vert c$, then $a \vert (bx+cy)$ 

*Proof :*
Assume $a\vert b$ and $a\vert c$
Then, $b = ar$ and $c = as$ where $r, s \in \mathbb{Z}$ 
Then, 
$$
\begin{aligned}
bx+cy &= (ar)x + (as)y\\
&= a(rx+sy)
\end{aligned}
$$
Since, $rx+sy$ is an integer, $a \vert (bx+cy)$ 

#### **Result 4.4**

Let $x\in \mathbb{Z}$ 
If $2\vert (x^2-1)$, then $4\vert (x^2-1)$

*Proof :* 
Assume that $2\vert (x^2-1)$
So, $x^2-1 = 2y$ for some integer $y$.
Thus $x^2 = 2y+1$ is an odd integer.
It then follows, that $x$ too is odd.
Hence, $x = 2z+1$ for some integer $z$.
Then 
$$
\begin{aligned}
x^2-1 &= (2z+1)^2-1\\
&=(4z^2+4z+1)-1\\
&=4z^2+4z\\
&=4(z^2+z)
\end{aligned}
$$
Since, $z^2+z$ is an integer, $4\vert (x^2-1)$ 




