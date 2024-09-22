| Logical Operator                      |     |
| ------------------------------------- | --- |
| Negation (NOT)                        |     |
| Exclusive (XOR)                       |     |
| Conjunction (AND)                      |     |
| Disjuction (OR)                       |     |
| Implication (IF - THEN)               |     |
| Bi-conditional (IF AND ONLY IF) (IFF) |     |

$p \rightarrow q$ 
Only the an implication can be **false** is if $p$ is true and $q$ is **false**. 
- If $p$ is false the entire statement is true regardless of $q$

**Contrapositive**
$\neg q \rightarrow \neg p$ 
- Sometime useful for proofs
	- Why?

BiDirectional (If and only if) (IFF)

Laws of propositional logic
| Laws of propositional logic |                                                      |                                                              |                          |                   |
| --------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ | ------------------------ | ----------------- |
| Idempotent Laws             | $p\lor p = p$                                        | $p \land p = p$                                              |                          |                   |
| Associative Laws            | $( p\lor q ) \lor r = p \lor ( q \lor r )$           | $(\, p \land q\,)\land r = p \land (\, q \land r\,)$         |                          |                   |
| Commutative   Laws          | $p \lor q = q \lor p$                                | $p \land q = q\land p$                                       |                          |                   |
| Distributive Laws           | $p \lor ( q \land r ) = (p \lor q) \land (p \lor r)$ | $p\land (\,q \lor r\,) = (\,p\land q\,)\lor(\,p\land r\,)$   |                          |                   |
| Identity Laws               | $p \lor F = p$                                       | $p \land T = p$                                              |                          |                   |
| Domination Laws             | $p \land F = F$                                      | $p\lor T = T$                                                |                          |                   |
| Double Negation Law         | $\neg\neg p = p$                                     |                                                              |                          |                   |
| Complement Laws             | $p\land \neg p = F \quad : \quad \neg T = F$  | $p \lor \neg p = T \quad : \quad \neg F = T$ |
| De Morgan's Laws            | $\neg(\, p \lor q \,) = \neg p \land \neg q$         | $\neg(\, p\land q \,) = \neg p \lor \neg q$                   |                          |                   |
| Absorption Laws             | $p \lor (\,p\land q\,) = p$                          | $p\land (\,p \lor q\,) = p$                                  |                          |                   |
| Conditional Identities      | $p\rightarrow q = \neg p \lor q$                     | $p\iff q = (\,p\rightarrow q\,) \land (\,q \rightarrow p\,)$ |                          |                   |
|                             |                                                      |                                                              |                          |                   |

**Rules of Inference**

**Modus Ponens**
$$
\begin{aligned}
&p\\
&p \rightarrow q\\
&\hline\\
&\therefore \quad q
\end{aligned}
$$
$$((p\rightarrow q)\land p) \Rightarrow q$$
"if its raining, then I will make Tea"
"it is raining"
"therefore, I will make tea"

**Modus Tollens**
$$
\begin{aligned}
&p \rightarrow q\\
&\neg q\\
&\hline\\
&\therefore \quad \neg p
\end{aligned}
$$
$$((p\rightarrow q)\land \neg q )\Rightarrow \neg p$$
"if it is raining, then I will make tea"
"I do not make tea"
"therefore, It is not raining"

**Hypothetical Syllogism**
$$
\begin{aligned}
&p \rightarrow q\\
&q \rightarrow r\\
&\hline\\
&\therefore \quad p\rightarrow r
\end{aligned}
$$
$$((p\rightarrow q)\land(p\rightarrow r))\Rightarrow(p\rightarrow r)$$
"If it raining, then I will make tea"
"if I make tea, then I will read a book"
"Therefore, If it raining I will read a book"

**Disjunctive Syllogism**
$$
\begin{aligned}
&q \lor r\\
&\neg q\\
&\hline\\
&\therefore \quad r
\end{aligned}
$$
$$((q\lor r)\land \neg q)\Rightarrow r$$

"I will make tea, or I will read a book."
"i will not make tea"
"Therefore, I will read a book"

**Addition**
$$
\begin{aligned}
&p\\
&\hline\\
&\therefore \quad p \lor q
\end{aligned}
$$
$$p\Rightarrow p \lor q$$
"I will make tea"
"therefore, i will make tea, or I will read a book"

**Simplification**
$$
\begin{aligned}
&q \land r\\
&\hline\\
&\therefore \quad q
\end{aligned}
$$
$$(p\land q)\Rightarrow q$$
"I will make tea and I will read a book"
"Therefore if it rains, then I will read a book"

