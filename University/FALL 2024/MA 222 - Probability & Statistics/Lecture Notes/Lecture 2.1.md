Sample Spaces and Events
***
Objectives:
- Introduce the sample space of a probability event, events, and operations on them.
***
# Sample Space
- A *(probability) experiment* or (trial) is any process with a result determined by chance. 
	- Each individual result that is possible for a probability experiment is an *outcome*

- The *sample space* of an experiment, denoted by $S$, 
	- is the set of all possible outcomes of that experiment.

- An *event* is a subset of outcomes from the sample space $S$.
	- An event is *simple* if it consists of exactly one outcome
	- And *compound* if it consists of more than one outcome. 

## Example
- Flipping a coin: $S = \{H,T\}$, where $H$ is head, and $T$ is tail.
	- Event $A$ of getting a head: $A = \{H\}$
- Tossing a dice: $S = \{1, 2, 3, 4, 5, 6\}$
	- Event $O$ of getting an odd number: $O = \{1, 3, 5\}$
- Examining product quality: $S = \{G, D\}$, where $G$ is good, and $D$ is defective
- Drawing a raffle ticket
- Tossing a coin, then rolling a die:
	- $S = \{H_{1}, H_{2}, H_{3}, H_{4}, H_{5}, H_{6}, T_{1}, T_{2}, T_{3}, T_{4}, T_{5}, T_{6}\}$
	- Event $B$ of tossing a tail then rolling an even number: $B=\{T_{2}, T_{4}, T_{6}\}$
- Consider a family with three children. What is the sample space for the gender of each child in regard to birth order.
	- Sample space $S=\{GGG, GGB, GBG, GBB, BGG, BGB, BBG, BBB\}$

# Some Relations from Set Theory

- The *complement* of an event $A$, denoted by $A'$, is the set of all outcomes is $S$ that are not contained in $A$.
- The *union* of two events $A$ and $B$, denoted by $A\cup B$, is the event consisting of all outcomes that are either in $A$ **or** in $B$
- The *intersection* of two events $A$ and $B$, denoted by $A \cap B$, is the event consisting of all outcomes that are in both $A$ and $B$
- The *null* event (consisting of no outcomes) is the empty subset of the sample space, denoted by $\emptyset$  
- The sample space itself also an event
	- It can be described as "the event that at least one outcome happens."
- When $A\cap B = \emptyset$ $A$, and $B$ are said to be *mutually exclusive* or *disjoint* events.