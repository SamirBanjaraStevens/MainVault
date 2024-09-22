# %%
def false_position(f, a, b, TOL=1e-6, max_iter=1000):
    if f(a) * f(b) > 0:
        raise ValueError("The function must have different signs at a and b.")
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        if f(c) == 0 or abs(f(c)) < TOL:
            break
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c    

# %%
# Example usage with the given function and interval:
# Define the function : f(x) = 230x^4 + 18x^3 + 9x^2 - 221x - 9
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9
    # Find the root in the interval [-1, 0]
root = false_position(f, -1, 0)

 # Find the root in the interval [1, 0]
root2 = false_position(f, 0, 1)

# Print the results 
print(f"Root: {root}")
print(f"f({root}) = {f(root)}")
print(f"Root2: {root2}")
print(f"f({root2}) = {f(root2)}")

# %% [markdown]
# ## Lets try Newton's Method now

# %%
def newton_method(p0, e, max_it, f, f_prime):
    for _ in range(max_it):
        p1 = p0 - f(p0) / f_prime(p0)
        if abs(p1 - p0) < e:
            return p1
        p0 = p1
    else:
        print('Warning. Max Iter Reached!')
        return p0


# %%
def f(x):
    return 230*x**4 + 18*x**3 + 9*x**2 - 221*x - 9

def f_prime(x):
    return 920*x**3 + 54*x**2 + 18*x - 221

# Intervals
intervals = [(-1, 0), (0, 1)]
e = 1e-6
max_it = 50

roots = []

for a, b in intervals:
    p0 = (a + b) / 2  # Mid-point
    root = newton_method(p0, e, max_it, f, f_prime)
    roots.append(root)

print("Roots:", roots)


# %% [markdown]
# Lets try to experiment with Complex Numbers.
# 
# There is an issue with the use of absolute value of Real Numbers 
# $\mathbb{R}$. 
# We need to use the modulus of complex numbers defined as follows, 
# Let $z$ be a complex number represented in the standard form as  $z = a+bi$
# Where $a$ and $b$ are $\mathbb{R}$ real numbers, and $i$ is the imaginary unit such that $i^2 = -1$
# 
# The modulus (or magnitude) of $z$,
# is the negative square root of the sum of squares of its real and imaginary parts, denoted, $|z| = \sqrt{a^2+b^2}$
# 
# With the following properties:
# 1. $|z| \geq 0$ for all complex numbers $z$, and $|z| = 0$ if and only if $z = 0$.
# 2. $|z_1z_2| = |z_1| \, |z_2|$ for all complex number $z_1$ and $z_2$.
# 3. $|\hat{z}| = |z|$, where $\hat{z}$ is the complex conjugate of $z$.
# 4. $|z_1+z_2| \leq |z_1|+|z_2|$ (Triangle Inequality) for all complex numbers $z_1$ and $z_2$
# 
# And the argument is defined as follows: 
# 
# The argument of $z$, denoted by $\mathrm{arg}(z)$ or $\theta$, is the angle (in radians) that the line segment joining the origin and the point representing $z$ in the complex plane makes with the positive real axis. The angle is measured in the counter clockwise direction.
# 
# The *principal value* of the argument is given by:
# $\mathrm{arg}(z) = \arctan(\cfrac{b}{a})$
# 
# The quadrant in which $z$ lies must be taken into account to determine the correct angle
# 
# 1. if $a > 0$ and $b \geq 0$ then, $\mathrm{arg}(z) = \arctan(\cfrac{b}{a})$
# 
# 2. if $a<0$,then $\mathrm{arg}(z) = \arctan\left(\cfrac{b}{a}\right) + \pi$
# 3. if $a < 0$
# 
# 4. if $a = 0$ and $b\neq 0$ then $\mathrm{arg}(z) = \frac{\pi}{2}$ for $b >0$ and $\mathrm{arg}(z)=-\frac{\pi}{2}$ for $b < 0$        
# 
# 
# We need to modify the code, to reflect the solutions shown below.1. Replace all the absolute value computations with the modulus computations for complex numbers. we can still use `abs()`
# 
# 2. Instead of checking if `f(a) * f(b) > 0` we can check if the argument of the two complex number is different by more than the  `TOL`. This ensure they lie in different half-planes.
#    
# 

# %%
def false_position_complex(f, a, b, TOL=1e-6, max_iter=1000):
    # Check if f(a) and f(b) lie in different half-planes
    if (f(a) * f(b).conjugate()).real >= 0:
        raise ValueError("The function must have different signs at a and b.")
    
    for i in range(max_iter):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(c) == 0 or abs(f(c)) < TOL:
            break 

        # Check if f(a) and f(c) lie in different half-planes
        if (f(a) * f(c).conjugate()).real < 0:
            b = c
        else:
            a = c
            
    return c

# %%
# Example usage with a complex function and interval:
# Define the function: f(z) = z^2 + 1
def f(z):
    return z**2 + 1

# Find the root of the function in the interval [1-1j, 1+1j]
root = false_position_complex(f, 1-1j, 1+1j)

# Print the results
# print(f"Root: {root}")
print(f"f({root}) = {f(root)}")


# %% [markdown]
# ## Question 2
# 
# Let $f(x) \in C \, [a,b]$ and let $p \in  [a,b]$
# 
# 1. Suppose that $f(p)\neq 0$
# 	show that there is a $\delta > 0$ with $f(x) \neq 0$ 
# 		for all $x \in[p-\delta, p + \delta]$ 
# 
# 2. Suppose that $f(p) = 0$ and $k>0$ is given,
# 	Show that there is a $\delta>0$ with $f(x)\leq k$
# 		for all $x \in[p-\delta, p + \delta]$ 
# 
# ***
# #### Solution:
# 
# 1. 
# Given that $f(x)$ is continuous on $[a, b]$ and $f(p) \neq 0$, by the property of continuity functions, $f(x)$ is continuous at $x = p$. This means that for any $\epsilon >0$, there exists a $\delta > 0$ such that if $0<\left|\, x - p \,\right| < \delta$ then $\left|\, f(x) - f(p) \,\right| < \epsilon$ 
# 
# Now choosing $\epsilon = \cfrac{\left|\, f(p) \,\right|}{2}$ 
# 	This ensure that $f(x)$ does not change sign in the interval $(p-\delta, p + \delta)$, because the difference between $f(x)$ and $f(p)$ is less than half the magnitude of $f(p)$.
# 
# Given $\left|\, f(x) - f(p) \,\right| < \cfrac{\left|\, f(p) \,\right|}{2}$
# this implies, $\left|\, f(x) \,\right|> \cfrac{\left|\, f(p) \,\right|}{2}$ 
# since, $\cfrac{\left|\, f(p) \,\right|}{2} > 0$
# 	Thus, it follows that there exists a $\delta >0$ such that $f(x)\neq 0$ for all $x \in[p-\delta, p+\delta]$
# ***
# 2.
# Given that $f(x)$ is continuous on $[a, b]$ and $f(p) = 0$, by the property of continuity functions, $f(x)$ is continuous at $x = p$. This means that for any $\epsilon >0$, there exists a $\delta > 0$ such that if $0<\left|\, x - p \,\right| < \delta$ then $\left|\, f(x) - f(p) \,\right| < \epsilon$ 
# 
# Choose $\epsilon = k$
# 	Ensure that the difference between $f(x)$ and $f(p)$ is less than $k$
# Given $\left|\, f(x) - f(p) \,\right|< k$ and $f(p) = 0$,
# the inequality becomes
# 	$|f(x)| < k$, which implies $f(x) \leq k$
# Thus, there exists a $\delta > 0$ such that $f(x)\leq k$ for all $x \in[p-\delta, p+\delta]$
# ***

