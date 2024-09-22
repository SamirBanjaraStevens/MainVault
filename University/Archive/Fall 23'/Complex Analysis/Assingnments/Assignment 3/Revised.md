# 3

### (1) Consider the power series
***

$$  
\sum_{n \geqslant 1} \frac{1}{n} z^{n}=z+\frac{z^{2}}{2}+\frac{z^{3}}{3}+\frac{z^{4}}{4}+\cdots  
$$

#### (a)
***
To determine if the series converges for $z=-i$, we can use the ratio test. The ratio test states that if

$$  
\lim_{{n \to \infty}} \left| \frac{a_{n+1}}{a_n} \right| < 1  
$$

then the series converges absolutely. In this case, $a_n = \frac{1}{n} z^n$, so we have

$$  
\lim_{{n \to \infty}} \left| \frac{\frac{1}{n+1} (-i)^{n+1}}{\frac{1}{n} (-i)^n} \right| = \lim_{{n \to \infty}} \left| \frac{n}{n+1} (-i) \right| = \lim_{{n \to \infty}} \left| \frac{n}{n+1} \right| = 1  
$$

Since the limit is equal to 1, the ratio test is inconclusive. Therefore, we need to use another test to determine convergence.

Let's try the alternating series test. The alternating series test states that if a series has terms that alternate in sign and decrease in magnitude, then the series converges. In this case, the terms alternate in sign and decrease in magnitude, so we can apply the alternating series test.

For $z=-i$, the series becomes

$$  
\sum_{n \geqslant 1} \frac{1}{n} (-i)^{n} = -i + \frac{(-i)^2}{2} - \frac{(-i)^3}{3} + \frac{(-i)^4}{4} - \cdots  
$$

The terms alternate in sign and decrease in magnitude, so the series converges for $z=-i$.

#### (b)
***
To determine if the series converges for $z=\frac{1}{2}(-1+i \sqrt{3})$, we can again use the ratio test. The ratio test gives us

$$  
\lim_{{n \to \infty}} \left| \frac{\frac{1}{n+1} \left(\frac{1}{2}(-1+i \sqrt{3})\right)^{n+1}}{\frac{1}{n} \left(\frac{1}{2}(-1+i \sqrt{3})\right)^n} \right| = 2
$$

Since the limit is less than 1, the series converges absolutely for $z=\frac{1}{2}(-1+i \sqrt{3})$.
***
#### (2) 
***
We are given a power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ that is convergent for $z=-1$. We want to determine what we can conclude about the series

$$  
\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}  
$$

To analyze this series, we can use the convergence properties of power series. The power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ is convergent for $z=-1$, which means that the series converges when $z-2 = -1$, or $z = 1$. Therefore, the series converges for $z=1$.

Now, let's consider the series $\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}$. Since the power series is convergent for $z=1$, we can use the same value of $a_n$ for $n \geqslant 2023$. Therefore, we have

$$  
\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n} = \sum_{n \geqslant 2023} a_{n}(1-3)^{n}  
$$

Simplifying further, we have

$$  
\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n} = \sum_{n \geqslant 2023} a_{n}(-2)^{n}  
$$

From this, we can conclude that the series $\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}$ has the same convergence properties as the series $\sum_{n \geqslant 2023} a_{n}(-2)^{n}$. Therefore, we cannot determine if the series is absolutely convergent, divergent, or could be either, depending on the series.
***
### (3)
***
#### (a)
***
Let $z=-1-2 i$. We want to compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$.

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
***
To compute $\log(z)$, we can use the principal branch of the logarithm function. The principal branch is defined as $\log(z) = \ln|z| + i\arg(z)$, where $\arg(z)$ is the principal argument of $z$. In this case, $z=-1-2i$, so we have

$$  
\log(-1-2i) = \ln|-1-2i| + i\arg(-1-2i)  
$$

The magnitude of $-1-2i$ is $\sqrt{(-1)^2 + (-2)^2} = \sqrt{5}$, and the principal argument can be found using the formula $\arg(z) = \arctan\left(\frac{\Im(z)}{\Re(z)}\right)$. In this case, $\Re(-1-2i) = -1$ and $\Im(-1-2i) = -2$, so we have

$$  
\arg(-1-2i) = \arctan\left(\frac{-2}{-1}\right) = \arctan(2)-\pi
$$

Therefore, $\log(-1-2i) = \ln(\sqrt{5}) + i\arctan(2)-\pi$.
***
To compute $z^i$, we can use the formula $z^i = e^{i\log(z)}$. In this case, $z=-1-2i$ and $\log(z) = \ln(\sqrt{5}) + i\arctan(2)$, so we have

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
***
To compute $i^z$, we can use the formula $i^z = e^{z\log(i)}$. In this case, $z=-1-2i$ and $\log(i) = \ln|i| + i\arg(i)$. The magnitude of $i$ is 1, and the principal argument of $i$ is $\frac{\pi}{2}$. Therefore, we have

$$  
\log(i) = \ln(1) + i\left(\frac{\pi}{2}\right) = i\left(\frac{\pi}{2}\right)  
$$

Substituting into the formula, we have

$$  
i^{-1-2i} = e^{(-1-2i)i\left(\frac{\pi}{2}\right)}  
$$

Using Euler's formula, we can write

$$  
e^{(-1-2i)i\left(\frac{\pi}{2}\right)} = e^{-i\left(\frac{\pi}{2}\right)}e^{-2i^2\left(\frac{\pi}{2}\right)}  
$$

Simplifying further, we have

$$  
e^{-i\left(\frac{\pi}{2}\right)}e^{-2i^2\left(\frac{\pi}{2}\right)} = e^{-i\left(\frac{\pi}{2}\right)}e^{-2(-1)\left(\frac{\pi}{2}\right)} = e^{-i\left(\frac{\pi}{2}\right)}e^{\pi}  
$$

Therefore, $i^{-1-2i} = e^{-i\left(\frac{\pi}{2}\right)}e^{\pi}$.
#### (b)
***
Let $z=-1+t i$, with $t \in \mathbb{R}$. We want to compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$ as functions of $t$.
***
To compute $\operatorname{Exp}(z)$, we can use the definition of the exponential function for complex numbers:

$$  
\operatorname{Exp}(z) = e^z = e^{-1+ti}  
$$

Using Euler's formula, we can write

$$  
e^{-1+ti} = e^{-1}e^{ti} = e^{-1}(\cos(t) + i\sin(t))  
$$

Therefore, $\operatorname{Exp}(z) = e^{-1}(\cos(t) + i\sin(t))$.
***
To compute $\log(z)$, we can use the principal branch of the logarithm function. The principal branch is defined as $\log(z) = \ln|z| + i\arg(z)$, where $\arg(z)$ is the principal argument of $z$. In this case, $z=-1+ti$, so we have

$$  
\log(-1+ti) = \ln|-1+ti| + i\arg(-1+ti)  
$$

The magnitude of $-1+ti$ is $\sqrt{(-1)^2 + t^2} = \sqrt{1+t^2}$, and the principal argument can be found using the formula $\arg(z) = \arctan\left(\frac{\Im(z)}{\Re(z)}\right)$. In this case, $\Re(-1+ti) = -1$ and $\Im(-1+ti) = t$, so we have

$$  
\arg(-1+ti) = \arctan\left(\frac{t}{-1}\right) = \arctan(-t)  
$$

Therefore, $\log(-1+ti) = \ln(\sqrt{1+t^2}) + i\arctan(-t)$.
***
To compute $z^i$, we can use the formula $z^i = e^{i\log(z)}$. In this case, $z=-1+ti$ and $\log(z) = \ln(\sqrt{1+t^2}) + i\arctan(-t)$, so we have

$$  
(-1+ti)^i = e^{i(\ln(\sqrt{1+t^2}) + i\arctan(-t))}  
$$

Using Euler's formula, we can write

$$  
e^{i(\ln(\sqrt{1+t^2}) + i\arctan(-t))} = e^{i\ln(\sqrt{1+t^2})}e^{-\arctan(-t)}  
$$

Simplifying further, we have

$$  
e^{i\ln(\sqrt{1+t^2})}e^{-\arctan(-t)} = (\cos(\ln(\sqrt{1+t^2})) + i\sin(\ln(\sqrt{1+t^2})))e^{-\arctan(-t)}  
$$

Therefore, $(-1+ti)^i = (\cos(\ln(\sqrt{1+t^2})) + i\sin(\ln(\sqrt{1+t^2})))e^{-\arctan(-t)}$.
***
To compute $i^z$, we can use the formula $i^z = e^{z\log(i)}$. In this case, $z=-1+ti$ and $\log(i) = \ln|i| + i\arg(i)$. The magnitude of $i$ is 1, and the principal argument of $i$ is $\frac{\pi}{2}$. Therefore, we have

$$  
\log(i) = \ln(1) + i\left(\frac{\pi}{2}\right) = i\left(\frac{\pi}{2}\right)  
$$

Substituting into the formula, we have

$$  
i^{-1+ti} = e^{(-1+ti)i\left(\frac{\pi}{2}\right)}  
$$

Using Euler's formula, we can write

$$  
e^{(-1+ti)i\left(\frac{\pi}{2}\right)} = e^{-i\left(\frac{\pi}{2}\right)}e^{-ti^2\left(\frac{\pi}{2}\right)}  
$$

Simplifying further, we have

$$  
e^{-i\left(\frac{\pi}{2}\right)}e^{-ti^2\left(\frac{\pi}{2}\right)} = e^{-i\left(\frac{\pi}{2}\right)}e^{-t\left(\frac{\pi}{2}\right)}  
$$

Therefore, $i^{-1+ti} = e^{-i\left(\frac{\pi}{2}\right)}e^{-t\left(\frac{\pi}{2}\right)}$.

### (4)
***
#### (a)
***
Let $n>0$ be a positive real number. We want to compute $n^{-2+i}$.
***
To compute $n^{-2+i}$, we can use the formula $a^b = e^{b\log(a)}$. In this case, $a=n$ and $b=-2+i$, so we have

$$  
n^{-2+i} = e^{(-2+i)\log(n)}  
$$

Using the principal branch of the logarithm function, we have

$$  
\log(n) = \ln|n| + i\arg(n)  
$$

Since $n$ is a positive real number, the principal argument of $n$ is 0. Therefore, we have

$$  
\log(n) = \ln(n) + i(0) = \ln(n)  
$$

Substituting into the formula, we have

$$  
n^{-2+i} = e^{(-2+i)\ln(n)}  
$$

Simplifying further, we have

$$  
n^{-2+i} = e^{-2\ln(n)}e^{i\ln(n)}  
$$

Therefore, $n^{-2+i} = e^{-2\ln(n)}e^{i\ln(n)}$.

#### (b)
***
To show that the series $\sum_{n \geqslant 1} n^{-2+i}$ is absolutely convergent, we can use the comparison test. The comparison test states that if $0 \leqslant a_n \leqslant b_n$ for all $n$ and $\sum_{n \geqslant 1} b_n$ is absolutely convergent, then $\sum_{n \geqslant 1} a_n$ is also absolutely convergent.

In this case, we can compare $n^{-2+i}$ to $n^{-2}$. Since $i$ is a complex number, we can write $n^{-2+i}$ as $n^{-2}n^{i}$. The magnitude of $n^{i}$ is 1, so we have $|n^{-2+i}| = |n^{-2}n^{i}| = |n^{-2}| = n^{-2}$.

Therefore, $0 \leqslant |n^{-2+i}| \leqslant n^{-2}$ for all $n$. Since the series $\sum_{n \geqslant 1} n^{-2}$ is a convergent $p$-series with $p=2 > 1$, we can conclude that the series $\sum_{n \geqslant 1} n^{-2+i}$ is absolutely convergent.

#### (c)
***
Let $z=x+i y \in \mathbb{C}$ such that $x>1$. We want to determine whether the series $\sum_{n \geqslant 1} \frac{1}{n^{z}}$ is convergent or divergent.

To analyze the convergence of this series, we can use the comparison test. The comparison test states that if $0 \leqslant a_n \leqslant b_n$ for all $n$ and $\sum_{n \geqslant 1} b_n$ is convergent, then $\sum_{n \geqslant 1} a_n$ is also convergent.

In this case, we can compare $\frac{1}{n^{z}}$ to $\frac{1}{n^{x}}$. Since $x>1$, we have $0 \leqslant \frac{1}{n^{z}} \leqslant \frac{1}{n^{x}}$ for all $n$.

Now, let's consider the series $\sum_{n \geqslant 1} \frac{1}{n^{x}}$. This series is a convergent $p$-series with $p=x > 1$. Therefore, we can conclude that the series $\sum_{n \geqslant 1} \frac{1}{n^{z}}$ is convergent.

### (5)
***
The Fibonacci sequence is given by $F_{0}=0, F_{1}=1$, and $F_{n}=F_{n-1}+F_{n-2}$ for all $n \geqslant 2$, and the general term is

$$  
F_{n}=\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)  
$$

where $\phi=\frac{1+\sqrt{5}}{2}$. Consider the power series

$$  
\sum_{n \geqslant 0} F_{n} z^{n}=F_{0}+F_{1} z+F_{2} z^{2}+F_{3} z^{3}+\cdots=0+z+z^{2}+2 z^{3}+3 z^{4}+5 z^{5}+8 z^{6}+\cdots  
$$
***
#### (a)
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
***
#### (b)
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