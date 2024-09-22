## Q1 
### What is meant by a consistent system of linear equations?
**SOLUTION :** A system of linear equations is consistent if it has a solution, (either one or many solutions)
## Q2
### Which of the following is consistent system of equations? For each, explain why or why not.
#### (a) $$\begin{pmatrix} 3u + 4v = -1 \\ -6u -8v = 2 \end{pmatrix}$$ 
**SOLUTION :** Second equation is multiple of the first equation resulting in coincident planes in a vector space . Resulting in a consistent system with many solutions, one of which is; u = 1 and y = -1. 
#### (b) $$\begin{pmatrix} 3x + 5y = 8 \\ 5x + 3y = 8 \end{pmatrix}$$
**SOLUTION** Using Gauss Jordan, (Steps shown below) we get the following solution. x = 1 and y = 1, thus making the system of linear equations consistent. 

**GAUSS JORDAN STEPS** 
(1). Convert to matrix 
$$\begin{pmatrix} 3 & 5 & 8 \\ 5 & 3 & 8\end{pmatrix}$$

(2). Multiply matrix row by constant: $R_{1} \Leftarrow \,(1/3\,)\times R_{1}$
$$\begin{pmatrix} 1 & 5/3 & 8/3 \\ 5 & 3 & 8\end{pmatrix}$$

(3). Cancel leading coefficient in row $R_{2}$ by performing $R_{2}\Leftarrow R_{2} - 5R_{1}$
$$\begin{pmatrix} 1 & 5/3 & 8/3 \\ 0 & -16/3 & -16/3\end{pmatrix}$$

(4). Multiply matrix row by constant: $R_{2}\Leftarrow \,-(3/16\,)\times R_{2}$
$$\begin{pmatrix} 1 & 5/3 & 8/3 \\ 0 & 1 & 1\end{pmatrix}$$

(5). Cancel leading coefficient in row $R_{1}$ by performing $R_{1}\Leftarrow R_{1} - (5/3)\times R_{2}$
$R_{2}\Leftarrow \,-(3/16\,)\times R_{2}$
$$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1\end{pmatrix}$$
## Q3
### In each part of equation 2 above is it possible to change the right hand side so as to change the state of consistency of the system?
#### (a).
**Solution :** Since the two equations are multiples of one another, we can replace the bottom entry of the right hand side to any number other than 2 and we will have an inconsistent system. 
For example,
$$\begin{pmatrix} 3u + 4v = -1 \\ -6u - 8v = 2.718\end{pmatrix}$$

This is because the original system of linear system of equations coincide, but we we change the   right hand side, the two equations which represent plane in vector space, no longer coincide, but intersect. 

#### (b).
**Solution :** It is *not* possible to change the right hand side of the system and change it from a consistent to an inconsistent system. The system has a unique solution for each given right hand side. This is clear to see, because the coefficient matrix of the RREF is an identity matrix, and so no mater the augmentation, we will always arrive to a consistence identity matrix when we try to attain RREF. We have two independent columns and two dependent variables