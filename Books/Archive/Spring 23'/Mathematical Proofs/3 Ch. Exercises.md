3.1 Let $x\in \mathbb{R}$. Prove that if $0<x<1$, then $x^2 -2x + 2 \ne 0$ 
***
*Solution:* 

$$
\begin{aligned}
x^2-2x+2 &=\\
&=(x^2-1)+1 \geq 1
\end{aligned}
$$
It follows that $x^2 -2x + 2 \ne 0$ for all $x\in \mathbb{R}$ 
***

3.2 Let $n \in \mathbb{N}$. 
Prove, $$|n-1| +|n+1| \leq 1 \Rightarrow |n^2-1| \leq 4$$
***
*Solution : *

Since natural numbers start from 1, all absolute values will never be negative, Hence, 
$$
\begin{aligned}
|n-1| +|n+1| &= n - 1 + n + 1\\
&= 2n\\
&= 2\\
&\text{thus,}\\
2 &> 1
\end{aligned}
$$
Since, out hypothesis is false,
our implication is true regardless if the conclusion is true or false
***

3.3 Let $r\in \mathbb{Q}^+$.
Prove,  $$\cfrac{r^2+1}{r}\leq 1 \Longrightarrow \cfrac{r^2+2}{r} \leq 2$$
***
$$
\begin{aligned}

\end{aligned}
$$
***

max := a[1]
for i := 2 to n
	if max < a[i]
		max := a[i]
end for

return max

for the given algorithm, 
	on each iteration of the for-loop
		we compare max to a[i] exactly once
			thus, we execute 1 operation per iteration of the for loop
				**Number of operation per iteration = 1**

Now,
	i can take on values from 2 to n 
		which are n-2 + 1 = n - 1 possible values
			thus the loop is iterated n-1 times
				**Number of iterations = n - 1**

The total number of operations 
	is then the product 
		of operations per iteration of the for-loop 
			and the number of iteration of the for-loop
				**Number of operations = Number of operations per iteration X Number of Iterations**
					**1 x (n - 1)**
					**n - 1**

By the theorem on polynomial orders, 
	**n - 1**
		is $\Theta (n)$ 
			so, this algorithm segment has order $n$


(9). 
s := 0
for i:= 1 to n
	for j := 1 to 2n
		s := s + i$\cdot$j  
	end-for
end-for

for each loop that iterates n times
	these is a inner for loop that iterates 2n times
		and inside the inner loop is a addition and multiplication operation
thus, there is n * 2n * n elementary operations 


(13)
for k := 1 to n-1
	max := a[k]
	for i := k + 1 to n 
		if max < a[i] 
			max := a[i]
a[k] := max

on each iteration of the inner for loop:
	we execute the comparison once
		which contains 1 comparison
			thus, we execute 1 operation per iteration of the inner for loop
				**Number of operation per iteration = 1**

for the inner for loop, i , can take on values from k + 1 to n
	which are 
		n - (k + 1) + 1 = n - k possible values
			thus, the for-loop will have n - k iterations where k can range from 1 to n-1

$$
\begin{aligned}
\text{Number of Iterations} &= \sum_{k = 1}^{n-1} (n - k)\\
&= \left(\sum_{k = 1}^{n - 1}n\right)+\left(\sum_{k = 1}^{n - 1}k\right)\\
&= n \cdot \left(\sum_{k = 1}^{n - 1}1\right) + \cfrac{(n-1)((n-1)+1)}{2}\\
&= n \cdot (n-1) + \cfrac{(n-1)n}{2}\\
&= n^2 - n + \cfrac{(n-1)n}{2}\\
&= n^2 - n + \frac{1}{2}n^2-\frac{1}{2}n\\
&= \frac{3}{2}n^2 - \frac{3}{2}n \quad \text{: number of total operations}
\end{aligned}
$$

order $n^2$ or $\Theta (n^2)$ 


n iterations where n can range from 1 to n 