
## 1
***
Is the following argument valid?
	If yes, show why by applying rules of inference to arrive at the conclusion.
	If not, show that the conclusion can be false while all the hypotheses are true.
$$
\begin{array}{}
p \to q \\
q \lor s \to r \\
p \\
\hline \\
\therefore r
\end{array}
$$
$$
\begin{align}
&1. \ &  &p \to q & \quad &\text{hypothesis }\\
&2. \ &  &p & \quad &\text{hypothesis}\\
&3. \ & &q & \quad &\text{modus pones (2.) and (1.)}\\
&4. \ & &q \lor s \to r & \quad &\text{hypothesis}\\
&5. \ & &q \lor s & \quad &\text{generalization (4.)}\\
&6. \ & &\therefore r & \quad &\text{modus pones (4.) and (5.)}\\
\end{align}
$$
Thus, the argument is valid.

## 2
***
$P(x)$ means $x$ is prime. 
$E(x)$ means $x$ is even
Use quantifier logic to generate the statement:
$$\text{'There is exactly one prime that is even'}$$
***
**Solution :**
***
Exactly one means 
	at least one 
		and 
			at most one
this is the at least one portion
$$\exists x \mid P(x) \land E(x)$$
lets do at most
$$\forall y \mid [E(y) \land P(x) \implies x = y]$$
Combine them:
$$\exists x \mid [P(x) \land E(x)\land \forall y \mid[E(y) \land P(y) \implies x = y]]$$
So exactly one is hence defined.
***
# 3
***
Prove that the square of an odd integer is an odd integer
***
**Solution :**
***
$$
\begin{align}
x^{2}&=2k+1 \quad \text{where } x \text{ is an odd integer}\\
(2k+1)^{2} &= (2k+1)\\
4k^{2}+4k+1 & = 2k+1\\
2(2k^{2}+2k)+1 &= 2k+1
\end{align}
$$
Notes:
	**Notice** that $4k^{2}+4k$ is even since $\cfrac{4k^{2}+4k}{4}=k^{2}+k$
	and when you add $1$ to an even number you obtain an odd number.
	**Notice** that we could've taken the contrapositive form, and solved for evens.
		Normal form:
			  Let $x$ be an integer. Prove that $x^{2}$ is an odd integer, if an only if $x$ is an odd number
		Contra positive form : 
			If $x$ is even then $x^{2}$ is even
## 8
***
A borrower takes a loan of amount $X$ with monthly interest rate of $r$.
The loan is taken at month $0$, a payment of amount $Y$ is made at the start of each month, starting at month $1$.

A) Give a recursive relation and a base case that define the sequence that gives the remaining balance on the borrower account. after the kth payment
B) Which monthly payment value $Y$ causes the loan balance to stay the same each month? Find it in terms of $X$ and $r$
***
**Solution :**
***
$P_{k} = \left[P_{k-1}\cdot\left(1+r\right)\right]-Y$
$P_{0}=X$
monthly payment is the monthly interest times the current balance before the payment is made

what ever part of a payment not interest is the principle

Interest amount at the K-th 

Balance after the k-th payment 
$B_{k}=B_{k-1}-p+i_{k}$
	$B_{k}$ balance after the k-th payment
	$B_{k-1}$ previous month balance after payment.
	$p$ monthly payment
	$i_{k}$ the interest amount at the the k-th payment
		$i_{k}=m \cdot B_{k-1}$
			$m$ is the monthly interest rate
			$B_{k-1}$ is the previous balance

To define it into a sequence 
$$
\begin{align}
B_{k}&=B_{k-1}-p+m \cdot B_{k-1}\\
&= (m+1)\cdot B_{k-1} - p
\end{align}
$$
then base case is $B_{0} = X$
	where $X$ is the loan amount

**Part B**

so next months monthly balance must be same as previous month,
$B_{k-1}=B_{k}=B_{k+1}$ after payment


$$\sum_{j=1}^{n} \ j(j-1) = \cfrac{n(n^{2}-1)}{3}$$
