The **Frobenius inner product** is a binary operation that takes two *[[matricies]]* and return a *[[Scalars]]*. 
	Oftern denoted $\left< A, B \right>_{F}$

The operation is a component-wise *[[inner product]]* of two matricies
	as though they are vectors
		and satsfiy the aximos for an inner product.

The two matricies must have the same dimension
	same number of rows and columns
		but are **not** restriced to be *[[Square matricies]]*

Frobenius inner product is defined as,
$$\left< A, B \right> _{F} = \sum_{ij} \overline{A_{ij}}B_{ij}=\mathrm{Tr}\left( \overline{A^{T}B} \right) = \mathrm{Tr}\left( A^{\dagger}B \right) $$
	where the overline denotes the *[[complex conjugate]]*
		and ${\dagger}$ denotes the *[[Hermetian conjugate]]*

The inner product **induces** the *[[Frobenius norm]]* 
	$\|A\|_{F}=\sqrt{ \mathrm{Tr}(A^{*}A) }=\sqrt{ \mathrm{Tr}(A A^{*}) }=\sqrt{ \left< A, A \right>_{F} }$ 