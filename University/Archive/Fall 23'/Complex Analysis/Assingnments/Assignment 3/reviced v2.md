1) 
To determine if the series $\sum_{n \geqslant 1} \frac{1}{n} z^{n}$ converges for $z=-i$, we can use the ratio test. The ratio test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| < 1$, then the series converges absolutely.

Let's apply the ratio test to our series: $$  
\lim_{n \to \infty} \left|\frac{\frac{1}{n+1} (-i)^{n+1}}{\frac{1}{n} (-i)^n}\right| = \lim_{n \to \infty} \left|\frac{n}{n+1} (-i)\right| = \lim_{n \to \infty} \left|\frac{n}{n+1}\right| = 1  
$$

Since the limit is 1, the ratio test is inconclusive. Therefore, we cannot determine if the series converges absolutely for $z=-i$ using the ratio test.

To determine if the series converges conditionally, we can use the alternating series test. The alternating series test states that if a series $\sum_{n \geqslant 1} (-1)^n b_n$ satisfies the conditions: (1) $b_n > 0$ for all $n$, (2) $b_{n+1} \leqslant b_n$ for all $n$, and (3) $\lim_{n \to \infty} b_n = 0$, then the series converges.

In our case, $b_n = \frac{1}{n} (-i)^n$. We can see that $b_n > 0$ for all $n$, and $b_{n+1} \leqslant b_n$ since $\frac{1}{n+1} \leqslant \frac{1}{n}$. Additionally, $\lim_{n \to \infty} \frac{1}{n} = 0$. Therefore, the series converges conditionally for $z=-i$.

#### (b)

we can follow the same steps as above to determine if the series converges for $z=\frac{1}{2}(-1+i \sqrt{3})$. The ratio test yields a limit of 1, so the test is inconclusive. However, the alternating series test cannot be applied since the terms are not alternating. Therefore, we cannot determine if the series converges for $z=\frac{1}{2}(-1+i \sqrt{3})$ using these tests.

### 2)
Since the power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ is convergent for $z=-1$, it means that the series converges when $z-2=-1-2i$. Solving for $z$, we get $z=-1+2-2i=1-2i$.

Now, we can substitute $z=1-2i$ into the series $\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n}$ to determine its convergence. However, we cannot make any conclusions about absolute convergence or divergence without knowing the specific values of $a_n$.

### 3)

#### (a)
To compute $\operatorname{Exp}(z)$, we can use the definition of the exponential function for complex numbers: $$  
\operatorname{Exp}(z) = e^z = e^{-1-2i} = e^{-1}e^{-2i} = \frac{1}{e}(\cos(-2)+i\sin(-2))  
$$
***
To compute $\log(z)$, we can use the principal branch of the complex logarithm: $$  
\log(z) = \log(-1-2i) = \ln|z| + i\arg(z) = \ln|-1-2i| + i\arg(-1-2i)  
$$ We can find the magnitude and argument of $-1-2i$: $$  
|-1-2i| = \sqrt{(-1)^2 + (-2)^2} = \sqrt{1+4} = \sqrt{5}  
$$ $$  
\arg(-1-2i) = \arctan\left(\frac{-2}{-1}\right) = \arctan(2)  
$$ So, we have: $$  
\log(z) = \ln(\sqrt{5}) + i\arctan(2)  
$$

Let's further simplify the expression.

To simplify $\log(-1-2i) = \ln(\sqrt{5}) + i\arctan(2)$, we can use the properties of logarithms and trigonometric functions.

First, we can simplify the natural logarithm term $\ln(\sqrt{5})$. Since $\sqrt{5}$ is a positive real number, we can rewrite it as $\ln(\sqrt{5}) = \frac{1}{2}\ln(5)$.

Next, we can simplify the arctan term $i\arctan(2)$. The arctan function has a periodicity of $\pi$, so we can add or subtract any multiple of $\pi$ to the argument while preserving the value. In this case, we can write $\arctan(2) = \arctan\left(\frac{2}{1}\right)$. Since $2$ and $1$ are both positive, the arctan function will give us a positive angle. Therefore, we have $\arctan(2) = \frac{\pi}{4}$.

Putting it all together, we have: $$  
\log(-1-2i) = \ln(\sqrt{5}) + i\arctan(2) = \frac{1}{2}\ln(5) + i\frac{\pi}{4}  
$$

Therefore, the simplified form of $\log(-1-2i)$ is $\frac{1}{2}\ln(5) + i\frac{\pi}{4}$.

To compute $\log(z)$ for $z=-1-2i$, we can use the complex arithmetic rules and properties of the complex logarithm function.

First, let's express $z$ in polar form. We can find the magnitude and argument of $z$ as follows:

Magnitude: $$|z| = \sqrt{(-1)^2 + (-2)^2} = \sqrt{1 + 4} = \sqrt{5}$$

Argument: $$\arg(z) = \arctan\left(\frac{-2}{-1}\right) = \arctan(2)$$

Now, we can write $z$ in polar form as $z = \sqrt{5}e^{i\arctan(2)}$.

Using the property of the complex logarithm $\log(z) = \ln|z| + i\arg(z)$, we can substitute the values of $|z|$ and $\arg(z)$ into the expression:

$$\log(z) = \ln(\sqrt{5}) + i\arctan(2)$$

Therefore, using complex arithmetic rules and properties of the complex logarithm, we have computed $\log(z)$ for $z=-1-2i$ as $\log(z) = \ln(\sqrt{5}) + i\arctan(2)$.
***
To compute $z^i$, we can use the definition of exponentiation with complex numbers: $$  
z^i = (1-2i)^i = e^{i\log(1-2i)} = e^{i(\ln(\sqrt{5}) + i\arctan(2))}  
$$ Using Euler's formula $e^{ix} = \cos(x) + i\sin(x)$, we can simplify further: $$  
z^i = e^{i\ln(\sqrt{5})}e^{-\arctan(2)} = (\cos(\ln(\sqrt{5}))+i\sin(\ln(\sqrt{5})))e^{-\arctan(2)}  
$$
***
To compute $i^z$, we can use the definition of exponentiation with complex numbers: $$  
i^z = e^{z\log(i)} = e^{(1-2i)\log(i)}  
$$ We can find the logarithm of $i$: $$  
\log(i) = \ln|i| + i\arg(i) = \ln(1) + i\left(\frac{\pi}{2}+2\pi k\right) \quad \text{(for } k \in \mathbb{Z}\text{)}  
$$ So, we have: $$  
i^z = e^{(1-2i)\left(\ln(1) + i\left(\frac{\pi}{2}+2\pi k\right)\right)} = e^{i\left(\frac{\pi}{2}+2\pi k\right)} = \cos\left(\frac{\pi}{2}+2\pi k\right) + i\sin\left(\frac{\pi}{2}+2\pi k\right)  
$$

#### (b)
To compute $\operatorname{Exp}(z)$, $\log(z)$, $z^i$, and $i^z$ as functions of $t$, we can substitute $z=-1+ti$ into the formulas derived in part (a). The calculations will involve the same steps, but the specific values of $z$ will be different.

### 4)
#### (a)
To compute $n^{-2+i}$, we can use the definition of exponentiation with complex numbers: $$  
n^{-2+i} = e^{(2-i)\log(n)} = e^{(2-i)(\ln(n)+i\arg(n))}  
$$ Since $n$ is a positive real number, $\arg(n) = 0$. Therefore, we have: $$  
n^{-2+i} = e^{(2-i)\ln(n)} = e^{2\ln(n)-i\ln(n)}  
$$ Using Euler's formula, we can simplify further: $$  
n^{-2+i} = e^{2\ln(n)}e^{-i\ln(n)} = n^2(\cos(\ln(n)) - i\sin(\ln(n)))  
$$

#### (b)
To show that the series $\sum_{n \geqslant 1} n^{-2+i}$ is absolutely convergent, we can use the comparison test. We can compare the series to the convergent series $\sum_{n \geqslant 1} n^{-2}$.

Let's consider the absolute value of each term in the series: $$  
|n^{-2+i}| = |n^{-2}(\cos(\ln(n)) - i\sin(\ln(n)))| = n^{-2}  
$$ Since $n^{-2}$ is a convergent series, and $|n^{-2+i}| \leqslant n^{-2}$ for all $n \geqslant 1$, we can conclude that the series $\sum_{n \geqslant 1} n^{-2+i}$ is absolutely convergent.

(c) To determine if the series $\sum_{n \geqslant 1} \frac{1}{n^{z}}$ is convergent or divergent for $z=x+iy$, where $x>1$, we can use the comparison test. We can compare the series to the convergent series $\sum_{n \geqslant 1} \frac{1}{n^{x}}$.

Let's consider the absolute value of each term in the series: $$  
\left|\frac{1}{n^{z}}\right| = \left|\frac{1}{n^{x+iy}}\right| = \frac{1}{n^x}  
$$ Since $x>1$, we have $\frac{1}{n^x} \leqslant \frac{1}{n}$ for all $n \geqslant 1$. Therefore, the series $\sum_{n \geqslant 1} \frac{1}{n^{z}}$ is convergent for $z=x+iy$, where $x>1$.

### 5)
#### (a)
To determine the radius of convergence of the power series $\sum_{n \geqslant 0} F_{n} z^{n}$, we can use the ratio test. The ratio test states that if $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| < 1$, then the series converges absolutely.

Let's apply the ratio test to our series: $$  
\lim_{n \to \infty} \left|\frac{F_{n+1} z^{n+1}}{F_n z^n}\right| = \lim_{n \to \infty} \left|\frac{F_{n+1}}{F_n} z\right|  
$$ Since the Fibonacci sequence grows exponentially, we have $\lim_{n \to \infty} \left|\frac{F_{n+1}}{F_n}\right| = \phi$, where $\phi$ is the golden ratio. Therefore, the limit becomes: $$  
\lim_{n \to \infty} \left|\frac{F_{n+1}}{F_n} z\right| = \phi |z|  
$$

For the series to converge absolutely, we need $\phi |z| < 1$. Therefore, the radius of convergence is $\frac{1}{\phi}$.

#### (b)
For $z$ in the disk of convergence, we can determine the sum of the series by substituting $z$ into the formula for the Fibonacci sequence: $$  
\sum_{n \geqslant 0} F_{n} z^{n} = \sum_{n \geqslant 0} \left(\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)\right) z^{n}  
$$ Simplifying further, we have: $$  
\sum_{n \geqslant 0} \left(\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)\right) z^{n} = \frac{1}{\sqrt{5}}\sum_{n \geqslant 0} \left(\phi^{n} z^{n} - (-\phi)^{-n} z^{n}\right)  
$$ Using the geometric series formula, we can express the sum as: $$  
\frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi z} - \frac{1}{1-(-\phi) z}\right) = \frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi z} - \frac{1}{1+\phi z}\right)  
$$

Therefore, the sum of the series for $z$ in the disk of convergence is $\frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi z} - \frac{1}{1+\phi z}\right)$.