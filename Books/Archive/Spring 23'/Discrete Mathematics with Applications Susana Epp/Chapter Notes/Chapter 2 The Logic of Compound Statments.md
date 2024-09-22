## 2.1 Logical Form and Equivalence

"*Logic is a science of the necessary laws of thought, without which no employment of the understanding and the reason takes place*" - Immanuel Kant, 1785

Argument - sequences of statements aimed at demonstrating the truth of an assertion
	Assertion at end of the sequence is the conclusion and preceding statements are premises (hypothesis).

**Statement** (or proposition) is a sentence that is true or false, but not both
	"*Two plus two equals four*" : statement because it is true 
		But the truth or falsity of **$x^{2} + 2 = 11$** depends on the value of x, hence it is not a statement.

## Compound Statements 
p but q : means : p and q ($p \land q$)
neither p nor q : means : $\lnot p \land \lnot q$

### Example 2.1.2 Translating From English to Symbols: But and Neither-Nor
#### Write each of the following sentences symbolically, letting h = "It is hot" and s = "It is sunny."

a. It is not hot but it is sunny.
	(SOL) : $\lnot h \land s$
b. It is neither hot nor sunny.
	(SOL) : $\lnot \, (h \lor s) \,$

### Example 2.1.4 Truth Table for Exclusive Or $\oplus$ 
$\, (p \lor q) \, \land \lnot \, (p \land q) \,$ : "*p **or** q but not both*"

| p   | q   | $p \lor q$ | $p \land q$ | $\lnot \, (p \land q) \,$ | $\,(p \lor q)\, \land \lnot \,(p \land q)\,$ |
| --- | --- | ---------- | ----------- | ------------------------- | ----------------------------------------------- |
| T   | T   | T          | T           | F                         | F                                               |
| T   | F   | T          | F           | T                         | T                                               |
| F   | T   | T          | F           | T                         | T                                               |
| F   | F   | F          | F           | T                         | F                                               |

**Logically Equivalent** : Two statements are logically equivalent if, and only if, they have identical truth values for each possible substitution of statements for their statement variables.

## De Morgan's Laws
The negation of an *and* statement is logically equivalent to the *or* statement in which each component is negated

The negation of an *or* statement is logically equivalent to the *and* statement in which each component is negated. 

### Example 2.1.11
$p:$ Jim is tall *and* Jim is thin.

is $\lnot p:$ Jim is not tall *or* Jim is not thin.

## Tautologies and Contradictions 
**Tautology** : Statement form that is always **True** regardless of the truth values of the individual statements substituted for its statement variables. 

**Contradiction** : Statement form that is always **False** regardless of the truth values of the individual statements substituted for its statement variables. 

#### Logical Equivalences
![[Pasted image 20230127213809.png]]

## 2.2 Conditional Statements
The **Conditional** of *q* by *p* is "if *p* then *q*" or *"p* implies *q"*
	Denoted $p \rightarrow q$
	It is false when *p* is True and *q* if False: otherwise it is True.
	*p* : hypothesis (antecedent)
	*q* : conclusion (consequent)
		**Vacuously True or (true by default)**

"If you show up for work Monday morning, then you will get the job”

Vacuously true if you do not show up for work Monday morning.

### The Converse, Contrapositive, and Inverse
Of $p \Rightarrow q$

**Converse** : <big>$q \Rightarrow p$</big>

**Contrapositive** :  <big>$\lnot q \Rightarrow \lnot p$</big>

**Inverse** :  <big>$\lnot p \Rightarrow \lnot q$</big>

1. Conditional Statements are logically equivalent to its **Contrapositive**
2.  **Converse** is not logically equivalent to conditional Statement
3. **Inverse** is not logically equivalent to conditional Statement
4. **Converse** and **inverse** of a conditional statement are logically equivalent to each other

![[B78E8D52-642F-42CC-BC6F-BBDD06C39133.jpeg]]
<!-- ### The Converse, Contrapositive, and Inverse from ZyBook --> 

### Bi-Conditional Operation *If, and only if,*
$p \Leftrightarrow q$
**True** when p and q have the same truth value, **False** when p and q have different Truth values.

**biconditional** of p and q : "*p* if, and only if, *q*"

### Order of Operation for Logical Operation
If parentheses are not used to explicitly indicate the order in which the operations should be applied, then ∧, ∨, and ¬ should be applied before $\Rightarrow$.

![[Pasted image 20230127220252.png]]
<!-- Order of Operations for Logical Operators, taken from Susana Epp book -->

### Necessary and Sufficient 

r is a **sufficient condition** for s : means : "if r then s" : $r\rightarrow s$
- occurrence of *r* is sufficient to guarantee the occurrence of *s*.

r is a **necessary condition** for s: means : "if not r then not s" $\lnot r\rightarrow \lnot s$
- if *r* does not occur, then *s* cannot occur either
- also means "if s then r" : $s\rightarrow r$ and so, necessary condition is the contrapositive. 
r isa necessary and sufficent condition for s : means : "r if, and only if, s" : $p\leftrightarrow r$
## 2.3 Valid and Invalid Arguments

| If socrates is a man, then socrates is mortal | If p then q    |
| --------------------------------------------- | -------------- |
| Socrates is man                               | p              |
| $\therefore$ Socrates is mortal               | $\therefore$ q | 

**Argument** : sequence of statements 
**Argument form** : sequence statement forms

To say an argument form is valid to to say no matter what particular statements are substituted for the statement variables in its premises, (assumptions), if the resulting premises are all true then conclusion is also true. 

**Fallacy** : error in reasoning that results in an invalid argument 
- Using Ambiguous premises
- Circular reasoning
- Jumping to conclusions
For an Argument to be valid, every argument of the same form whose premises are all true must have a true conclusion. 

### Rules of inference 
![[Pasted image 20230130124518.png]]

## 2.4 Circuits 
![[Pasted image 20230130124630.png]]
### Boolean expression for circuits 
![[Pasted image 20230130124841.png]]

a. $\,(\lnot P \land Q\,)\lor\lnot Q$
![[Pasted image 20230130125238.png]]

b. $\,(\,(P\land Q\,)\land \,(R\land S\,)\,)\land T$
![[Pasted image 20230130125338.png]]
