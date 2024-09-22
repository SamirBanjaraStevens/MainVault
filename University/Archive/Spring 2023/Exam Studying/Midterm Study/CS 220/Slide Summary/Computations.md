Pseudo Code

Example : Find maximum in a finite sequence

max := a_1
for i := 2 ... n do
	if max < a_i
		then max := a_i
	end if
end for
return max


Example: Linear search (return the index of a particular number in sequence)

i := 1
while (i $\leq$ n and x $\neq$ a_i) do
	i := i + 1
end while 
if i $\leq$ n 
	then location := i
else 
	location := 0
end if
return location 





Example : Binary Search 


i := 1
j := n
while (i $\leq$ j) do
	m := $\lfloor(i+j)/2\rfloor$ 
	if x > a_m 
		then i : m + 1
	else
		j := m 
	end if
end while 
if (x == a_i)
	then location := i
else 
	location := 0
end if
return location 


**Worst-Case** 
- Number of basic operations as a function 
	- of the number of terms ($n$) in the sequence 

Worst case for linear algorithm occurs when the the element to be located is not included in the sequence

**Computational Complexity**
- Computation time
- memory storage

For $n$ elements, 
- the statement in the loop
	-  while ($i \leq n$ and $x\neq a_i$) do
		- i := i + 1
- is processed $n$ times requiring 5n elementary operations 

*complexity* is express as a function $n\rightarrow f(n)$ 
-  $n$ is the size of the input
- $f(n)$ is either 
	- the *worst-case complexity* (maximum amount of resources that are need over all inputs of size n)
	- or a*verage-case complexity*

and *time complexity* is the number of required elementary operations on an input of size $n$

# zybook notes

The O notation serves as a <u> rough upper bound</u> for functions
- Disregarding constant and small input values.

The $\Omega$  notation provides a <u> lower bound </u>on the growth function 


| Function                                  | Name        |
| ----------------------------------------- | ----------- |
| $\Theta (1)$                              | Constant    |
| $\Theta (\log\log n)$                     | $\log \log$ |
| $\Theta (\log n)$                         | Logarithmic |
| $\Theta (n)$                              | Linear      |
| $\Theta (n \log n)$                       | $n \log n$  |
| $\Theta (n^2)$                            | Quadratic   |
| $\Theta (n^3)$                            | Cubic       |
| $\Theta (n^m) \quad {m \in \mathbb{Z}^+}$ | Power       |
| $\Theta (c^n), \quad c > 1$               | Exponential |
| $\Theta (n!)$                             | Factorial   |

computation complexity - resources used 
space complexity - memory used
time complexity 
- defined by a function $f : \mathbb{Z}^+ \rightarrow \mathbb{Z}^+$ 
	- such that $f(n)$ is the <u>Maximum number of atomic operations performed</u> by the algorithm on an input size of $n$  


Compute the sum

input : $a_1, a_2, \cdots, a_n$ 
- $n$ is length of sequence

output : The sum of the number in the sequence

sum := 0 /*(1 assignment operation)*/
For i = 1 to n /*(loop iterated n times)*/
	sum := sum + $a_1$ 
		/*(for loop tests i and increments i (2 operations))*/
		/*(1 addition and 1 for assignment)*/
End-for

return (sum) /*(1 operation for return)*/


$$
\begin{aligned}
f(n) &= \#\text{ number of operations on a sequence of length n}\\
f(n) &= 1 + n [2 + 2] + 1\\
&= 1 + 4n + 1\\
&= 4n +2
\end{aligned}
$$






upper bound - using (Big O) 
	must apply for every input of size n

lower bound
	(using $\Omega$ )
		- need only apply for at least one possible input of size n







