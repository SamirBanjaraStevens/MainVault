| Sum, (OR), ($\cup$), ($\lor$) | Product, (AND), ($\cap$), ($\land$) |
| ----------------------------- | ----------------------------------- |
| 1 + 1 = 1                     | 1 * 1 = 1                           |
| 1 + 0 = 1                     | 1 * 0 = 0                           |
| 0 + 1 = 1                     | 0 * 1 = 0                           |
| 0 + 0 = 0                     | 0 * 0 = 0                                    |

**Minterm is a product of $n$ literals**
- with one literal for each variable



Disjunctive Normal Form (DNF)

Has the form 

$c_1 + c_2 + c_3 + \cdots + c_m$
- where each $c_j$ for $j\in \{1, \cdots, m\}$ is a product of literals

Example: $x\bar{y}\bar{z} + z + y\bar{z}$ 
- (the complement operator can be applied to individual literals only)


Conjunctive Normal Form (CNF)

Has the form 

$c_1 \cdot c_2 \cdot \, ... \, \cdot c_m$ 
- where each $c_j$ for $j \in \{1, \cdots, m\}$ is a sum of literals

Example : $(x + \bar{y} + \bar{z})(z)(y + \bar{z})$ 
- (the complement operator can be applied to individual literals only)


$(F+G)(b_1, b_2, \cdots, b_n) = F(b_1, b_2, \cdots, b_n) + G(b_1, b_2,\cdots, b_n)$ 
$(FG)(b_1, b_2, \cdots, b_n) = F(b_1, b_2, \cdots, b_n) \cdot G(b_1, b_2,\cdots, b_n)$ 



Number of possible functions?

how many different boolean functions o degree 1 are there?
- Sol : 4

$\huge{2^{2^n}}$  
