Samir Banjara
02/22/23
5:47pm

#### **Question: **

Find the distance between the plane passing through the points
$$
P_1(1,\, 2,\, 3), \ P_2(2,\, 3,\, 5), P_3(3,\, 5,\, 7)
$$
 And
$$
Q(2,\, -2,\, 2)
$$

 Explain how you found the answer using vector projections. Please draw a diagram to help with your solution.

#### **Solution :**

Distance $D$ from $Q$ to the plane is equal to the absolute value of the scalar projection of $b$ onto the normal vector $n = \langle a,b, c\rangle$ 

Thus, 
$$
\begin{aligned}
D &= |comp_{n}b|\\ 
&= \frac{n\cdot b}{n}\\
&= \frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}
\end{aligned}
$$

First let's find the equation of the plane:
$$
\begin{aligned}
a &= \vec{P_1P_2}\\ 
&= (2-1)i+(3-2)j+(5-3)k\\
&=1i+1j+2k\\
&=\langle 1, 1, 2\rangle
\end{aligned}
$$
$$
\begin{aligned}
b &= \vec{P_1P_3}\\ 
&= (3-1)i+(5-2)j+(7-3)k\\
&=2i+3j+4k\\
&= \langle 2, 3, 4 \rangle
\end{aligned}
$$

Since both $a$ and $b$ lie on the same plane, their cross product $a\times b$ is orthogonal to the plane, and can be taken as normal vector. Thus,

$$
\begin{aligned}
n = a\times b &= 
\begin{bmatrix}
i & j & k\\
1 & 1 & 2\\
2 & 3 & 4
\end{bmatrix}\\
&= (1\cdot 4)-(2\cdot 3)i - (1\cdot 4)-(2\cdot 2)j + (1\cdot 3)-(1\cdot 2)k\\
&=-2i-0j+1k
\end{aligned}
$$

With point $P_1(1,2, 3)$ and normal vector $n$ the equation of the plane is,
$$-2x+0y+1z-1=0$$

Then the distance from point $Q(2, -2, 2)$ to the plane is, 

$$
\frac{|-2(2)+0(-2)+1(2)-1|}{\sqrt{(-2)^2+(0)^2+(1)^2}} = \frac{3}{\sqrt{5}}
$$

![[Pasted image 20230222174334.png]]

The white line that goes through point $Q$ (pink), the shortest possible path, is the line perpendicular to the plane (green).
- Therefore, the distance $D$ from point $Q$ to the plane is along a line parallel to the normal vector. 
