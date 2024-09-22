
Certain Problems types involving <u>rearrangements of distinct objects</u> (**"Permutations"**) 
or <u>ways to select subsets of particular size</u> ("**Combinations**") 

## Example

Determine the number of permutations (i.e., ways to rearrange) the six letters ABCDEF

- There are 6 letters to be arranged into 6 locations
- For the first letter 
	- there are 6 choices 
		- (any of ABCDEF)
- For the second letter, 
	- there are only 5 choices 
		- any of the letter excpet the one we have already chosen
- Continuing this way, 
	- we see that there are 4 choices for the third letter,
		- 3 choices for the fourth letter
			- 2 choices for the fifth letter
				- and only 1 choice for the last (sixth) letter
- By the multiplication princple,
	- the total number of permutations
		- is $6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1\cdot=710$ 

## Example

A new company has four design elements
	which must all be different colors chosen from red, orange, yellow, green, blue, and purple
		How many different logos are possible?

- There are 6 possible colors
	- the first design elemnet has 6 possible colors, 
		- the second had 5 possible colors
			- third has 4 possible colors
				- fourth has 3 possible colors
- Thus, the total number of logos is $6\cdot 5\cdot 4\cdot 3 = 360$ 
- Both of the problems are examples of computing **permutations** 
	- where we choose $k$ distinct items from a list of $n$ possibilities
		- where the order matters


## Proposition
**Permutation**

The number of ways of choosing $k$ ordered items from a list of $n$ distinct possibilities 
	(where the order of the $k$ items matter)
		is equal to $\cfrac{n!}{(n-k)!}$
			in particular the number of ways of rearranging $n$ distinct items in $n!$

## Example

A sports leauge has $31$ teams in total. 
	How many ways are there to choose $16$ tems that make the playoff?
		assuming the ranking of the playoff teams matters
			and there are no ties?

- We are choosing $k=16$  teams from $n=31$ list of teams 
	- thus the total number of choices is
		- $$\cfrac{31!}{(31-16)!}=\cfrac{31!}{15!}$$

## Proposition
**Combination** 

The number of ways of choosing $k$ unordered items from a list of $n$ distinct possibilities is equal to $\left( \begin{array}{} n\\ k \end{array} \right) = \ _{c}C_{k} = \cfrac{n!}{k!(n-k)!}$ 
- Remark,
	- the denotions are read as "$n$ choose $k$" 
- If we cant to count unordered lists,
	- we can simply observe that for any unordered list,
		- there are $k!$ ways to rerrange the $k$ elements on the list
- Thus, we have counded each unordered list $k!$ times,
	- so the number of unrdered lists is
		- $$\cfrac{1}{k!}\cdot\cfrac{n!}{(n-k)!}=\cfrac{n!}{k!(n-k)!}$$
- The numbers $\left( \begin{array}{} n \\ k\end{array} \right)$ are called **binomial coefficents**
	- because they arise s coefficents of binomial expansions

	- Specficially,
		- in the expansion of $(x+y)^{n}$, the coefficents of $x^{k}y^{n-k}$ is equal to $\left( \begin{array}{} n \\ k\end{array} \right)$ 
	- This follows by observing that in expanding the product $(x+y)\cdot(x+y)\dots(x+y)$
		- we may choose an $x$ or $y$ from each of the $n$ terms
			- The term $x^{k}y^{n-k}$ willl arise from products that choose exactaly $k$ terms equal to $x:$ 
	- For example,
		- we can compute that $(x+y)^{4}=x^{4}+4x^{3}y+6x^{2}y^{2}+4xy^{3}+y^{4}$ 
			- and the middle term is indeed equal to $\left( \begin{array}{} 4 \\ 2\end{array} \right)=\cfrac{4!}{2!2!}=6$
- Binomial coefficients show up in many different places,
	- and satsfiy many intresting algebraic identies
		- such as the "reflection identity" $\left( \begin{array}{} n \\ k\end{array} \right) = \left( \begin{array}{} n \\ n-k\end{array} \right)$ 
			- along with the recurrence $\left( \begin{array}{} n \\ k\end{array} \right)= \left( \begin{array}{} n-1 \\ k\end{array} \right)+\left( \begin{array}{} n-1 \\ k-1\end{array} \right)$
- In general, 
	- expanding the products of factorials is not the most efficent way to evaluate binomial coefficients.
		- Insted the formula $\left( \begin{array}{} n \\ k\end{array} \right)$ is typically more efficent

## Example

How many $3-$elements subsets of $\{ 1, 2, 3, 4, 5, 6, 7 ,8 ,9 \}$ are there?

- Since subsets are not ordered, 
	- we are simply counting the number of ways to choose $3$ unordered elements
		- from the given set of $9$
			- thusm $\left( \begin{array}{} 9 \\ 3\end{array} \right)=84$

## Example

At a confrence with $30$ mathematicians,
	every pair of attendes shakes hands once.
		How many total handshakes occur?

Since pairs of people are not otdered, 
	we are counting the number of ways to choose $2$ attendes 
		from a total of $30$, 
			which is $\left( \begin{array}{} 30 \\ 2\end{array} \right) = \cfrac{30 \cdot 29}{2 \cdot 1}=435$ 

## Example 

A pizza parlor offers $13$ different possible toppings on a pizza.
A pizza may have from $0$ up to $3$ different toppings.
How many different pizza toppings combinations are possible?

- In general there are $\left(\begin{array}{}13\\k\end{array} \right)$ possible pizzas that have exactally $k$ toppings.
- Thus, the number of pizza with at most $3$ topping is 
	- $$\left(\begin{array}{}13\\0\end{array} \right)+\left(\begin{array}{}13\\1\end{array} \right)+\left(\begin{array}{}13\\2\end{array} \right)+\left(\begin{array}{}13\\3\end{array} \right)=1 + 13 + 78 + 286 = 378$$

## Example

Determine the number of different full-house hands
	consisting of $3$ cards of one rank
		and a pair of cards in another rank,
			that can be delt from a standard 52-card deck


- Notes there are $13$ possible card ranks
	- and 4 cards of each rank
- First there are $13$ ways to choose the rank of $3$ of a kind, 
	- and there are $12$ ways to choose the rank of a pair.
- Once we have chosen the ranks, there are $\left(\begin{array}{}4\\ 3\end{array} \right) = 4$ ways to choose the three cards formaing a 3 of a pair.
- And $\left(\begin{array}{}4\\2\end{array} \right)=6$ ways of choosing a 2 of a pair
- Thus, in total there are $13\cdot 12\cdot 4\cdot 6=3744$ possible full houses

## Example

Determine the number of possible ways of permuating the letters in the word **MISSISSIPPI** 
- Since there are total of $11$ letters, it might make sense that there are $11!$ permutaions of the letters.
- However, not all these permutations yeild different words:
	- for example, if we swap two of the $S's$ the resulting word would be the same.
- There are $4$ S's , $4$ I's, $2$ P'S, $1$ M, which we will order in that order.
- First place the $4$ S's:
	- Since there are 11 possible locations there are $\left(\begin{array}{}11\\4\end{array} \right)$ ways to place them
		- since the $4$ S's are identical
- Next we place the $4$ I's
	- since there $7$ remaining locations there are $\left(\begin{array}{}7\\4\end{array} \right)$ ways to place them
- After this, there are only $3$ remaining locations in which we may place the $2$ P's 
	- yeilding $\left(\begin{array}{}3 \\2\end{array} \right)$ choices
- Finally, there is only one locatin for the M.

In total there are $\left(\begin{array}{}11\\4\end{array} \right)\cdot \left(\begin{array}{}7\\4\end{array} \right) \cdot \left(\begin{array}{}3\\2\end{array} \right)=300 \cdot 35 \cdot 3 = 34650$ ways of permutations the letters

**NOTE:** Another way to perform the count is to deternube the number of times each word shows up in the $11!$ permutaions of the letter. 
Since there are $4!$ ways of permutating the $4$S's among themselves, $4!$ of permutation $4$I's, $2!$ of permutating the $2$ P's.
Each words shows up $4! \cdot 4 !\cdot 2!$ times.
Thus the number of different words is $\cfrac{11!}{4!4!2!}=34650$ 













