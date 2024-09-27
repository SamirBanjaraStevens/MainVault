Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Signature: Samir Banjara
# Question 1 
Determine whether each sequence is convergent or divergent. If convergent find the limit.
### a)
$$\lim_{ n \to \infty } ne^{-n}$$
***
**Solution:** 
First lets convert it,
$$\lim_{ n \to \infty } ne^{-n} \implies \lim_{ n \to \infty } \frac{n}{e^{ n }}$$
Taking the limit give us the indeterminate form,
$$\lim_{ n \to \infty } \frac{n}{e^{ n }}=\frac{\infty}{\infty}$$
We can use L' Hopital's rule and take the derivative of both the numerator and denominator, which give us, $\lim_{ n \to \infty } \frac{1}{e^{ n }}$, and then we can take the limit again.
$$\lim_{ n \to \infty } \frac{n}{e^n}:=\lim_{ n \to \infty } \frac{1}{e^{ n }}=\frac{1}{e^{ \infty }} = 0$$

### b)
$$\lim_{ n \to \infty } \cfrac{\sin^2n}{n+3}$$
***
**Solution:** 
We can use the squeeze theorem to derive the limit.
-  Setting up bounds.
	- For all,$\forall$, real, $\mathbb{R}$, number $n$, $\forall \ n \in \mathbb{R}$,
$$-1\leq \sin n \leq 1$$
		- Squaring both sides 
$$0\leq \sin^2n \leq 1$$
This is because $\sin n$ oscillates between $-1$ and $1$, so $\sin^2n$ oscillates between $0$ and $1$.

Divide the inequality by $n+3$,
- Since $n+3$ is positive for all $n\geq 1$, we can divide the inequality without changing the direction of the inequality:
$$0\leq \cfrac{\sin^2n}{n+3}\leq \cfrac{1}{n+3}$$
Consider the Sequence for the Lower and Upper Bounds
- Lets us define
	- Lower bound sequence: $a_{n}=0$
	- Upper bound sequence: $b_{n}=\cfrac{1}{n+3}$
	- Given sequence: $c_{n} = \cfrac{\sin^2n}{n+3}$

So we have:
$$a_{n}\leq c_{n}\leq b_{n} \ \ \text{for all} \ n \geq 1$$
- Computing the limits of the Lower and Upper bound as $n \to \infty$:
	- Lower bound:
$$\lim_{ n \to \infty } a_{n} = \lim_{ n \to \infty } 0 = 0$$
	- Upper bound:
$$\lim_{ n \to \infty } b_{n} = \lim_{ n \to \infty } \cfrac{1}{n+3}=0$$

Application of Squeeze Theorem (Sandwich Theorem)':
The Squeeze Theorem states that if $a_{n}\leq c_{n}\leq b_{n}$ for all $n$ beyond some index $N$, and if:
$$\lim_{ n \to \infty } a_{n} = L = \lim_{ n \to \infty } b_{n}$$
then,
$$\lim_{ n \to \infty } c_{n} = L$$
Since both the Lower and Upper bounds converge to $0$ it follows that,
$$\lim_{ n \to \infty } \cfrac{\sin^2n}{n+3} = 0$$

### c)
$$\lim_{ n \to \infty } \cfrac{5n^2+2}{3n^2+3}$$
***
**Solution:** 
First, lets divide all terms in the numerator and denominator by $n^{2}$, which is the greatest power in the denominator.
$$\lim_{ n \to \infty } \cfrac{\frac{5n^2}{n^2}+\frac{2}{n^2}}{\frac{3n^2}{n^2}+\frac{3}{n^2}} \implies \lim_{ n \to \infty } \cfrac{5+\frac{2}{n^2}}{3+\frac{3}{n^2}}$$
Then we can take the limit,
$$\lim_{ n \to \infty } \cfrac{5+\frac{2}{n^2}}{3+\frac{3}{n^2}}=\cfrac{5+\frac{2}{\infty^2}}{3+\frac{3}{\infty^2}}=\cfrac{5+0}{3+0}=\frac{5}{3}$$
# Question 2
### a) 
Express the repeating decimal $0.45454545\dots$ as a geometric series.
***
**Solution:** 
$$.454545\ldots=0.45+.0045+.000045+\dots=\sum_{n=1}^{\infty}0.45\cdot(0.01)^{n-1}$$

### b)
***
**Solution:**
This is a geometric series with common ratio $r=0.01$, and initial term $a=0.45$.

Since $|r|<1$, this series converges.

$$0.454545\ldots=\text{sum}=\cfrac{a}{1-r}=\cfrac{0.45}{1-(0.01)}=\cfrac{0.45}{0.99}=\cfrac{45}{99}=\frac{5}{11}$$
# Question 3
### a) 
Prove that if $\sum_{n=0}^{\infty}a_{n}$ converges and $\sum_{n=0}^{\infty}b_{n}$ diverges, then $\sum_{n=0}^{\infty}(a_{n}+b_{n})$ diverges. 

**Hint:** To derive a contradiction assume $\sum_{n=0}^{\infty}(a_{n}+b_{n})$ converges and consider $\sum_{n=0}^{\infty}(a_{n}+b_{n})-\sum_{n=0}^{\infty}a_{n}$
***
**Solution:** 
We know through through the Algebraic Property of Convergent Series (Linearity of Series) that if two series $\sum a_{n}$ & $\sum b_{n}$ are convergent, then the following linear combination of series is also convergent.
$$
\begin{align}
\sum(a_{n}+b_{n})&=\sum a_{n} + \sum b_{n} \\
\sum(a_{n}-b_{n})&=\sum a_{n} - \sum b_{n}
\end{align}
$$
$\textbf{Proof:}$

Assume $\sum(a_{n}+b_{n})$ is convergent.

Given that $\sum a_{n}$ is convergent, by the Linearity of Series, we can say that $\sum(a_{n}+b_{n})-a_{n}=\sum b_{n}$ converges.

This contradicts the given information $\sum b_{n}$ is divergent.

$\textbf{Conclusion:}$
Therefore, by contradiction the initial assumption was incorrect and $\sum(a_{n}+b_{n})$ is divergent.
### b)
Is the series $\sum_{n=0}^{\infty} \cfrac{n+(-1)^n}{n^2}$ convergent or divergent? Explain!
***
**Solution:** 

$\textbf{Proof:}$

First, we observe that for all $n\geq 1$:
$$
\sum_{n=0}^{\infty}\cfrac{n+(-1)^n}{n^{2}}=\cfrac{n}{n^{2}}+\cfrac{(-1)^n}{n^2}
$$
The first series $\sum_{n=0}^\infty \frac{n}{n^2}$ is equivalent to the harmonic series, $\sum_{n=0}^\infty \frac{1}{n}$, which is divergent.

The second series $\sum_{n=0}^\infty \frac{(-1)^n}{n^2}$, is a convergent alternating series.

We can rewrite it as,
$$S = \sum_{n=0}^{\infty}\cfrac{n+(-1)^n}{n^{2}}=\cfrac{n}{n^{2}}+\cfrac{(-1)^n}{n^2}=\frac{1}{n}+\cfrac{(-1)^n}{n^2}$$
Thus the series can be expressed as the sum of two series by the Linearity of Series. The partial sums of the original series is shown bellow,
$$
\begin{align}
S_{N} &= \sum_{n=0}^{\infty} \cfrac{n+(-1)^n}{n^2} \\
&=\sum_{n=0}^{\infty}\cfrac{n}{n^{2}}+\cfrac{(-1)^n}{n^2} \\
&=\sum_{n=0}^{\infty}\frac{1}{n}+\cfrac{(-1)^n}{n^2} \\
&=\sum_{n=0}^{\infty} \cfrac{1}{n}+\sum_{n=0}^{\infty}\cfrac{(-1)^n}{n^2}
\end{align}
$$
1. Divergence of the first partial sum $H=\sum_{n=0}^{\infty}\frac{1}{n}$:

The series $H=\sum_{n=0}^{\infty}\frac{1}{n}$ is a harmonic series that diverges to infinity as $N$ approaches infinity. 

This is easily seen by the integral test.
$$
\int_{1}^\infty \frac{1}{x}\, dx = \lim_{ t \to \infty }  \ln t-\ln 1 = \infty
$$

2. Convergence of $\sum_{n=0}^{\infty}\cfrac{(-1)^n}{n^2}$:

Conditions for the alternating series test $A = \sum_{n=0}^{\infty}\cfrac{(-1)^n}{n^2}$ :
- Let $b_{n}=\cfrac{1}{n^{2}}$
- $b_{n+1}>0$ for all $n\geq 1$
- $b_{n+1}=\cfrac{1}{(n+1)^2}< \cfrac{1}{n^2}=b_{n}$
	- Thus $\{b_{n}\}$ is a decreasing sequence.
- $\lim_{ n \to \infty }b_{n}=0$ 

By the Alternating Series Test, the series $A$ converges.
- Moreover, since the series $\sum_{n=0}^\infty b_{n}$ converges, which is a $p\text{-series}$, with $p=2>1$, the series $A$ converges absolutely.

Lets say that it converges to some finite value, say $L$

$\textbf{Conclusion:}$ 
The sum of a divergent series and a convergent series is divergent. 

Because for any $M>0$, there exists $N$ such that,
$$
\sum_{n=0}^N \cfrac{n}{n^2} > M - L
$$
Adding the convergent alternating series to both sides, we get,
$$
S_{N} = \sum_{n=0}^N \cfrac{n+(-1)^n}{n^2}>M
$$
Which shows that the partial sums of the original series can be made arbitrarily large, implying that the series $S = H + A$ is divergent. 

Thus, the series $\sum_{n=0}^{\infty} \cfrac{n+(-1)^n}{n^2}$ is divergent. 