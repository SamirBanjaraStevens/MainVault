The QR decomposition 
	or (QR factorization)
		Of a matrix is a decomposition of the matrix 
			into an orthogonal matrix and 
			a triangular matrix.

A QR decomposition of a real square matrix $A$ is a decomposition of $A$ as
$A = QR$ 
- Where $Q$ is an orthogonal matrix 
	- ($Q^{*}Q=I$)
- $R$ is an upper triangular matrix.

*Note :* If $A$ is non-singular, the factorization is unique.

## Gram-Schmidt Process
***

Consider the vectors to be the columns of $A$, so
$$A = \begin{bmatrix}
\ a_{1} & | & a_{2} & | & \cdots & | & a_{n} \ \\
\end{bmatrix}$$
then 
$$\begin{aligned}
u_{1}&= a_{1}, \quad &e_{1} &= \cfrac{u_{1}}{\|u_{1}\|}\\
u_{2}&= a_{2}-(a_{2}\cdot e_{1})e_{1}, &e_{2}&= \cfrac{u_{2}}{\|u_{2}\|}\\
&\vdots{}\\
u_{k+1}&= a_{k+1}-(a_{k+1}\cdot e_{1})e_{1}-\cdots- (a_{k+1}\cdot e_{k})e_{k}, &e_{k+1}&= \cfrac{u_{k+1}}{\|u_{k+1}\|}
\end{aligned}$$
*Note:*  $\|\cdot\|$ is the $L_{2}$ norm

the resulting QR factorization is
$$A = \begin{bmatrix}
\ a_{1} & | & a_{2} & | & \cdots & | & a_{n} \ \\
\end{bmatrix} = \begin{bmatrix}
\ e_{1} & | & e_{2} & | & \cdots & | & e_{n} \ \\
\end{bmatrix}
\begin{bmatrix}
a_{1}\cdot e_{1} & a_{2}\cdot e_{1} & \cdots & a_{n}\cdot e_{1}\\
0 & a_{2}\cdot e_{2} & \dots & a_{n}\cdot e_{2}\\
\vdots & \vdots & \ddots & \vdots\\
0 & 0 & \cdots & a_{n}\cdot e_{n}
\end{bmatrix}
= QR
$$
## Example
***
$$A = \begin{bmatrix}
1 & 2 \\
0 & 3 \\
-1 & 4
\end{bmatrix}$$
with the vectors
$$
\begin{aligned}
a_{1}&= (1, 0, -1)^{*} \\
a_{2}&=(2, 3, 4)^{*}
\end{aligned}
$$

All vectors consideerd are column vectors

$$
\begin{aligned}
u_{1}&= a_{1} &= (1, 0, -1)\\
e_{1}&= \cfrac{u_{1}}{\|u_{1}\|} &= \cfrac{1}{\sqrt{ 2 }}(1, 0, -1) &= \left(\cfrac{1}{\sqrt{ 2 }}, 0, -\cfrac{1}{\sqrt{ 2 }}\right)\\
u_{2} &= a_{2}-(a_{2}\cdot e_{1})e_{1} &= (2, 3, 4) - \cfrac{6}{\sqrt{ 2 }}\left(\cfrac{1}{\sqrt{ 2 }}, 0, -\cfrac{1}{\sqrt{ 2 }}\right) &= (1, 3, 1) \\
e_{2} &= \cfrac{u_{2}}{\|u_{2}\|} &= \cfrac{1}{\sqrt{ 11 }}(1, 3, 1) &= \left(\cfrac{1}{\sqrt{ 11 }}, \cfrac{3}{\sqrt{ 11 }}, \cfrac{1}{\sqrt{ 11 }}\right) \\
\end{aligned}
$$


thus,
$$Q = 
\begin{bmatrix}
\ e_{1} & | & e_{2} & | & \cdots & | & e_{n} \ \\
\end{bmatrix}
=
\begin{bmatrix}
\cfrac{1}{\sqrt{ 2 }} & \cfrac{1}{\sqrt{ 3 }} \\
0 & \cfrac{1}{\sqrt{ 3 }}  \\
-\cfrac{1}{\sqrt{ 2 }} & \cfrac{1}{\sqrt{ 3 }}
\end{bmatrix},
$$
$$R = 
\begin{bmatrix}
a_{1}\cdot e_{1} & a_{2}\cdot e_{1} \\
0 & a_{2}\cdot e_{2}
\end{bmatrix}
=
\begin{bmatrix}
\sqrt{ 2 } & -\sqrt{ 2 } \\
0 & 3\sqrt{ 3 }
\end{bmatrix}
$$
Orthonormalize $v_{1}$
***

1. Orthonormalize $v_{2}$
***
$$
\begin{aligned}
u_{2} &= v_{2}-(v_{2} \cdot e_{1})e_{1}\\
&=v_{2}-\mathbf{proj}_{u_{1}}(v_{2})
\end{aligned}
$$
- Calcuate $(v_{2} \cdot e_{1})e_{1} \text{ or } \mathbf{proj}_{u_{1}}(v_{2})$ 
***
	*Notes :* $\mathbf{proj}_{u_{1}}(v_{2}) = \cfrac{v_{2}\cdot u_{1}}{\|u_{1}\|^{2}}\cdot u_{1}$ 
so, 
$$v_{2} = (2, 3, 4) \textbf{ and } u_{1} = (1, 0, -1)$$
$\|u_{1}\| \ : \ \|(1, 0, -1)\| = \sqrt{ (1)^{2} + (0)^{2} + 1^{2} } =\sqrt{ 2 }$ 

 $v_{2}\cdot u_{1} = (2, 3, 4)(1, 0, -1) = -2$
 
 $\cfrac{v_{2}\cdot u_{1}}{\|u_{1}\|^{2}}\cdot u_{1} = \cfrac{-2}{\sqrt{ 2 }^{2}}\cdot(1, 0, -1) = (-1, 0, 1)$


- calcuate $v_{2}-\mathbf{proj}_{u_{1}}(v_{2})$
***

$$
\begin{align}
u_{2} &= v_{2}-(v_{2} \cdot e_{1})e_{1}  \\
&= v_{2}-\mathbf{proj}_{u_{1}}(v_{2})\\
&= (2, 3, 4) - (-1, 0, 1) \\
&= (2-(-1), 3-(0), 4-(1)) \\
&= (3, 3, 3)
\end{align}
$$

calcaute $e_{1}$ 
***
$\|u_{2}\| : \|(3, 3, 3)\| = \sqrt{ 3^{2} + 3^{2} + 3^{2}} = 3\sqrt{ 3 }$

then, $e_{2} = \cfrac{u_{2}}{\|u_{2}\|} = \cfrac{(3, 3, 3)}{3\sqrt{ 3 }} = \left(\cfrac{1}{\sqrt{ 3 }}, \cfrac{1}{\sqrt{ 3 }}, \cfrac{1}{\sqrt{ 3 }}\right)$ 

thus,

$$
\begin{aligned}
e_{1} &= \left(\cfrac{1}{\sqrt{ 2 }}, 0, -\cfrac{1}{\sqrt{ 2 }}\right)\\
e_{2} &= \left(\cfrac{1}{\sqrt{ 3 }}, \cfrac{1}{\sqrt{ 3 }}, \cfrac{1}{\sqrt{ 3 }}\right)
\end{aligned}
$$
