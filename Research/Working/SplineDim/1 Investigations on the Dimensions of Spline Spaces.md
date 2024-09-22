# Abstract

A computational method to obtain explicit formulas for the dimension of spline spaces over simplicial partitions. The method is applied to conjecture the dimension of several $n$-simplex partitions.

## Introduction

A spline is a smooth piecewise polynomial function.
The splines of these pages are defined on [[triangulations]](decompositions) of a domain $\Omega \subseteq \mathbb{R}^n$. Where $n$ will denote the dimension of the polyhedral domain.  

Let 
$$\tag{1} \mathcal{T}=\{ \sigma_{i} : i=1, 2, \dots, T \}$$
be a finite set of non degenerate simplices in $\mathbb{R}^n$ and let 
$$\tag{2}\Omega=\bigcup_{i=1}^{T} \sigma_{i}.$$

Let 
$$\tag{3}\mathcal{X} = \{ x_{i}\in\Omega, \, i =1, 2, \dots, N \}$$
be the set of all vertices of simplicies in $\mathcal{T}$. Then $\mathcal{T}$ is a triangulation of $\Omega$ provided that,
1. The interiors of the simplices in $\mathcal{T}$ are pairwise disjoint.
2. Each (k-1)-dimensional face of a simplex in $\mathcal{T}$ is either on the boundary of $\Omega$ or else is a common face of precisely two simplicies in $\mathcal{T}$
3. Each simplex contains no points of $\mathcal{X}$ other than its vertices.
Some of ours bounds require that the triangulation have special properties. These are formalized in the following two definitions:

### Definition 2.

A triangulation of $\mathcal{T}$ is regular if $\Omega$ is homeomorphic to the unit cube.
### Definition 3

A regular triangulation $\mathcal{T}$ is said to be shellable if it consists of a single simplex or a smaller shellable triangulation $\hat{\mathcal{T}}$ can be obtained by removing one simplex from $\mathcal{T}$ 
### Definition 4

Let $\mathcal{P}^n_{d}$ denoted the $\left(\begin{array}{}{n+d}\\ d\end{array} \right)$-dimensional space of polynomials in $n$ variables of degree $d$. Then the space $\mathcal{S}^r_{d}(\mathcal{T})$ is the set of all functions that can be represented as a polynomial in $\mathcal{P}^n_{d}$ on each simplex in $\mathcal{T}$, and that are r-times differentiable across each interior facet of $\mathcal{T}$.

By an abuse of notation we identify $\Delta$ with its embedding in $\mathbb{R}^n$ and $\Delta_{n}$ to now denote the simplicial partition $\mathcal{T}$


Our goal is to determine the dimension of this space for some particular partitions $\Delta_{n}$ of a polyhedral domain $\Omega\subseteq \mathbb{R}^n$, so that if two simplicies in $\Delta_{n}$ intersect, then their intersection is a facet of $\Delta_{n}$. For example $\Delta_{2}$ is triangulation of a polygon $\Omega\subseteq \mathbb{R}^2$, $\Delta_{3}$ is a tetrahedral partition of a polyhedron $\Omega\subseteq \mathbb{R}^3$

Thus let
$$
\mathcal{S}^r_{d}=(\Delta_{n})=
\{ s \in \mathcal{C} : s\mid_{T} \in \mathcal{P}^n_{d}\ \text{ for each simplex }\,T\in\Delta_{n}\}
$$
denote the space of $\cal{C}^r$ splines of degree $\leq d$ in $n$ variables over $\Delta_{n}$ our goal is to determine the dimension of this space for some particular partitions $\Delta_{n}$. 

## Bivariate case $n=2$

In this case, it is known, [M.J. Lai and Schumaker, Spline functions on trigulations, Cambridge University Press, Cambridge, 2007] (p.240) that if $\Delta_{2}$ is shellable (regular with no holes )


# The computational method

## 2.1 via Hilbert Polynomials

## 2.2 Via Hilbert series in Bernstien Bezier form

# Applications to specific partitions

## Trivariate splines of a tetrahedron

### Alfeld-split

### Clough-Tocher split

### Worsey-Farin split
## Multivariate splines of a simplex

### Alfeld-split

### Clough-Tocher split

### Worsey-Farin split



# Triangu