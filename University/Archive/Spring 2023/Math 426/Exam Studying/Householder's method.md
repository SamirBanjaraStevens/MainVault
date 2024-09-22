**Householder's methods** are a class of *[[Root-finding algorithms]]* 
	that are used for functions of one real variable
		with continious derivatives up to some order $d + 1$ 
The algorithm is *[[Iterative]]* and has a *[[Rate of convergence]]* of $d+1$ 


Householder's method
	is a numerical algorithm
		 for solving the nonlinear equation $f(x)=0$
In this case,
	the function $f$ has to be a function of one real variable.
The method consists of a sequence of iterations begining with an initial guess $x_{0}$
$$x_{n+1}=x_{n}+d\cfrac{\left( \frac{1}{f} \right)^{(d-1)}(x_{n})}{\left( \frac{1}{f} \right)^{(d)}(x_{n})}$$
If $f$ is a $d+1$ times continuously differentiable function 
	and $a$ is a zero of $f$ 
		but not of its derivative,
			then in a neighborhood of $a$ 
				the irerates $x_{n}$ satisfy,
					$$|x_{n+1}-a|\leq K \cdot|x_{n}-a|^{d+1}, \quad \text{ for some } K>0$$

This means that the itertes converge to the zero 
	if the initial guess is sufficiently close,
		and that the convergence has order $d+1$
	