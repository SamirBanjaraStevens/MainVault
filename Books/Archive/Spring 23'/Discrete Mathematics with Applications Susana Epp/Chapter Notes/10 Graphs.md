**Walk** 
- finite alternating sequences of adjacent vertices and edges
- $v_0e_1\,v_1e_2\,\cdots v_{n-1}e_nv_n$ 

**Trail** 
 - <u>walk that</u> *does not contain* a repeated *edge*.

**Path** 
- <u>Trail</u> that *does not contain* repeated *vertex*

**Closed walk**
- Walk that *start and ends at same vertex*

**Circuit**
- Closed walk that *contains at least one edge* and *does not contain a repeated edge*

**Simple Circuit**
- Circuit that does not have any other repeated
- except the first and last

**Subgraph**
- A graph $H$ of a graph $G$, 
	- if and only if, 
		- every vertex in $H$ is also a vector in $G$
		- every edge in $H$ is also a edge in $G$
		- Every edge in $H$ has the same end points as it has in $G$

**Connected**
- Two vertices $v$ and $w$ of $G$ are connected 
	- if and only if,
		- there is a walk from $v$ to $w$ 
- A graph $G$ is connected
	- if and only if,
		- given any two vertices $v$ and $w$, 
		- there is a walk from $v$ to $w$

- **Connected Component**
	- A graph $H$ is a connected component of a graph $G$ 
		- if and only if,
			-$H$ is a subgraph of $G$
			- $H$ is connected; and 
			- no connected subgraph of $G$ has $H$ as a subgraph 
				- and contains vertices or edges that are not in $H$

**Euler Circuit**
- Circuit that contains every vertex and every edge of $G$
	- Every vertex of the graph has a positive even degree
		- Hence, if some vertex has a odd degree then it is not an Euler Circuit

**Euler Trail**
- trail, that passes through every vertex *at least* once, and *every edge exactly* once 
	- Two vertices have an odd degree, 
		- and the rest of vertices have even degree

**Hamiltonian Circuit**
- Simple circuit, that includes every vertex

- if a Graph is a Hamiltonian Circuit, then it has a subgraph $H$ with,
	- $H$ contains every vertex of $G$
	- $H$ is connected 
	- $H$ has the same number of edges as vertices
	- Every vertex of $H$ has degree 2

**Adjacency Matrix**

*For Directed Graph*
- $n\times n$ matrix $A = (a_{ij})$ over the set of nonnegative integers that
	- $a_{ij} =$ the number of arrows from $v_i$ to $v_j$ for all $i, j = 1, 2, /cdots , n$  

*For Unirected Graph*
- $n\times n$ matrix $A = (a_{ij})$ over the set of nonnegative integers that
	- $a_{ij} =$ the number of edges connecting $v_i$ to $v_j$ for all $i, j = 1, 2, /cdots , n$  

**Length of a Walk**
- if repeated edges are counted each time they occur,
	- *number of edges in the sequence* 
	- $v_2 \ e_3 \ v_3 \ e_4 \ v_2 \ e_2 \ v_2 \ e_3 \ v_3$
	- has length of 4, (counting $e_3$ two times)

**Isomorphic**