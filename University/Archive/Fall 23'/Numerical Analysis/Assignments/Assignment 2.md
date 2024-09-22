## Question 1

Study the method of **False Positions** 
	Write python script to implement the **False Positions** *algo*.

Apply the algorithm 
	as well as the **Newton's algorithm** 
		to find the roots of the polynomial  
$$f(x) = 230x^{4}+18x^{3}+9x^{2}-221x-9$$
			in the intervals 
				1. $[-1, 0]$
				2. $[0, 1]$
Attempt to approximate the roots within $10^{-6}$ using each method.
You may use the *end points of each interval* 
	as initial approximation for the method of **False Positions** 
		and use the *mid-point* 
			for **Newton's method**.
Tabulate your findings in a pandas data frame 
	and insure that the roots 
		are bracketed by the **method of False Position**
***
#### Solution:

Lets start by rough drafting a simple python script.

```Python
if
```

***
## Question 2

Let $f(x) \in C \, [a,b]$ and let $p \in  [a,b]$

1. Suppose that $f(p)\neq 0$
	show that there is a $\delta > 0$ with $f(x) \neq 0$ 
		for all $x \in[p-\delta, p + \delta]$ 

2. Suppose that $f(p) = 0$ and $k>0$ is given,
	Show that there is a $\delta>0$ with $f(x)\leq k$
		for all $x \in[p-\delta, p + \delta]$ 

***
#### Solution:

1. 
Given that $f(x)$ is continuous on $[a, b]$ and $f(p) \neq 0$, by the property of continuity functions, $f(x)$ is continuous at $x = p$. This means that for any $\epsilon >0$, there exists a $\delta > 0$ such that if $0<\left|\, x - p \,\right| < \delta$ then $\left|\, f(x) - f(p) \,\right| < \epsilon$ 

Now choosing $\epsilon = \cfrac{\left|\, f(p) \,\right|}{2}$ 
	This ensure that $f(x)$ does not change sign in the interval $(p-\delta, p + \delta)$, because the difference between $f(x)$ and $f(p)$ is less than half the magnitude of $f(p)$.

Given $\left|\, f(x) - f(p) \,\right| < \cfrac{\left|\, f(p) \,\right|}{2}$
this implies, $\left|\, f(x) \,\right|> \cfrac{\left|\, f(p) \,\right|}{2}$ 
since, $\cfrac{\left|\, f(p) \,\right|}{2} > 0$
	Thus, it follows that there exists a $\delta >0$ such that $f(x)\neq 0$ for all $x \in[p-\delta, p+\delta]$
***
2.
Given that $f(x)$ is continuous on $[a, b]$ and $f(p) = 0$, by the property of continuity functions, $f(x)$ is continuous at $x = p$. This means that for any $\epsilon >0$, there exists a $\delta > 0$ such that if $0<\left|\, x - p \,\right| < \delta$ then $\left|\, f(x) - f(p) \,\right| < \epsilon$ 

Choose $\epsilon = k$
	Ensure that the difference between $f(x)$ and $f(p)$ is less than $k$
Given $\left|\, f(x) - f(p) \,\right|< k$ and $f(p) = 0$,
the inequality becomes
	$|f(x)| < k$, which implies $f(x) \leq k$
Thus, there exists a $\delta > 0$ such that $f(x)\leq k$ for all $x \in[p-\delta, p+\delta]$
***