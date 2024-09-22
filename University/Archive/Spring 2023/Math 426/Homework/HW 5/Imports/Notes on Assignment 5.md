## Question 1
***
Write an R program to implement,
QR factorization using the following. 

1. Classic Gram Schmidt,
2. Modified Gram Schmidt (MGS) by modifying CGS as discussed in class,
3. Modified Gram Schmidt as outlined in the text book,
4. Householder method.

### Directions
*** 
Program should take a matrix $A$ as input and return both $Q$ and $R$ as output. 
Use the following matrix : $$A = \begin{bmatrix}1 & 2\\ 0 & 3\\ -1 & 4\end{bmatrix}$$
Compare results and verify that $A = QR$ 


### Solution
***
Let 
$$
\begin{aligned}
A_{CGS} &= \text{ Classic Gram Schmidt}\\
A_{MGS} &=\text{ Modified Gram Schmidt}\\
A_{TMGS} &=\text{ Text Book Modified Gram Schmidt}\\
A_{HH} &=\text{ Householder Method}\\
\end{aligned}
$$

## Pseudocode
 
```ad-note
title: Classic Gram Schmidt $A_{CGS}$
```
***
$$
\begin{aligned}
&\textbf{Algorithm } \text{}\\
&\textbf{For }\text{j = 1} \textbf{ to } \text{n} \textbf{ do:}\\
&v_{j} = a_{j}\\
&\textbf{For } \text{i = 1} \textbf{ to } \text{j - 1}\textbf{ do:}\\
&r_{ij} = q_{i}^{*}a_{j}\\
&v_{j} = v_{j} - r_{ij}q_{i}\\
&r_{jj} = \|v_{j}\|_{2}\\
&q_{j} = \cfrac{v_{j}}{r_{jj}}
\end{aligned}
$$

```ad-info
title:Notes
Gram-Schmidt Orthogonalization using this algorithm produce a reduced QR fractorization denoted as $A = \hat{Q}\hat{R}$
```

![[7 QR Fractorization#**Theorem 7.1**]]

```ad-tldr
title: Summary
color: 152, 72, 75
How to do Classic by hand
```



```ad-note
title: Modified Gram Schmidt $A_{MGS}$
color: 245, 9, 104
```
***

$\textbf{For } j-1 \textbf{ to } n \textbf{ do:}$
	$v_{j}^{(1)} = a_{j}$
$\textbf{end for}$
	$\textbf{For } i = 1 \textbf{ to } n \textbf{ do:}$
		$r_{ij} = \|v_{j}^{(1)}$
		$q_{i} = \cfrac{v_{i}^{(1)}}{r_{ij}}$
		$\textbf{For } j = i + 1 \textbf{ to } n \textbf{ do:}$
			$r_{ij} = q_{i}^{(1)} v_{j}^{(1)}$
			$v_{j}^{i+1} = v_{j}^{(1)} - r_{ij}q_{i}$
		$\textbf{end for}$
	$\textbf{end for}$



```ad-note
title: Text Book Modified Gram Schmidt $A_{TMGS}$
color: 66, 245, 147
```
***
### Pseudocode
***
$\textbf{For } i = 1 \textbf{  to  } n \textbf{ do:}$
	$v_{i} = a_{i}$
$\textbf{For } i=1 \textbf{ to } n \textbf{ do:}$
	$r_{ii} = \|v_{i}\|$
	$q_{i} = \cfrac{v_{i}}{r_{ii}}$
	$\textbf{For } j = i + 1 \textbf{ to } n \textbf{ do:}$
		$r_{ij} = q_{i}^{*}v_{j}$
		$v_{j} = v_{j} - r_{ij}q_{i}$


*Note :* 
common to let $v_{i}$ overwrite $a_{i}$ 
& $q_{i}$ overwrite $v_{i}$ 
 

```ad-note
title: Householder method $A_{HH}$
color: 245, 209, 66
```
***
### Pseudocode
***
![[10 Householder Triangular#The Algorithm|]]

Upon completion of this algo, 
$A$ has been reduced to <u>upper triangullar form</u> 
- (**We have calculated $R$**) 

**But**
- we still need to calculate $Q$ and,
- $n-$column submatrix $\hat{Q}$ 
	- corresponding to a reduced $\mathbf{QR}$ factorization 

![[10 Householder Triangular#The Algorithm]]

