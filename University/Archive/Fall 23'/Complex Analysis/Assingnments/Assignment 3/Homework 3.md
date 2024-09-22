***
Samir Banjara
Ashot Melkonyan
***
#### Question 1
Consider the power series

$$
\sum_{n \geqslant 1} \frac{1}{n} z^{n}=z+\frac{z^{2}}{2}+\frac{z^{3}}{3}+\frac{z^{4}}{4}+\cdots
$$
***
##### a) 
 Does the series converge for $z=-i$ ? (Note: changed from $z=i$ in first version)
 ***
 **Sol:** 

To determine if the series $\sum_{n \geqslant 1} \frac{1}{n} z^{n}$ converges for $z=-i$, we can use the ratio test. The ratio test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| < 1$, then the series converges absolutely.

Let's apply the ratio test to our series: 
$$  
\lim_{n \to \infty} \left|\frac{\frac{1}{n+1} (-i)^{n+1}}{\frac{1}{n} (-i)^n}\right| = \lim_{n \to \infty} \left|\frac{n}{n+1} (-i)\right| = \lim_{n \to \infty} \left|\frac{n}{n+1}\right| = 1  
$$

Since the limit is 1, the ratio test is inconclusive. 
Therefore, we cannot determine if the series converges absolutely for $z=-i$ using the ratio test.

To determine if the series converges conditionally, we can use the alternating series test. The alternating series test states that if a series $\sum_{n \geqslant 1} (-1)^n b_n$ satisfies the conditions: (1) $b_n > 0$ for all $n$, (2) $b_{n+1} \leqslant b_n$ for all $n$, and (3) $\lim_{n \to \infty} b_n = 0$, then the series converges.

In our case, $b_n = \frac{1}{n} (-i)^n$. We can see that $b_n > 0$ for all $n$, and $b_{n+1} \leqslant b_n$ since $\frac{1}{n+1} \leqslant \frac{1}{n}$. Additionally, $\lim_{n \to \infty} \frac{1}{n} = 0$. Therefore, the series converges conditionally for $z=-i$.
##### b)
Does the series converge for $z=\frac{1}{2}(-1+i \sqrt{3})$ ?
***
To determine whether the series converges for $z = \frac{1}{2}(-1+i\sqrt{3})$, we can again use the ratio test.

The ratio test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| < 1$, then the series converges absolutely.

$$
\begin{align}
  
\left| \frac{a_{n+1}}{a_n} \right| &= \left| \frac{\frac{1}{n}\left(\frac{1}{2}(-1+i\sqrt{3})\right)^{n+1}}{\frac{1}{n}\left(\frac{1}{2}(-1+i\sqrt{3})\right)^n} \right| \\
&=\left|\, \frac{\frac{1}{n+1}\left(\frac{-1+i\sqrt{3}}{2}\right)^{n+1}}{\frac{1}{n}\left(\frac{-1+i\sqrt{3}}{2}\right)^n}  \,\right|\\
&=\left|\, \frac{\frac{1}{n+1}\left(-1+i\sqrt{3}\right)}{\frac{1}{n}\cdot \:2} \,\right| \\

&=\left|\frac{\left(-1+\sqrt{3}i\right)n}{\left(n+1\right)\cdot \:2}\right| \\


\end{align}
$$



Given the sequence:
$$ \frac{(-1 + i\sqrt{3})n}{2(n+1)} $$
we need to find:
$$ \lim_{n \to \infty} a_n $$

Separate the sequence into its real and imaginary parts:

Real part:
$$ \text{Re}\left( \frac{(-1 + i\sqrt{3})n}{2(n+1)} \right) = \frac{-n}{2(n+1)} $$

Imaginary part:
$$ \text{Im}\left( \frac{(-1 + i\sqrt{3})n}{2(n+1)} \right) = \frac{\sqrt{3}n}{2(n+1)}$$

Now, let's find the limit of each part as $( n \to \infty ):$

For the real part:
$$ \lim_{n \to \infty} \frac{-n}{2(n+1)} = \lim_{n \to \infty} \frac{-1}{2 + \frac{2}{n}} $$
As $( n \to \infty )$, the term $( \frac{2}{n} )$ approaches $0$, hence:
$$ \lim_{n \to \infty} \frac{-n}{2(n+1)} = \frac{-1}{2} $$

For the imaginary part:
$$ \lim_{n \to \infty} \frac{\sqrt{3}n}{2(n+1)} = \lim_{n \to \infty} \frac{\sqrt{3}}{2 + \frac{2}{n}} $$
Similarly, as $( n \to \infty )$, the term $( \frac{2}{n} )$ approaches 0, so:
$$ \lim_{n \to \infty} \frac{\sqrt{3}n}{2(n+1)} = \frac{\sqrt{3}}{2} $$

Thus, the final result is a value less than 1, the series converges for $z = \frac{1}{2}(-1+i\sqrt{3})$


#### Question 2
We are given a power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ that is convergent for $z=-1$. What can we conclude about the series $$
\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n} ?
$$

Is it absolutely convergent, is it divergent, or could be either, depending on the series?
***
**Sol:**
To determine the convergence of the series $\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}$, we can use the ratio test.

The ratio test states that if $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| < 1$, then the series converges absolutely. If $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| > 1$, then the series diverges. If $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = 1$, the test is inconclusive.

Let's apply the ratio test to the given series. We have: $$\begin{align*}  
\left| \frac{a_{n+1}(-2-2i)^{n+1}}{a_n(-2-2i)^n} \right| &= \left| \frac{a_{n+1}}{a_n} \right| \cdot \left| -2-2i \right| \\  
&= \left| \frac{a_{n+1}}{a_n} \right| \cdot 2\sqrt{2}  
\end{align*}$$

Since the series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ is convergent for $z=-1$, we know that $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| < 1$ for $z=-1$. Therefore, we have: $$\begin{align*}  
\lim_{n \to \infty} \left| \frac{a_{n+1}(-2-2i)^{n+1}}{a_n(-2-2i)^n} \right| &= \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| \cdot 2\sqrt{2} \\  
&< 1 \cdot 2\sqrt{2} \\  
&= 2\sqrt{2} \\  
&< 1  
\end{align*}$$

Since $\lim_{n \to \infty} \left| \frac{a_{n+1}(-2-2i)^{n+1}}{a_n(-2-2i)^n} \right| < 1$, we can conclude that the series $\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}$ is absolutely convergent.
***
*Additional method:*
Given that the power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ is convergent for $z=-1$, we know that the series $\sum_{n \geqslant 0} a_{n}(-3)^{n}$ converges.

To analyze the convergence of the series $\sum_{n \geqslant 2023} a_{n}(-2-2i)^{n}$, we'll use the comparison test.

First, let's find the magnitude of $(-2-2i)^{n}$: $$\begin{align*}  
(-2-2i)^{n} &= ((-2)(1+i))^{n} \\  
&= (-2)^{n}(1+i)^{n}  
\end{align*}$$

The magnitude of $1+i$ is $\sqrt{2}$. So, the magnitude of $(1+i)^{n}$ is $(\sqrt{2})^{n} = 2^{n/2}$. Hence, the magnitude of $(-2-2i)^{n}$ is: $$\begin{align*}  
2^{n} \cdot 2^{n/2} &= 2^{3n/2} \\  
&= 2^{3n/2}  
\end{align*}$$

Thus, the magnitude of the general term for $\sum_{n \geqslant 2023} a_{n}(-2-2i)^{n}$ is: $|a_{n}| \cdot 2^{3n/2}$

Now, we know that $\sum_{n \geqslant 0} a_{n}(-3)^{n}$ converges. Therefore, $\sum_{n \geqslant 0} |a_{n}| \cdot 3^{n}$ is absolutely convergent.

Using the comparison test, we can compare the two series: $\sum_{n \geqslant 0} |a_{n}| \cdot 3^{n}$ and $\sum_{n \geqslant 2023} |a_{n}| \cdot 2^{3n/2}$

Since $2^{3n/2} \leq 3^{n}$ for all $n \geqslant 0$, it means that: $\sum_{n \geqslant 2023} |a_{n}| \cdot 2^{3n/2} \leq \sum_{n \geqslant 2023} |a_{n}| \cdot 3^{n}$

And since the series on the right-hand side is absolutely convergent, the series on the left-hand side is also absolutely convergent.

Therefore, the series $\sum_{n \geqslant 2023} a_{n}(-2-2i)^{n}$ is absolutely convergent.
#### Question 3
##### a)
Let $z=-1-2 i$. Compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$.
***

###### $\operatorname{Exp}(z)$

Let $z=-1-2 i$. We want to compute 
$\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$.

To compute $\operatorname{Exp}(z)$, we can use the definition of the exponential function for complex numbers:

$$  
\operatorname{Exp}(z) = e^z = e^{-1-2i}  
$$

Using Euler's formula, $e^{i\theta} = \cos(\theta) + i\sin(\theta)$, we can write

$$  
e^{-1-2i} = e^{-1}e^{-2i} = e^{-1}(\cos(-2) + i\sin(-2)) 
$$

Simplifying further, we have

$$  
e^{-1-2i} = e^{-1}(\cos(-2) - i\sin(2))  
$$

Therefore, $\operatorname{Exp}(z) = e^{-1}(\cos(-2) - i\sin(2))$.
###### $\log(z)$
To compute $\log(z)$, we can use the principal branch of the logarithm function. The principal branch is defined as $\log(z) = \ln|z| + i\arg(z)$, where $\arg(z)$ is the principal argument of $z$. In this case, $z=-1-2i$, so we have

$$  
\log(-1-2i) = \ln|-1-2i| + i\arg(-1-2i)  
$$

The magnitude of $-1-2i$ is $\sqrt{(-1)^2 + (-2)^2} = \sqrt{5}$, and the principal argument can be found using the formula $\arg(z) = \arctan\left(\frac{\Im(z)}{\Re(z)}\right)$. In this case, $\Re(-1-2i) = -1$ and $\Im(-1-2i) = -2$, so we have

$$  
\arg(-1-2i) = \arctan\left(\frac{-2}{-1}\right) = \arctan(2) - \pi
$$

Therefore, 
$$
\begin{align}
\log(-1-2i) &= \ln(\sqrt{5}) + i\arctan(2)-\pi\\
\end{align}
$$
###### $z^i$
$z^i=\operatorname{Exp}(i \log(z))$
or $z^i = e^{i\log(z)}$
Substituting the value of log⁡(z)log(z) which we computed in the previous step, we get:
$z^i=\operatorname{Exp}(\ln(\sqrt{5}) + i\arctan(2))$

In this case, $z=-1-2i$ and $\log(z) = \ln(\sqrt{5}) + i\arctan(2)$, so we have

$$  
(-1-2i)^i = e^{i(\ln(\sqrt{5}) + i\arctan(2))}  
$$

Using Euler's formula, we can write

$$  
e^{i(\ln(\sqrt{5}) + i\arctan(2))} = e^{i\ln(\sqrt{5})}e^{-\arctan(2)}  
$$

Simplifying further, we have

$$  
e^{i\ln(\sqrt{5})}e^{-\arctan(2)} = (\cos(\ln(\sqrt{5})) + i\sin(\ln(\sqrt{5})))e^{-\arctan(2)}  
$$

Therefore, $(-1-2i)^i = (\cos(\ln(\sqrt{5})) + i\sin(\ln(\sqrt{5})))e^{-\arctan(2)}$.
###### $i^z$

##### b)
Let $z=-1+t i$, with $t \in \mathbb{R}$. Compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$ as functions of $t$.
***
###### $e^z$
To compute $\operatorname{Exp}(z)$, we can use the definition of the exponential function for complex numbers:

$$  
\operatorname{Exp}(z) = e^z = e^{-1+ti}  
$$

Using Euler's formula, we can write

$$  
e^{-1+ti} = e^{-1}e^{ti} = e^{-1}(\cos(t) + i\sin(t))  
$$

Therefore, $\operatorname{Exp}(z) = e^{-1}(\cos(t) + i\sin(t))$.
###### $\log(z)$
The complex logarithm is defined as $\log(z) = \ln|z| + i\arg(z)$

Here, $z = -1 + ti$, so $|z| = \sqrt{(-1)^2 + t^2} = \sqrt{1 + t^2}$

The argument of $z$ is $\arg(z) = \arctan\left(\frac{t}{-1}\right) = -\arctan(t)$

Therefore, $\log(z) = \ln(\sqrt{1 + t^2}) - i\arctan(t)$

To compute $\log(z)$, we can use the principal branch of the logarithm function. The principal branch is defined as $\log(z) = \ln|z| + i\arg(z)$, where $\arg(z)$ is the principal argument of $z$. In this case, $z=-1+ti$, so we have

$$  
\log(-1+ti) = \ln|-1+ti| + i\arg(-1+ti)  
$$

###### $z^i$


We have $z = -1 + ti$, and we want to compute $z^{i}$.

First, we express $z$ in polar form. The modulus of $z$ is $|z| = \sqrt{(-1)^2 + t^2} = \sqrt{1 + t^2}$, and the argument of $z$ is $\arg(z) = \arctan\left(\frac{t}{-1}\right) = -\arctan(t)$.

So, $z = |z|(\cos(\arg(z)) + i\sin(\arg(z))) = \sqrt{1 + t^2}(\cos(-\arctan(t)) + i\sin(-\arctan(t)))$.

Now, we can compute $z^{i}$ using the formula $z^{i} = |z|^{i}(\cos(i\arg(z)) + i\sin(i\arg(z)))$.

Substituting the expressions for $|z|$ and $\arg(z)$, we get $z^{i} = (\sqrt{1 + t^2})^{i}(\cos(-i\arctan(t)) + i\sin(-i\arctan(t)))$.

Simplifying, we get $z^{i} = \sqrt{1 + t^2}^{i} \cdot e^{-\arctan(t)}$.
###### $i^z$
$i^{z} = e^{z\log(i)}$

Again, we're using the property of exponents that $a^{bc} = (a^b)^c = (a^c)^b$. We're applying this property with $a = e$, $b = z$, and $c = \log(i)$.

5. $i^{z} = e^{(-1 + ti)\cdot i\frac{\pi}{2}} = e^{-\frac{\pi}{2} - \frac{\pi t}{2}i}$

This is just substituting the expression for $z$ and $\log(i)$ that we computed earlier.

We have $z = -1 + ti$, and we want to compute $i^{z}$.

First, we express $i$ in polar form. The modulus of $i$ is $|i| = 1$, and the argument of $i$ is $\arg(i) = \frac{\pi}{2}$.

So, $i = |i|(\cos(\arg(i)) + i\sin(\arg(i))) = \cos(\frac{\pi}{2}) + i\sin(\frac{\pi}{2})$.

Now, we can compute $i^{z}$ using the formula $i^{z} = |i|^{z}(\cos(z\arg(i)) + i\sin(z\arg(i)))$.

Substituting the expressions for $|i|$ and $\arg(i)$, we get $i^{z} = 1^{z}(\cos((-1 + ti)\frac{\pi}{2}) + i\sin((-1 + ti)\frac{\pi}{2}))$.

Simplifying, we get $i^{z} = e^{-\frac{\pi}{2} - \frac{\pi t}{2}i}$.

So, the final results are:

$z^{i} = \sqrt{1 + t^2}^{i} \cdot e^{-\arctan(t)}$

$i^{z} = e^{-\frac{\pi}{2} - \frac{\pi t}{2}i}$
#### Question 4
##### a)
Let $n>0$ be a positive real number. Compute $n^{-2+i}$.
***
Using the exponential function, we can rewrite this as $e^{(-2+i) \ln(n)}$.

From the notes, we know that the exponential of a complex number $x+iy$ is given by $e^{x}(\cos y+i \sin y)$. Applying this to our problem, we get:

$$  
n^{-2+i} = e^{(-2+i) \ln(n)} = e^{-2 \ln(n)}(\cos(\ln(n)) + i \sin(\ln(n))) = \frac{1}{n^2}(\cos(\ln(n)) + i \sin(\ln(n)))  
$$
##### b)
Show that the series

$$
\sum_{n \geqslant 1} n^{-2+i}
$$

is absolutely convergent.
***
A series $\sum_{n \geqslant 1} a_n$ is absolutely convergent if the series $\sum_{n \geqslant 1} |a_n|$ is convergent.

In this case, $a_n = n^{-2+i} = \frac{1}{n^2} \cdot (cos(\ln(n)) + isin(\ln(n)))$.

The absolute value of $a_n$ is $|a_n| = |\frac{1}{n^2} \cdot (cos(\ln(n)) + isin(\ln(n)))| = \frac{1}{n^2} * |cos(\ln(n)) + isin(\ln(n))|$.

Since $|cos(\ln(n)) + isin(\ln(n))| \leq 2$ for all $n$, we have $|a_n| \leq \frac{2}{n^2}$.

The series $\sum_{n \geqslant 1} \frac{2}{n^2}$ is a convergent p-series with $p = 2 > 1$, so by the comparison test, the series $\sum_{n \geqslant 1} |a_n|$ is also convergent.

Therefore, the series $\sum_{n \geqslant 1} n^{-2+i}$ is absolutely convergent.
##### c)
Let $z=x+i y \in \mathbb{C}$ such that $x>1$. Determine whether the series

$$
\sum_{n \geqslant 1} \frac{1}{n^{z}}
$$

is convergent or divergent.
***
Here, $z = x + iy$ with $x > 1$.

The series $\sum_{n \geqslant 1} \frac{1}{n^{z}} = \sum_{n \geqslant 1} \frac{1}{n^{x+iy}} = \sum_{n \geqslant 1} \frac{1}{n^x \cdot n^{iy}}$.

We know that $\sum_{n \geqslant 1} \frac{1}{n^x}$ is a convergent p-series since $x > 1$.

For $\sum_{n \geqslant 1} n^{iy}$, we can use Euler's formula again to get $\sum_{n \geqslant 1} (cos(y\cdot ln(n)) + isin(y\cdot \ln(n)))$.

This is a sum of a cosine and sine series, both of which are bounded.

Therefore, the product of a convergent series and a bounded series is also convergent.

So, the series $\sum_{n \geqslant 1} \frac{1}{n^{z}}$ is convergent.
#### Question 5
The Fibonacci sequence is given by $F_{0}=0, F_{1}=1$, and $F_{n}=F_{n-1}+F_{n-2}$ for all $n \geqslant 2$, and the general term is

$$
F_{n}=\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)
$$

where $\phi=\frac{1+\sqrt{5}}{2}$. Consider the power series

$$
\sum_{n \geqslant 0} F_{n} z^{n}=F_{0}+F_{1} z+F_{2} z^{2}+F_{3} z^{3}+\cdots=0+z+z^{2}+2 z^{3}+3 z^{4}+5 z^{5}+8 z^{6}+\cdots
$$
***
##### a)
Determine the radius of convergence of the power series.
***
To determine the radius of convergence of the power series, we can use the ratio test. The ratio test states that if

$$  
\lim_{{n \to \infty}} \left| \frac{a_{n+1}}{a_n} \right| < 1  
$$

then the series converges absolutely. In this case, $a_n = F_n$, so we have

$$  
\lim_{{n \to \infty}} \left| \frac{F_{n+1}}{F_n} \right| = \lim_{{n \to \infty}} \left| \frac{\frac{1}{\sqrt{5}}\left(\phi^{n+1}-(-\phi)^{-(n+1)}\right)}{\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)} \right| = \lim_{{n \to \infty}} \left| \frac{\phi^{n+1}-(-\phi)^{-(n+1)}}{\phi^{n}-(-\phi)^{-n}} \right|  
$$

Simplifying further, we have

$$  
\lim_{{n \to \infty}} \left| \frac{\phi^{n+1}-(-\phi)^{-(n+1)}}{\phi^{n}-(-\phi)^{-n}} \right| = \lim_{{n \to \infty}} \left| \frac{\phi^{n+1}-(-\phi)^{-(n+1)}}{\phi^{n}-(-\phi)^{-n}} \right| = \lim_{{n \to \infty}} \left| \frac{\phi^{n+1}-(-\phi)^{-(n+1)}}{\phi^{n}-(-\phi)^{-n}} \right| = \phi  
$$

Therefore, the radius of convergence of the power series is $\phi$.
##### b)
For $z$ in the disk of convergence, determine the sum of the series.
$\cfrac{\left| -1+\sqrt{ 3 }i \right|\left| n \right|}{2\left| n+1 \right|}$
***
For $z$ in the disk of convergence, we can determine the sum of the series by evaluating the power series at $z$. In this case, the power series is

$$  
\sum_{n \geqslant 0} F_{n} z^{n}=F_{0}+F_{1} z+F_{2} z^{2}+F_{3} z^{3}+\cdots=0+z+z^{2}+2 z^{3}+3 z^{4}+5 z^{5}+8 z^{6}+\cdots  
$$

To find the sum of the series, we can substitute $z$ into the power series and simplify. For example, if $z=1$, we have

$$  
\sum_{n \geqslant 0} F_{n} (1)^{n}=F_{0}+F_{1} (1)+F_{2} (1)^{2}+F_{3} (1)^{3}+\cdots=0+1+1+2+3+5+8+\cdots  
$$

which is the Fibonacci sequence. Therefore, for $z$ in the disk of convergence, the sum of the series is the Fibonacci sequence.