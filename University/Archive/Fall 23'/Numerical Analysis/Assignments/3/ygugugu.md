\documentclass[10pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage[version=4]{mhchem}
\usepackage{stmaryrd}
\usepackage{bbold}

\begin{document}
UMass Boston

Due: Mon 10/16 at 2:30pm, in class

Department of Mathematics

Math 358 - Complex Analysis

Fall 2023

Homework \#03 v.2

(1) Consider the power series

$$
\sum_{n \geqslant 1} \frac{1}{n} z^{n}=z+\frac{z^{2}}{2}+\frac{z^{3}}{3}+\frac{z^{4}}{4}+\cdots
$$

(a) Does the series converge for $z=-i$ ? (Note: changed from $z=i$ in first version)

(b) Does the series converge for $z=\frac{1}{2}(-1+i \sqrt{3})$ ?

(2) We are given a power series $\sum_{n \geqslant 0} a_{n}(z-2)^{n}$ that is convergent for $z=-1$. What can we conclude about the series

$$
\sum_{n \geqslant 2023} a_{n}(-2-2 i)^{n} ?
$$

Is it absolutely convergent, is it divergent, or could be either, depending on the series?

(3) (a) Let $z=-1-2 i$. Compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$.

(b) Let $z=-1+t i$, with $t \in \mathbb{R}$. Compute $\operatorname{Exp}(z), \log (z), z^{i}$, and $i^{z}$ as functions of $t$.

(4) (a) Let $n>0$ be a positive real number. Compute $n^{-2+i}$.

(b) Show that the series

$$
\sum_{n \geqslant 1} n^{-2+i}
$$

is absolutely convergent.

(c) Let $z=x+i y \in \mathbb{C}$ such that $x>1$. Determine whether the series

$$
\sum_{n \geqslant 1} \frac{1}{n^{z}}
$$

is convergent or divergent.

(5) The Fibonacci sequence is given by $F_{0}=0, F_{1}=1$, and $F_{n}=F_{n-1}+F_{n-2}$ for all $n \geqslant 2$, and the general term is

$$
F_{n}=\frac{1}{\sqrt{5}}\left(\phi^{n}-(-\phi)^{-n}\right)
$$

where $\phi=\frac{1+\sqrt{5}}{2}$. Consider the power series

$$
\sum_{n \geqslant 0} F_{n} z^{n}=F_{0}+F_{1} z+F_{2} z^{2}+F_{3} z^{3}+\cdots=0+z+z^{2}+2 z^{3}+3 z^{4}+5 z^{5}+8 z^{6}+\cdots
$$

(a) Determine the radius of convergence of the power series.

(b) For $z$ in the disk of convergence, determine the sum of the series.


\end{document}

Problem 1: This problem is asking about the convergence of a power series. To solve it, you would need to use the ratio test or the root test. These tests involve taking the limit as n approaches infinity of the absolute value of the ratio of the (n+1)th term to the nth term (ratio test) or the nth root of the absolute value of the nth term (root test). If this limit is less than 1, the series converges; if it's greater than 1, it diverges; if it's equal to 1, the test is inconclusive.

Problem 2: This problem is asking about the convergence of a power series at a specific point. To solve it, you would need to use the concept of the radius of convergence, which is the distance from the center of the series to the point where the series converges. If the given point is within this radius, the series converges; if it's outside, it diverges.

Problem 3: This problem is asking for the computation of complex exponentials and logarithms. To solve it, you would need to use Euler's formula, which states that e^(ix) = cos(x) + isin(x), and the definition of the complex logarithm, which is log(z) = ln|z| + iarg(z), where arg(z) is the argument of z.

Problem 4: This problem is asking about the convergence of a series involving complex powers. To solve it, you would need to use the concept of absolute convergence, which states that a series converges absolutely if the series of the absolute values of its terms converges. You would also need to use the p-series test, which states that the series 1/n^p converges if p > 1 and diverges if p <= 1.

Problem 5: This problem is asking about the convergence of a power series involving Fibonacci numbers. To solve it, you would need to use the Binet's formula for Fibonacci numbers, which involves the golden ratio, and the concept of the radius of convergence. You would also need to use the formula for the sum of a geometric series, which is a/(1-r) if |r| < 1.
Problem 1: If the ratio or root test is inconclusive (i.e., the limit equals 1), you could try using the comparison test. This involves comparing the given series to a known convergent or divergent series. If the given series is less than a convergent series, it also converges; if it's greater than a divergent series, it also diverges.

Problem 2: If the given point is on the boundary of the radius of convergence, the series could either converge or diverge. In this case, you would need to use other tests, such as the ratio test, root test, or comparison test, to determine the convergence at this point.

Problem 3: If Euler's formula and the definition of the complex logarithm do not give a clear answer, you could try using the properties of exponentials and logarithms, such as the power rule, product rule, and quotient rule, to simplify the expressions.

Problem 4: If the p-series test is inconclusive (i.e., p equals 1), you could try using the integral test. This involves comparing the series to an improper integral. If the integral converges, the series also converges; if the integral diverges, the series also diverges.

Problem 5: If the formula for the sum of a geometric series does not give a clear answer, you could try using the method of generating functions. This involves finding a function whose power series expansion gives the terms of the series. The sum of the series can then be found by evaluating the function at a specific point.
Problem 1: 1. Limit Comparison Test: If the ratio test is inconclusive, you can compare the limit of the nth term of your series to the nth term of a known series. 2. Alternating Series Test: If the series is alternating, you can check if the absolute value of the terms is decreasing and the limit of the terms is zero.

Problem 2: 1. Direct Comparison Test: If the series is similar to a known series, you can directly compare the terms. 2. Leibniz’s Rule: If the series is alternating, you can use Leibniz’s rule which states that an alternating series converges if the absolute value of the terms is decreasing and the limit of the terms is zero.

Problem 3: 1. Change of Base Formula: If the base of the logarithm or exponential is not e, you can use the change of base formula to convert it to a natural logarithm or exponential. 2. Properties of Logarithms and Exponentials: If the expressions are complex, you can use properties of logarithms and exponentials to simplify them.

Problem 4: 1. Cauchy's Root Test: If the p-series test is inconclusive, you can use Cauchy's root test which involves taking the nth root of the absolute value of the nth term. 2. Cauchy's Condensation Test: This test involves creating a new series where the nth term is 2^n times the 2^n-th term of the original series, and then checking if this new series converges.

Problem 5: 1. Ratio Test for Series: If the series is not geometric, you can use the ratio test to check for convergence. 2. Use of Recurrence Relations: Since the Fibonacci sequence is defined by a recurrence relation, you can use this relation to find a formula for the nth term and then use this formula to check for convergence.Provide detailed and comprehensive steps, work, definitions, theorems, arithemetic used to solve the problem. Ensure that all necessary work is clearly shown, and include any subtle nuances or intricacies that might not be immediately obvious in your initial solution
