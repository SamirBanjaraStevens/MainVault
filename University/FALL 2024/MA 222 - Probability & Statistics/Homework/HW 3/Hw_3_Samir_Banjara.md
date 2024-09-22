Pledge: I pledge my honor that I have abided by the Stevens Honor System.
Signature: Samir Banjara

# Problem 1:

**A)** Find the probability of rolling two dice and not getting doubles.
***
*Solution:*
Given the set of possibilities of rolling two dice, 
$$
s = 
\begin{align}
&\left\{(1,1), (2,1), (3, 1), (4, 1), (5, 1), (6, 1)\right\}  \\
 &\left\{(1,2), (2,2), (3, 2), (4, 2), (5, 2), (6, 2)\right\}  \\
 & \left\{(1,3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3)\right\} \\
 & \left\{(1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4)\right\} \\
 & \left\{(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)\right\} \\
& \left\{(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)\right\}
\end{align}
$$
$30$ rolls out of $36$ are not an ordered double. Thus the probability is $\frac{30}{36}$.

**B)** Given that every fifth person in line will get a coupon for a free box of popcorn at the movies, what is the probability that you don’t get a coupon when you’re in line?
***
*Solution:*
Every $5^{th}$ person in line gets a coupon. That means $1$ person out of $5$ gets a coupon. The probability of not getting a coupon is then $1-\cfrac{1}{5}=\cfrac{4}{5}$ 

# Problem 2:
Insulin pens used to administer a patient’s insulin at hospitals have a malfunction rate of 9%. This means that out of a box of 200 pens, 18 are defective in some way and must be thrown away. Find the probability of randomly selecting 3 defective insulin pens in a row from a brand-new box of 200 pens, if a defective pen is immediately discarded.
***
*Solution:*
Probability of randomly selecting a defective pen out of a brand new box of $200$ is $\frac{18}{200}$. And since we are discarding the pen, the probability of picking another defective pen is $\left( \cfrac{18-1}{200-1} \right)=\left( \cfrac{17}{199} \right)$. And the probability that the third pen  will be defective is $\left( \cfrac{16}{198} \right)$. Then the probability that each pen picked up in a row that will be defective is, 
$$\left( \frac{18}{200} \right)\left( \frac{17}{199} \right) \left( \cfrac{16}{198} \right) = 0.000621 \times 100\% = 0.0621\%$$


# Problem 3:
The following table displays the breakdown of attendees at an International Biology conference by country and their role in the company they were representing.

|          | Canada | France | South Korea | UK  | US  |
| -------- | ------ | ------ | ----------- | --- | --- |
| CEO      | 138    | 45     | 4           | 19  | 117 |
| Director | 8      | 4      | 25          | 6   | 63  |
| Partner  | 23     | 7      | 3           | 20  | 103 |
| Chairman | 12     | 9      | 3           | 9   | 62  |
| Other    | 112    | 146    | 154         | 143 | 2103    |

A random attendee is selected for an interview.

**a)** What is the probability that a Partner is selected, given that the attendee is from South Korea? 
***
*Solution:*
Given two events $A$ and $B$, the conditional probability of $A$ given $B$ is given by $P(A|B)=\cfrac{P(A\cap B)}{P(B)}$.
Given there is $A=3$ Partners who are Korean, and $B = 189$ total Korea participants, thus, the probability is given by, $$\cfrac{3}{189}=\cfrac{1}{63}$$

**b)** What is the probability that a Canadian is selected, given that the attendee is a director of the company? 
***
*Solution:*
Given there is $A=8$ Canadian's who are Directors, and $B = 106$ total participants who are directors, thus, the probability is given by, $$\cfrac{8}{106}$$
**c)** What is the probability that a director is selected, given that the attendee is Canadian? 
***
*Solution:*
Given there is $A=8$ Canadian's who are Directors, and $B = 293$ total participants who are Canadian, thus, the probability is given by, $$\cfrac{8}{293}$$
**d)** What is the probability that a CEO is selected, given that the attendee is from the continent of North America?
***
*Solution:*
The total number of North American CEO's is $255$ and the total number of North American Attendants is $2741$, the probability that they are a CEO given that they are from North America is $\cfrac{255}{2741}$

# Problem 4:
Every 6 months, university email requires that a new 5-igit password be set up. No digits are allowed to be repeated and it must be different from your last two passwords. If you let your computer randomly choose a 5-digit code for you with no repeating digits, what is the probability that it will choose one of the last 2 passwords you’ve had? Round your answer to five decimal places.
***
*Solution:*
Given that we have to make a $5$-digit password without repeating digits from the set of $\left\{ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 \right\}$. We can calculate how many digits can be a possible input in each index, until we are left with a $5$ digit number. 

$(10)_{n=0}$ digits can take the $0$-th place. Tossing one out.
Then $(9)_{n=1}$ digits can take the $1$-st place.
Then $(8)_{n=2}$ digits can take the $2$-st place.
Then $(7)_{n=3}$ digits can take the $3$-st place.
And finally, $(6)_{n=4}$ digits can take the $4$-st place.

So the total number of possible passwords we could have is, $10\times 9 \times 8 \times 7 \times 6 = 30240$. 

The probability that $2$ of the computer generated passwords are their previous password 2 password is $\cfrac{2}{30240}=0.00007$



# Problem 5:
Virginia’s Veggie Café offers 5 types of homemade bread, 10 toppings, and 6 different condiments. How many different super sandwiches can be made if a super sandwich consists of 6 different toppings and 2 different condiments? 
***
*Solution:*
There are only a total of $\mathcal{C}_{1,5}=5$ ways to combine the breads. Out of $10$ toppings, the super sandwich has only $6$, so there are $\mathcal{C}_{6,10}=210$ combinations of toppings. And $\mathcal{C}_{2, 6} = 15$ possible ways of combining the condiments. Thus the total number of sandwich combinations are $5 \times 210 \times 15 = 15,750$.

# Problem 6: 
Ashley’s Internet service is terribly unreliable. In fact, on any given day, there is a 15% chance that her Internet connection will be lost at some point that day. What is the probability that her Internet service is not broken for five days in a row? 
***
*Solution:*
Given there is a $15 \%$ chance that her wifi doesn't work, there is a $85\%$ chance that is does work on a given day. $P(Works) = 1 - 0.15 = 0.85$

$$\left( 0.85 \right)\times\left( 0.85 \right)\times\left( 0.85 \right)\times\left( 0.85 \right)\left( 0.85 \right) = (0.85)^{5} $$
# Problem 7: 
Because Tristan has diabetes, he must make sure that his daily diet includes 2 vegetables, 3 fruits, and 2 breads. At the grocery store, he has a choice of 20 vegetables, 8 fruits, and 5 breads. 

a) In how many ways can he make up his daily requirements if he doesn’t like to eat 2 helpings of the same thing in one day? 
***
*Solution:*
Combinations of each staple in their diet:
- Vegetables: $\mathcal{C}_{2, 20} = \cfrac{20!}{2!(20-2)!}=56$
- Fruits: $\mathcal{C}_{3, 8} = \cfrac{8!}{3!(8-3)!}=190$
- Breads: $\mathcal{C}_{2, 5} = \cfrac{5!}{2!(5-2)!}=10$
So the number of combinations for his daily requirement without have the same helpings of the same thing is $106,400$

b) What’s the probability that a random choice from his possibilities would yield either carrots or spinach in its menu, given that carrots and spinach are both vegetable choices at the grocery store?
***
*Solution:*
Well we know that there is total number of $190$ combinations for his veggies. 

We can calculate the number of combinations of of 20 veggies. 

Number of ways to choose 2 veggies which must include carrots:
$\mathcal{C}(19,1)=19$

Number of ways to choose 2 veggies which must include Spinach:
$\mathcal{C}(19,1)=19$

Number of way of choosing 2 veggies that are from carrots and Spinach
$\mathcal{2,2} = 1$

Thus using *Inclusion-Exclusion Principle*, the number of vegetable combinations including Carrots or Spinach is,
$$P(A)+P(B)-P(A\cap B)=19+19-1=37$$

Total combinations of daily serving that have carrots or vegetables, is $37 \times 56 \times 10 = 20720$.

Probability that his meal will have either carrots or veggies is $\cfrac{20720}{106400}\approx0.1947\times 100\% = 19.47\%$ 