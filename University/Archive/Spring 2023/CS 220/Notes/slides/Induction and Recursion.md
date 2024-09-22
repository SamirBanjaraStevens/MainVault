## Induction

Consider the following problem

Prove that $n<2^{n}$ for all natural numbers $n$ 

We can check for $n = 0, 1, 2, 4, \dots$ 
	and it holds every time

$0<2^{0}\quad 1<2^{1}\quad 2<2^{2}\quad 3<2^{3}$

But this is not a proof because universal statemnets cannot be proven by examples:
- either show they apply to all number, 
	- cant do that because they lead to infinity
- or show one example that has a false statmetn to disprove it

**Idea:**
Lets assume it is true for $n=k$ 
	and show that it must also be true for $n=k+1$
	$$P(k)\rightarrow P(k+1)$$
***
The principle of mathematical indurction is useful tool for **proving** that a certain predicate is true for all natural numbers.

It cannot be used to discover theorems, but only to prove them.

***
If we have a propositional function $P(n)$
	and we want to prove that $P(n)$ is true for any natural number $n$ 
		we do the following.
			- Show that $P(0)$ or $P(1)$ is true (**Basis Step**)
			- Show that if $P(k)$ then $P(k+1)$ $k \in \mathbb{N}$ (**Inductive step**)
			- Then $P(n)$ must be true for any $n \in \mathbb{N}$ (**Conclusion**)
*3-step process*
***
**Show that $n<2^{n}$ for all natural nuimbers $n$**

Let $P(n)$ be the proposition "$n<2^{n}$"

*Basis Step*
1. Show that $P(0)$ or $P(1)$ is true
	1. $0<2^{0}=0<1, \quad 1<2^{1}=1<2$
		1. thus, $P(0)$ and $P(1)$ is true.

*Inductive Step*
1. Show that if $P(k)$ is true then $P(k+1)$ is true (*inductive step*) 
	1. Aussume that $k<2^{k}$ is true
		1. Show that $P(k+1)$ is true 
			1. $k+1<2^{k+1}$
$$
k<2^{k}\rightarrow k+1<2^{k+1}
$$
Since $2^{k+1}=2^{k}+2^{k}=2\cdot 2^{k}$
we can say, $$k<2^{k}\rightarrow k+1<2^{k+1}\leq 2^{k}+2^{k}=2^{k+1}$$
Thereforem if $k<2^{k}$ then $k+1<2^{k+1}$

*Conclusion*
Then $P(n)$ must be true for any natural number 

**QED**
***
## Example

Prove
$$1+2+\cdots = \sum_{i=1}^{n} \ i = \cfrac{n(n+1)}{2}$$
1. *Basis step*
	- Show that $P(1)$
		- $P(1) = \cfrac{1(1+1)}{2} = 1$ (*True*)
2. *Inductive Step*
	- Show that if $P(k)$ is true then $P(k+1)$ is true (*inductive step*) 
- $$\sum_{i=1}^{k} \ i = \cfrac{k(k+1)}{2} \rightarrow \sum_{i=1}^{k+1} \ i = \cfrac{k+1(k+2)}{2}$$
$$
\begin{align}
1 + 2 + 3 + \cdots + k &= \cfrac{k(k+1)}{2}\\
1 + 2 + 3 + \cdots + k + k+1 &= \cfrac{k+1(k+2)}{2}=\cfrac{k(k+1)}{2}+(k+1)\\
&= \cfrac{k(k+1)}{2}+\cfrac{2(k+1)}{2}\\
&= \cfrac{k(k+1)+2(k+1)}{2}\\
&=\cfrac{(k+1)(k+2)}{2}
\end{align}
$$
3. Then $P(n)$ must be true for any $n\in \mathbb{Z}^{+}$ (*Conclusion*)
***

## Second Priciple of Mathematical Induction

There is another proof technique that is very similar to the priceple of mathrmatical induction, 
	called the **Second Principle of Mathematicla Induction** 

It can be used to show that a propositional function $P(n)$ is true for any natural number $n$ 

**Second Principle of Mathematicla Induction**
***
1. Show that $P(0)$ is true (*Basis Step*)
2. Show that **If $P(0)$ and $P(1)$ and ... and $P(k)$ are true** then $P(k+1)$ is true for any $k\in \mathbb{N}$ *(inductive step)*
3. Then for $P(n)$ must be true for any $n\in \mathbb{N}$ (*Conclusion*)
***

## Example 

```ad-note
title: Example
Show That every integer greater than $1$ is either a prime number or can be written as the product of primes.
```

1. Show that $P(2)$ is true. *(Bassi Step)* $2$ is prime
2. Show that if $P(2), P(3), \dots, P(k)$ are true then $P(k+1)$ is true for any $k \in \mathbb{N}$ (*Inductive step*)
	- Two possible cases: if $k+1$ is prime, then obviously $P(k+1) is true$
	- If $k+1$ is composite, it can be written as a product of two integers $a$ and $b$ such that $2\leq a\leq b< k+1$ 
	- By the induction hypothesis, both $a$ and $b$ can be written as the product of primes.
	- Therfore $k+1 = a * b$ can be written as the product of primes
3. Then $P(n)$ must be true for any $n \in \mathbb{N}$ with $n>1$ (*Conclusion*)
**QED**