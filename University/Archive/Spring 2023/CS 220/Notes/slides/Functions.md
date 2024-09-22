A **Function F** from a set $A$ to set $B$ is an assignment of <u>exactly one</u> element of $B$ to each element of $A$

We write $f(a) = b$ 

$b$ is the unique element of $B$ by the function $f$ to the element $a$ of $A$.

If $f$ is a function from $A$ to $B$, we write $f: A\rightarrow B$ 

If $f: A\rightarrow B$, 
- $A$ is the **domain**
- $B$ is the **co-domain**

if $f(a)=b$ 
- $b$ is the **image** of $a$
- $a$ is the **pre-image** of $b$

**Range** of $f: A\rightarrow B$ : set of all **images** of elements  $a\in A$   
- If we only regard a subset $S \subseteq A$, 
	- the set of all images of elements $s\in S$ is the **image of S**.
	- image of $S$ denoted by $f(S) = \{f(s) : s\in S\}$ 

We say that "$f: A\rightarrow B$ maps $A$ to $B$"

Two functions $f$ and $g$ are **equal** if and only if
- Their domain and range are the same
- And for every $x$ in the domain, $f(x) = g(x)$

## **One-to-One** (injective)
- If and only if it does not map two distinct elements of $A$ onto the same element of $B$
	- $\forall x,y \in A (f(x)=f(y) \rightarrow x=y$ 
		- Disproving a function is (injective)
			- $f : \mathbb{R} \rightarrow \mathbb{R}, f(x) = x^{2}$ 
			- $f(3) = f(-3)$ but $3 \neq -3$, so $f$ is not injective


- $f: A\rightarrow B$ with $A, B \subseteq R$ 
	- **Strictly Increasing** 
		- If $\forall x,y \in A(x<y\rightarrow f(x)<f(y))$ 
	- **Strictly Decreasing**
		- if $\forall x,y \in A(x<y\rightarrow f(x)>f(y))$ 
	- If function is either strictly increasing or decreasing then it is injective 

 
## **Onto** (surjective)
- If and only if for every element of $b\in B$ there is an element $a\in A$ with $f(a) = b$
	- $f$ if onto(surjective) if ant only if *<u>its range is its entire codomain</u>*  

## **Bijective**
If one to one and onto

## **Inversions and Compositions**
Bijection can be inverted
- Therefore for a function to be invertible, it be bijective(or both one-to-one and onto)
- **Inverse function** of a bijection $f: A \rightarrow B$ 
	- is the function $f^{-1}: B \rightarrow A$
		- with $f^{-1}(b) = a$ whenever $f(a)=b$ 

- **Composition** of two functions $g: A \rightarrow B$ and $f: B \rightarrow C$ 
	- denoted $f \circ g$ 
	- defined by 
		- $(f\circ g)(a) = f(g(a))$ 
			- 1. function $g$ is applied to element $a\in A$, mapping it onto an element $b \in B$. 
			- 2. then function $f$ is applied to this element of $B$, mapping it onto an element of $C$.
		- Therefore, the composite function maps from $A$ to $C$ 

**Identity Function**
- Composition of a function and its inverse
	- $i(x)=x$ 
	- $(f^{-1} \circ f)(x) = f^{-1}(f(x)) = x$ 

The **Graph** of a function $f: A \rightarrow B$ is the set of ordered pairs
- $\{{a, b} \ | \ a\in A \text{ and } f(a)=b\}$  
	- The graph is a subset of $A\times B$ (cross product) 

**Floor**
- Assigns to $r \in \mathbb{R}$ the *largest* $z\in \mathbb{Z}$  with $z\leq r$ denoted $\lfloor r \rfloor$ 
	- $\lfloor 2.3 \rfloor = 2$, $\lfloor 2 \rfloor = 2$, $\lfloor 0.5 \rfloor = 0$, $\lfloor -3.5 \rfloor = 4$ 
**Ceiling**
- Assign to $r \in \mathbb{R}$ the *smallest* $z\in \mathbb{Z}$  with $z\geq r$ denoted $\lceil r \rceil$
	- $\lceil 2.3 \rceil = 3$, $\lceil 2 \rceil = 2$, $\lceil 0.5 \rceil = 3$, $\lceil -3.5 \rceil = -3$ 

## **exponential Functions** 
The exponential function $\text{exp}_{b} : \mathbb{R}\rightarrow \mathbb{R}^{+}$ 
- is defined as $\text{exp}_{b}(x) = b^{x}$ 

Properties: 
$$b^{x}\, b^{y} = b^{x+y}$$
$$(b^{x})^{y} = b^{xy}$$
$$
\frac{b^{x}}{b^{y}} = b^{x-y}
$$
$$(bc)^{x} = b^{x} c^{x}$$

## **Logarithm function** 
- The logarithm function is the inverse of a exponential function

$\log_{b}: \mathbb{R}^{+}\rightarrow \mathbb{R}$   
- is defined as $b^{x} = y \leftrightarrow \log_{b}(y) = x$ 
	- $b>0 \text{ and } b\neq 1$ 

Properties:
$$\log_{b}(xy) = \log_{b}(x) + \log_{b}(y)$$
$$\log_{b}\left(\frac{x}{y}\right) = \log_{b}x - \log_{b}y$$
$$\log_{b}(x^{y}) = y\log_{b}x$$
$$\log_{c}x = \frac{\log_{b}x}{\log_{b}c}$$

Both Log and Exponential are strictly increasing hence, injective functions