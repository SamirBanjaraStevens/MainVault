Samir Banjara
***
## Question 1
***
Find the volume of the solid that lies within the sphere $x^{2}+y^{2}+z^{2}=4$, above the $xy-$plane, and below the cone $z=\sqrt{ x^{2}+y^{2} }$
***

**Solution :**
***
Rewrite the sphere as $\mathcal{p}^{2}=4 \Rightarrow \mathcal{p}=2$
Thus, the sphere is centered at the origin with radius $2$.

Cone $z=\sqrt{ x^{2}+y^{2} }$ is the same as $\phi=\cfrac{\pi}{4}$ 

Define solid using spherical coordinates,
$$E=\{ (\rho, \theta, \phi) \mid o \leq \rho \leq 2, \quad 0\leq \theta \leq 2\pi \quad \cfrac{\pi}{4}\leq \phi \leq \cfrac{\pi}{2} \}$$
Calculate the volume of the solid as the integral,
$$
\begin{align}
\iiint_{E} \ dV &= \int _{\frac{\pi}{4}}^{\frac{\pi}{2}} \int _{0}^{2\pi} \int _{0}^{2} \rho^{2}\sin \phi \, d\rho  \, d\theta  \, d\phi\\
&=  \int _{\frac{\pi}{4}}^{\frac{\pi}{2}} \sin \phi \ d\phi\int _{0}^{2\pi} d\theta\int _{0}^{2} \rho^{2} \ d\rho\\
&= [-\cos \phi]\mid_{\frac{\pi}{4}}^{\frac{\pi}{2}}\cdot [\theta]_{0}^{2\pi} \cdot \left[ \frac{1}{3}\rho^{3} \right]_{0}^{2}\\
&=\left[ \cfrac{1}{\sqrt{ 2 }} \right] \cdot \left[ 2\pi \right] \cdot \left[ \cfrac{8}{3} \right] \\
&= \cfrac{8\sqrt{ 2 }}{3}\pi
\end{align}
$$


## Question 2
***
Evaluate the integral $\iint_{R}(x+y)e^{x^{2}-y^{2}}$
***

**Solution :**
***

$u=x+y$ and $v=x-y$
thus, $$\begin{align}
x&=\cfrac{u+v}{2}\\
y&=\cfrac{u-v}{2}
\end{align}$$
$R$ is defined $0\leq u\leq 3$ and $0\leq v\leq 2$

The Jacobian is, 
$$\cfrac{\partial(x, y)}{\partial(u, v)}=\begin{bmatrix}
\frac{1}{2}  & \frac{1}{2} \\
\frac{1}{2}  & \frac{-1}{2}
\end{bmatrix}=\cfrac{-1}{2}$$
Thus, the integral is 
$$
\begin{align}
\iint_{R}(x+y)e^{x^{2}-y^{2}} dA &= \int _{0}^{3} \int _{0}^{2} ue^{uv}\mid -\frac{1}{2} \mid \, \, dv \, du\\
&=\left. \frac{1}{2}\int _{0}^{3} e^{uv}  \right]_{0}^{2}  \, du \\
&=\frac{1}{2}\int _{0}^{3} e^{2u}-1 \, du\\
&=\frac{1}{2}\cdot \left[ \frac{1}{2}e^{2u}-u \right]_{0}^{3}\\
&=\frac{1}{2}\cdot \left[ \frac{1}{2}e^{6}-3- \frac{1}{2} + 0 \right] \\
&=\frac{1}{4}(e^{6-7})
\end{align}
$$
