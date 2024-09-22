Samir banjara 
01/24/2002

1.  Show that the following is an equation of a sphere.  Determine the center of the sphere and its radius. $$x^2 + y^2 + z^2 - 4x + 2y = 10$$
	- Rewrite the given equation in the form of an equation of a sphere by completing the squares.
		 $$ \,(x^{2} - 4x + 4x\,) + \,(y^{2} + 2y + 1\,) + \,(z^2\,) = 10$$
		 $$\,(x^{2} - 2\,)^{2} + \,(y^{2} + 1\,)^{2} + z^{2} = 15$$
	- *Center* : $\,(2, -1, 0\,)$
	- *Radius* : $\sqrt{15}$
	

2. Determine if the points $P(0,2,0),\, Q(1,2,3),\, R(0,0,-2)$ be on the same line (are co-linear). Briefly explain how, you came to this conclusion.
	- We can also say *A, B,* and *C* are co-linear if the largest length of *AB,* and *AC*. and *BC* is equal to the sum of the other two. We can determine length of the vector by using the distance formula.
	$$\,|\overrightarrow{PQ}\,| = \sqrt{\,(0 - 1\,)^{2} + \,(2 - 2)\,)^{2} + \,(0 - 3\,)^{2}} = \sqrt{10}$$
	
	$$\,|\overrightarrow{PR}\,| = \sqrt{\,(0 - 0\,)^{2} + \,(2 - 0)\,)^{2} + \,(0 + 2\,)^{2}} = \sqrt{8}$$
	
	$$\,|\overrightarrow{QR}\,| = \sqrt{\,(1 - 0\,)^{2} + \,(2 - 0)\,)^{2} + \,(3 - 2\,)^{2}} = \sqrt{10}$$
	- Because the sum of any two lengths are not equal to the third. Points P, Q, and R are not co-linear. 
		- $\,|\overrightarrow{QR\,|} + \,|\overrightarrow{PR}\,| \ne \,|\overrightarrow{PQ}\,|$
		- $\,|\overrightarrow{PR\,|} + \,|\overrightarrow{PQ}\,| \ne \,|\overrightarrow{QR}\,|$
		- $\,|\overrightarrow{QR\,|} + \,|\overrightarrow{PQ}\,| \ne \,|\overrightarrow{PR}\,|$
		- 
**Bonus Answer (for fun to remember concepts for MATH 426**
	- If the cross product of the the vectors AB and AC  is not the zero vector $\,(0, 0, 0\,)$, then then the give points are not co-linear. (Corollary 10, pg 817, James Stewart Early Transcendentals Ed:8th)
	$$\overrightarrow{PQ}\times \overrightarrow{PR}$$
	$$\overrightarrow{PQ} = \,(1 - 0\,)i + \,(2 - 2\,)j + \,(3 -0\,)k = i + 3k$$
	$$\overrightarrow{PR} = \,(0 - 0\,)i + \,(0 - 2\,)j + \,(-2 - 0\,)k = -2j + -2k$$
	$$\overrightarrow{PQ}\times \overrightarrow{PR} = \begin{vmatrix} i & j & k \\ 1 & 0 & 3 \\ 0 & -2 & -2\end{vmatrix}$$
	$$\overrightarrow{PQ}\times \overrightarrow{PR} = \begin{vmatrix} 0 & 3 \\ -2 & -2\end{vmatrix}i - \begin{vmatrix} 1 & 3 \\ 0 & -2\end{vmatrix}j - \begin{vmatrix}1 & 0 \\ 0 & -2\end{vmatrix}k$$
	$$6i - \,(-2j\,) - \,(-2k\,) = \langle 6, -2, -2\rangle$$
	$$\therefore \text{given points are not co-linear, beacsue we did not attain a zero vector}$$
	- Also, if $P(0,2,0),\, Q(1,2,3),\, R(0,0,-2)$ are co-linear then $\overrightarrow{PQ}$ and $\overrightarrow{PR}$ are proportional. 
	$$\overrightarrow{PQ} = \lambda\cdot\overrightarrow{PR}$$

	