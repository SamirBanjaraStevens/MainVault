library(scatterplot3d)
## Computing SVD of a general m x n matrix
A = matrix(c(1,1,3,2,4,1,3,6,7,3,1,5), ncol = 3, byrow = T) ## A 4 x 3 matrix
print(A)

S = svd(A, nu = 4, nv = 3) ## computing Full SVD
U = S$u; print(U) ## a 4 x 4 matrix
V = S$v; print(V) ## a 3 x 3 matrix
D = diag(c(S$d, 0)); print(D) ## a 3 x 3 matrix. 

S = svd(A) ## computing Reduced SVD

## Looking at the decomposition
U = S$u; print(U) ## a 4 x 3 matrix
V = S$v; print(V) ## a 3 x 3 matrix
D = diag(S$d); print(D) ## a 3 x 3 matrix. 
##Note: S$d are the singular values and are not returned as a matrix. Hence we use the diag to turn in into a matrix


## Checking the decomposition A = U D V^T

print(A - U %*% D %*% t(V)) ## equal up to machine precision

## rank of A are the nonzero diagonal elements

rank.A = sum(S$d != 0); print(rank.A) ## A has full column rank

## Hence columns of U are an o.n basis for the range of A and the NULL(A) = {0}

## Testing the Geometry of SVD
A = matrix(c(1,2,1,-1), ncol = 2, byrow = T); print(A)
S = svd(A)
U = S$u; print(U) 
V = S$v; print(V) 
D = diag(S$d); print(D)  

## Apply A to the unit circle
theta = seq(from = 0, to = 2*pi, by = 0.01)
x = cos(theta)
y = sin(theta)

## turn x and y into a matrix with columns as coordinates on the circle and rows as different point
C = matrix(cbind(x,y), nrow = 2, byrow = T)

## Now apply A
A.tilde = A %*% C

## plotint the results
## asp = aspect ration is set to 1 so to prevent distortion
par(mfrow = c(1,2))
plot(t(C), type = 'l', asp = 1, xlab = 'x', ylab = 'y', main = 'Unit Circle') 
arrows(0, 0, V[1,1], V[2,1], length = 0.1, col = 'red')
arrows(0, 0, V[1,2], V[2,2], length = 0.1, col = 'red')

plot(t(A.tilde), type = 'l', asp = 1, xlab = 'x', ylab = 'y', main = 'Action of A')
arrows(0, 0, D[1,1]*U[1,1], D[1,1]*U[2,1], length = 0.1, col = 'blue')
arrows(0, 0, D[2,2]*U[1,2], D[2,2]*U[2,2], length = 0.1, col = 'blue')

