(1)

(a) To determine whether the series converges for $z = -i$, we can use the ratio test.

The ratio of consecutive terms is given by

$$  
\left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{\frac{1}{n+1}(-i)^{n+1}}{\frac{1}{n}(-i)^n} \right| = \left| \frac{n}{n+1} \right| = \frac{n}{n+1}.  
$$

Taking the limit as $n$ approaches infinity, we have

$$  
\lim_{{n\to\infty}} \frac{n}{n+1} = 1.  
$$

Since the limit is less than 1, the series converges for $z = -i$.

(b) To determine whether the series converges for $z = \frac{1}{2}(-1+i\sqrt{3})$, we can again use the ratio test.

The ratio of consecutive terms is given by

$$  
\left| \frac{a_{n+1}}{a_n} \right| = \left| \frac{\frac{1}{n}\left(\frac{1}{2}(-1+i\sqrt{3})\right)^{n+1}}{\frac{1}{n}\left(\frac{1}{2}(-1+i\sqrt{3})\right)^n} \right| = \left| \frac{\frac{1}{2}(-1+i\sqrt{3})}{1} \right| = \frac{1}{2}\sqrt{3}.  
$$

Since the ratio is a constant value less than 1, the series converges for $z = \frac{1}{2}(-1+i\sqrt{3})$.

(2)

Since $\sum_{n \geq 0} a_n(z-2)^n$ is convergent for $z = -1$, it converges within a certain radius of convergence. Let's call this radius $R$.

For $z = -2 - 2i$, we can calculate the distance from $-1$ using the distance formula:

$$  
\sqrt{((-2) - (-1))^2 + ((-2) - 0)^2} = \sqrt{2 + 4} = \sqrt{6}.  
$$

Since $\sqrt{6} < R$, the series $\sum_{n \geq 2023} a_n(-2-2i)^n$ is absolutely convergent.

(3)

(a)

To compute $\operatorname{Exp}(z)$, we can use the formula $\operatorname{Exp}(z) = \sum_{n \geq 0} \frac{z^n}{n!}$.

$$  
\operatorname{Exp}(z) = \sum_{n \geq 0} \frac{(-1-2i)^n}{n!} = 1 + (-1-2i) + \frac{(-1-2i)^2}{2} + \frac{(-1-2i)^3}{3!} + \cdots  
$$

To compute $\log(z)$, we can use $\log(z) = \log|z| + i\arg(z)$, where $\arg(z)$ is the principal value of the argument of $z$.

$$  
\log(z) = \log |-1-2i| + i\arg(-1-2i) = \log \sqrt{5} + i\left(\frac{3\pi}{2}\right)  
$$

To compute $z^i$, where $i = \sqrt{-1}$,

$$  
z^i = (-1-2i)^i = \exp(i \log(-1-2i))  
$$

(b)

To compute $\operatorname{Exp}(z)$, we can again use the formula $\operatorname{Exp}(z) = \sum_{n \geq 0} \frac{z^n}{n!}$.

$$  
\operatorname{Exp}(z) = \sum_{n \geq 0} \frac{(-1+ti)^n}{n!} = 1 + (-1+ti) + \frac{(-1+ti)^2}{2} + \frac{(-1+ti)^3}{3!} + \cdots  
$$

To compute $\log(z)$, we can use $\log(z) = \log|z| + i\arg(z)$, where $\arg(z)$ is the principal value of the argument of $z$.

$$  
\log(z) = \log |-1+ti| + i\arg(-1+ti) = \log \sqrt{1+t^2} + i\left(\frac{\pi+\arctan(t)}{2}\right)  
$$

To compute $z^i$, where $i = \sqrt{-1}$,

$$  
z^i = (-1+ti)^i = \exp(i \log(-1+ti))  
$$

(4)

(a)

We can represent $n^{-2+i}$ as $e^{(i\ln n - 2\ln n)}$.

Using Euler's formula, $e^{ix} = \cos x + i\sin x$, we have

$$  
e^{(i\ln n - 2\ln n)} = e^{-2\ln n}e^{i\ln n} = \frac{e^{i\ln n}}{n^2} = \frac{\cos(\ln n) + i\sin(\ln n)}{n^2}.  
$$

(b)

To show that the series $\sum_{n \geq 1} n^{-2+i}$ is absolutely convergent, we can use the comparison test.

Let's compare the series to the convergent series $\sum_{n\geq 1} \frac{1}{n^2}$.

Using the inequality $|\cos(\ln n)| \leq 1$ and $|\sin(\ln n)| \leq 1$, we have

$$  
\left| \frac{\cos(\ln n) + i\sin(\ln n)}{n^2} \right| \leq \frac{1}{n^2}.  
$$

Since the series $\sum_{n\geq 1} \frac{1}{n^2}$ converges, and we have a constant upper bound for the absolute value of each term in the series $\sum_{n \geq 1} n^{-2+i}$, we can conclude that the series $\sum_{n \geq 1} n^{-2+i}$ is absolutely convergent.

(c)

To determine whether the series $\sum_{n \geq 1} \frac{1}{n^z}$ is convergent or divergent for $z = x+iy$, where $x>1$, we can use the comparison test again.

Using the same inequality as in part (b), we have

$$  
\left| \frac{\cos(\ln n) + i\sin(\ln n)}{n^z} \right| \leq \frac{1}{n^x}.  
$$

Since $x > 1$, the series $\sum_{n\geq 1} \frac{1}{n^x}$ converges.

Therefore, by the comparison test, we can conclude that the series $\sum_{n \geq 1} \frac{1}{n^z}$ is convergent for $z = x+iy$, where $x>1$.

(5)

(a)

To determine the radius of convergence of the power series $\sum_{n \geq 0} F_n z^n$, we can use the ratio test.

The ratio of consecutive terms is given by

$$  
\left| \frac{F_{n+1}}{F_n} \right| = \left| \frac{\frac{1}{\sqrt{5}}\left(\phi^{n+1}-(-\phi)^{-n-1}\right)}{\frac{1}{\sqrt{5}}\left(\phi^n-(-\phi)^{-n}\right)} \right| = \left| \frac{\phi^{n+1}-(-\phi)^{-n-1}}{\phi^n-(-\phi)^{-n}} \right| = \left| \frac{\phi^{n+1}(-\phi)^n+(-\phi)^{n+1}\phi^{-n-1}}{\phi^n(-\phi)^n+(-\phi)^n\phi^{-n}} \right| = \left| \frac{\phi+(-1)\phi^{-n-1}}{1+(-1)\phi^{-2n}} \right|.  
$$

Taking the limit as $n$ approaches infinity, we have

$$  
\lim_{{n\to\infty}} \left| \frac{\phi+(-1)\phi^{-n-1}}{1+(-1)\phi^{-2n}} \right| = \left| \frac{\phi}{1} \right| = |\phi|,  
$$

where $|\phi|$ is the modulus of $\phi$.

Therefore, the radius of convergence of the power series is $|\phi|$.

(b)

For $z$ in the disk of convergence, the sum of the series $\sum_{n \geq 0} F_n z^n$ is given by

$$  
\sum_{n \geq 0} F_n z^n = F_0 + F_1 z + F_2 z^2 + F_3 z^3 + \cdots.  
$$

Since the Fibonacci sequence has the general term $F_n = \frac{1}{\sqrt{5}}\left(\phi^n-(-\phi)^{-n}\right)$, we can substitute this expression into the series.

$$  
\sum_{n \geq 0} F_n z^n = \sum_{n \geq 0} \frac{1}{\sqrt{5}}\left(\phi^n-(-\phi)^{-n}\right) z^n = \frac{1}{\sqrt{5}}\left(\sum_{n \geq 0} \phi^n z^n - \sum_{n\geq 0} (-\phi)^{-n} z^n\right).  
$$

Using the formula for the sum of a geometric series, we can simplify this expression as

$$  
\frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi z} - \frac{1}{1+\phi^{-1} z}\right).  
$$

Therefore, the sum of the series is $\frac{1}{\sqrt{5}}\left(\frac{1}{1-\phi z} - \frac{1}{1+\phi^{-1} z}\right)$.

$$
\begin{align*} \mathrm{\lim_{{{n}\to\infty}}{\left|{\frac{{{a}_{{{n}+{1}}}}}{{{a}_{{n}}}}}\right|}=\lim_{{{n}\to\infty}}{\left|{\frac{{{\frac{{{1}}}{{{2}}}}{\left(-{1}+{i}\sqrt{{{3}}}\right)}^{{{n}+{1}}}}}{{{n}+{1}}}}{\left\lbrace{\frac{{{1}}}{{{n}}}}{\left({\frac{{{1}}}{{{2}}}}{\left(-{1}+{i}\sqrt{{{3}}}\right)}\right)}^{{n}}\right\rbrace}\right|}=\lim_{{{n}\to\infty}}{\left|{\frac{{{\left(-{1}+{i}\sqrt{{{3}}}\right)}{n}}}{{{2}{\left({n}+{1}\right)}}}}\right|}=\infty} &\space\space\space\space\space \end{align*}$$