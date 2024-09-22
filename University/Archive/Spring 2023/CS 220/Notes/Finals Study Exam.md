## Question 1: Cardinality
***
How many distinct elements 
	does the set $S$ 
		contain in each case?

1. $S=\{ 7, 2, 3 \}\cup \{ 3, 1,2 \}$
2. $S=\{ (x,y), (y, z), (z,z) \}\cap \{ (y,x) (z, z), (y, y) \}$
3. $S=\{ A\mid(A \subseteq \{ 1, 2, 3, 4 \}\cap(|A|=5)) \}$ 
4. $S=\{ x\mid x^{2}+2x=8; x \in\mathbb{R} \}$ 
5. $S=\{ (a, b)\mid a<b \}; \ a,b\in\{ {1, 2,3} \}$ 
6. $S=E, \text{ where } G=(V, E) \text{ is a tree and } |V|=5$
7. $S=\{ G\mid G \text{ is a simple graph with } 4 \text{ vertices} \}$
8. $S=\{ R\mid R \text{ is a reflexive relation on } \{0,1\} \}$
9. $S=\{ n\mid(n \text{ is prime})\cap(n \text{ mod } 2=0) \}$
10. $S=\{ a, b, c, e \}-\{ b, c, d \}$

***
## Question 2: Equivalence Relations
***
Are the following relations 
	on the set of all people 
		equivalence relations?
If not, give a reason. 

1. $R=\{ (a,b) \mid a \text{ and } b \text{ are the same age }\}$
2. $R=\{ (a,b) \mid a \text{ and } b \text{ have the same parents }\}$
3. $R=\{ (a,b) \mid a \text{ and } b \text{ share a common parent }\}$
4. $R=\{ (a,b) \mid a \text{ and } b \text{ have met }\}$
5. $R=\{ (a,b) \mid a \text{ and } b \text{ speak a common language }\}$

***
## Question 3: Urns and Balls

**(A).** 
There is an urn 
	containing four blue balls 
		and four red balls. 
We randomly draw four balls from this urn 
	without returning any balls. 
What is the probability 
	that all of the four balls 
		that we drew 
			are blue?

**(B)** 
There are two urns, 
	each of them containing two blue balls 
		and two red balls. 
We  randomly draw two balls
	from the first urn 
		and then randomly draw two balls 
			from the second urn, 
				without returning any balls. 
What is the probability 
	that all of the four balls 
		that we drew 
			are blue?

**(C)**
There are four urns, 
	each of them containing one blue ball 
		and one red ball. 
We randomly draw one ball from each urn 
	without returning any balls. 
What is the probability 
	that all of the four balls 
		that we drew 
			are blue?

**(D)**
In each of the previous three experiments, 
	you calculated the probability 
		of randomly drawing exactly four blue balls 
			from a set of four blue 
				and four red balls. 
Explain in English words 
	why this probability changes 
		with the number of urns 
			as you observed it. 
Why does the probability 
	increase(?)/decrease(?) 
		with a larger number of urns 
			instead of being constant?

***
## Question 4: Rapid Reproduction
***
Somewhere in the forests 
	of Massachusetts, scientists 
		from UMass Boston discovered  
		two rare species of animals 
			named the Violent Squirrel 
				and the Sarcastic Cat. 
On their  first encounter with these animals, 
	the scientists found five animals 
		of each species. 
One year later, the scientists returned 
	and then found five Violent Squirrels 
		and 13 Sarcastic  Cats. 
The scientists somehow devised formulas 
	for the populations $v_{n}$ and $s_{n}$ 
		denoting the number of Violent Squirrels 
			and Sarcastic Cats, respectively
				in year $n$ for $n\geq 2$:
					$$v_{n}=n \cdot v_{n-1}$$
					$$s_{n}=4s_{n-1}+5s_{n-2}$$

**(A),**
Let us define that the species 
	were discovered in year $0$
		and, the second counting was done in year $1$
Use the above formulas to predict 
	the populations $v_{n}$ and $s_{n}$ 
		in the years $n=2, 3, 4, 5$

**(B)**
Find the explicit formulas for $v_{n}$ and $s_{n}$ $n\geq 2$
	that do not require iteration.
You should (but not have to) 
	check the correctness of the formulas using some of the results you obtained in **(A)**

**(C)**
Describe the growth of $v_{n}$ and $s_{n}$ 
	using the big-$\Theta$ notation 
		for each term.
In each,
	estimate $\Theta(f(n)), f(n)$ should 
		be the most suitable function 
			chosen from the following one:
$$
\begin{array}{}
\log(n), n, n \log(n), \\
n^{2},n^{3}, 2^{n}, \\
3^{n}, 4^{n},5^{n}, \\
 6^{n}, n!, n^{n}
\end{array}
$$

**(D)** 
In the year $1,000$ 
		will there be more Violent Squirrels
			than Sarcastic Cats,
	given that the populations
		develop as predicted?
Or will there be more Sarcastic Cats,
	than Violent Squirrels?
Do not try to compute the actual numbers!
Just tell which species you think will 
	have the larger population,
		and give the reason why you think so.
		
***
## Question 5: Possibilities
***
**(A)**
Paul wants to come to the U.S. 
	to first get his Bachelor’s degree, 
		then his Master’s degree, 
			and finally his Ph.D. 
He considers seven possible universities 
	for his studies, 
		but he does not want 
			to receive more than one degree 
				from the same university. 
How many different
		academic career paths 
			are possible for Paul, 
	assuming that he does not 
		switch universities during each program 
			and actually passes all three programs?

**(B)**
Ten years later,
	Paul becomes a professor at UMass Boston. 
He receives seven applications 
		from students who want to work 
			in his new Time Travel Lab, 
	but his research grants are limited, 
		and so he will hire only four of them. 
How many choices in the recruitment 
	of his research team does Paul have?
	
**(C)**
Paul’s most famous research article 
	is about four-letter strings 
		made up of the letters  ‘a’, ‘b’, and ‘c’. 
He discovers the number of such strings 
	in which an ‘a’ is never immediately 
		followed by another ‘a’ or a ‘b’, 
			and a ‘b’ or ‘c’ is never immediately  
				followed by a ‘c’. 
Use a tree diagram to replicate Paul’s finding. 
How many different strings 
	of this kind are there?

***
## Question 6: Lack of Isomorphism
***
**(A)**
![[Pasted image 20230429145338.png]]

**(B)**
![[Pasted image 20230429145521.png]]

**(C)**
![[Pasted image 20230429145603.png]]


**(D)**
![[Pasted image 20230429145618.png]]

**(E)**
![[Pasted image 20230429145634.png]]


***
## Question 7: About Trees
***
(A) 
If $T$ is a binary tree 
	with $41$ vertices
		its minimum height is ...........

**(B)**
If $T$ is a full binary tree 
	with $111$ vertices, 
		its maximum height is ..........

**(C)**
Every full binary tree 
	with $51$vertices
	has ....... leaves

**(D)**
Every full binary tree 
	with $60$ leaves
		has ........ vertices

**(E)**
Every full binary tree
	with $75$ vertices 
		has ....... internal vertices

**(F)**
A full $3$-ary tree 
	with $100$ internal vertices
		has ...... vertices

***
## Question 8 : Independence Day
***
**(A)**
Give an example 
	for two independent events.

Prove their independence.

**(B)**
Give an example 
	for two events 
		that are not independent 
Prove that they are not independent.