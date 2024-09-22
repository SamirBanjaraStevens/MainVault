### Q1
If we know that p = True, q = False and r =True, **what are the truth value of the following compound propositions?** 
#### Q1.1
$p \land q=$
	**False** 
#### Q1.2
$(p\lor q)\land\:r =$
	**True**
#### Q1.3
$p \implies q =$
	**False**
#### Q1.4
$q \implies r =$
	**True**
#### Q1.5
$(r \implies q) \implies (s \implies p =)$
	**True**
### Q2  Say it with Propositional Functions
Let Takes(x, y) be the propositional function “x takes course y”, Teaches(x, y) be the propositional function “x teaches course y”, and Passes(x, y) be the propositional function “x passes course y”. The universe of discourse is the set of all living people and all courses (i.e., you do not have to check this in your expressions).
For example, if we need to say “Adam takes and passes CS 110”, we can write it as“Takes(Adam, CS 110) ∧ Passes(Adam, CS 110)”.
#### Q2.1
Peter takes CS 220 and CS 410, but not CS 680
$$Takes \left(Peter, CS 220\right) \land Takes \left(Peter, CS 410 \right) \land \lnot Takes \left(Peter, CS 680 \right)$$
#### Q 2.2 
Bob passes every course that he takes except CS 220.
$$\forall x \left(Takes \left(Bob,x \right)\land x \ne CS220 \implies Passes\left(Bob,x \right) \right) \land \lnot \left(Passes,CS220 \right)$$
#### Q 2.3
Francesca passes every course that is taught by Prof. Einstein.
$$\forall x \left(Teaches \left(Einstein,x \right) \implies Passes\left(Francesca,x \right)\right)$$
#### Q 2.4
There is a course that both Julia and Peter took, but both of them failed it.
$$\exists x \left(Takes \left(Peter,x \right) \land Takes \left(Julia, x \right) \land \lnot Passes \left(Peter,x \right) \land \lnot Passes \left(Julia, x \right) \right) $$
###  Q3 Tautologies and Contradictions
**Find out for each of the following propositions whether it is a tautology, a contradiction, or neither (a contingency). Prove your answer**
#### Q3.1
[(p → q) ∧ (q → p)] → (p ↔ q)

| p | q | $p \implies q$ | $q \implies p$ | $p \Leftrightarrow q$ | $\left(p \implies q \right) \land \left(q \implies p \right)$ | $[\left(p \implies q \right) \land \left(q \implies p \right)] \implies \left(p \Leftrightarrow q \right)$ |
|---|---|----------------|----------------|-----------------------|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| T | T | T              | T              | T                     | T                                                             | T                                                                                                          |
| T | F | F              | T              | F                     | F                                                             | T                                                                                                          |
| F | T | T              | F              | F                     | F                                                             | T                                                                                                          |
| F | F | T              | T              | T                     | T                                                             | T                                                                                                          |

$\therefore$ the given proposition **[(p → q) ∧ (q → p)] → (p ↔ q))** is a Tautology
#### Q3.


| $$( \,p \lor q \lor r) \, \implies [( \, q \implies r) \, ∨ ( \, p \implies q) \,]$$ |                      |
| ------------------------------------------------------------------------------------ | -------------------- |
| $$( \, \lnot q \lor r) \, \lor ( \, \lnot p \lor q) \,$$                             | Conditional Identity |
| $$\lnot q \lor r \lor \lnot p \lor q$$                                               | Associative Laws     |
| $$( \, \lnot q \lor q) \, ∨ \lnot p \lor r$$                                         | Commutative Law      |
| $$T \lor r \lor \lnot p$$                                                            | Complement Laws      |
| $$T$$                                                                                | Domination Laws      |

$\therefore$ Argument is valid

### Q4
Is the below argument valid? Prove your answer by replacing each proposition with a variable to obtain the form of the argument. Then prove that the form is valid or invalid.

**“If k is a prime number, then 2k+4 is a composite number. 2k+4 is a composite number. Therefore, k is a prime number.”**

#### Q4.1
$p = k$ is a prime number
$q = 2k+4$ is a composite number
#### Q4.2
$p \implies q$
$q$
$\therefore p$
#### Q4.3
Argument is not valid , because in instance $p = F$ & $q = T$ both hypothesis are also true, but the conclusion is false.

$F \implies T$
$T$
$\therefore F$

