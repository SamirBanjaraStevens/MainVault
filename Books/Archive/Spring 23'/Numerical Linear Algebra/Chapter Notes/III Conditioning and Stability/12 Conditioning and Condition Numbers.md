***
We turn to a systematic discussion of two fundamental issues of numerical analysis
- **Conditioning** : pertains to the perturbation behavior of a mathematical problem
- **Stability** : pertains to the perturbation behavior of a an algorithm used to solve that problem on a computer
***

## Condition of a Problem
***
In the abstract,
	we can view a *Problem* as a function $f : X \rightarrow Y$ 
		from a normed vector space $X$ of data
			to a normed vector space $Y$ of solutions.

This function $f$ is usually nonlinear (even in linear algebra), 
	but most of the time it is at least continuous

We are concerned with the behavior of a problem $f$ 
	at a particular data point $x \in X$ 
		(the behavior may vary greatly from one point to another)

The combination of a problem $f$ 
	with prescribed data $x$ 
		might be called a *problem instance* 
			but it is more usual
				to use the term *problem*

A *well-conditioned* problem (instance)
	is one with the property 
		that all small perturbations of $x$ 
			leads to only small changes in $f(x)$ 

An *ill-conditioned* problem 
	is one with the property
		 that some small perturbation of $x$ 
			 leads to a large change in $f(x)$

Th meaning of "small" and "large" in these statements depends on the application

In particular,
	sometimes it is more appropriate to measure perturbations on an absolute scale, 
	and sometimes it is most appropriate to measure them relative to the norm of the object being perturbed

## Absolute Condition Number
***
Let $\delta x$ denote a small perturbation of $x$ 
	and, write $\delta f = f(x + \delta x) - f(x)$ 

The **absolute condition number** $\hat{k} = \hat{k}(x)$ of the problem $f$ at $x$ is defined as 
$$\tag{12.1} \hat{k} = \lim_{\delta \rightarrow 0} \quad \underset{\|\delta x\| \leq \delta}{\text{sup}} \ \cfrac{\|\delta f\|}{\|\delta x\|}$$
For most problems,
	the limit of the supremum in the formula above (12.1) 
		can be interpreted as a supremum over all infinitesimal perturbations $\delta x$ 

To make formula *(12.1)* more readable,  
	remove lim and other notations

$$\hat{k} = \underset{\delta x}{\text{ sup }} \cfrac{\|\delta f\|}{\|\delta x\|}$$

If $f$ is differentiable,
	we can evaluate the condition number number by means of the derivative of $f$

Let $J(x) be the matrix whose $i, j$ entry is the partial derivative 

## Relative Condition Number
***

## Examples
***

#### Example 12.1

#### Example 12.2

#### Example 12.3

#### Example 12.4

#### Example 12.5

#### Example 12.6

## Condition of Matrix-Vector Multiplication 
***

### Theorem 12.1
***

## Condition Number of a matrix
***

## Condition of a System of Equations
***

### Theorem 12.2
***



# Exercises
***



## 12.1
***

## 12.2
***
### (a)
### (b)
### (c)
### (d)

## 12.3 
***
### (a)
### (b)
### (c)
### (d)
