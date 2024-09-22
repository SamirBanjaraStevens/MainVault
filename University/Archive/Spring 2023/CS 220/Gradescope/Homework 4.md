Let us take a look at the sets A = {x, y, z}, B = {1, 2, 3}, C = {x}, D = {y, z}. List the elements of the following sets:

### Q1.1
(A × B) – (B × C) =
{(x,1), (x,2), (x,3), (y,1), (y,2), (y,3), (z,1), (z,2), (z,3)}

# 1.2
(A × A) – (D × D) =
{(x,x), (y,x), (z,x), (x,y), (x,z)}

# 1.3
(A × B × C) ∩ (C × B × A) =
{(x,1,x), (x,2,x), (x,3,x)}

# 1.4
E = {(a, b, c) | a, b, c ∈ D ∧ a ≠ b ∧ a ≠ c} =
{(y,z,z),(z,y,y)}

# 1.5
F = {(a, b, c) | a ∈ B ∧ b ∈ C ∧ c ∈ B ∧ a ≠ c} =
{(1,x,2),(1,x,3),(2,x,1),(2,x,3),(3,x,1),(3,x,2)}


Are the following statements true for all sets A, B and C? Prove your answers. (If you need to draw anything, you can upload it as a file.)

# 2.1
∣A∪B∪C∣=∣A−B−C∣+∣B−A−C∣+∣C−A−B∣
Assume sets $A, B, \ \text{and} \ C$ are identical 
$$
A = \{1, 2, 3\} \\
B = \{1, 2, 3\} \\
C = \{1, 2, 3\} \\
$$
$|A\cup B\cup C| = 3$
$A-B-C=B-A-C=C-A-B$
hence, $|A-B-C| = 0$
Because $3\neq0$, the equality 
$|A\cup B\cup C|= |A-B-C|+|B-A-C|+|C-A-B|$ 
$3 = 0 + 0 + 0$
is false

# 2.2
∣A∪B∪C∣=∣A∣+∣B∣+∣C∣−∣A∩B∣−∣A∩C∣−∣B∩C∣+∣A∩B∩C∣
$$
\begin{align}
|A\cup B\cup C| &= |(A\cup B)\cup C|\\
&= |A\cup B| + |C| - |(A\cup B)\cap C|\\
&= |A| + |B| - |A\cap B| + |C| - |A\cap C|\cup |B\cap C|\\
&= |A| + |B| + |C|- |A\cap B| - |A\cap C|-|B\cap C| + |A\cap B\cap C|
\end{align}
$$
