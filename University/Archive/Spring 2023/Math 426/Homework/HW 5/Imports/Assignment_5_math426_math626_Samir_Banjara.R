library(pracma)

A = matrix(c(1, 0, -1, 2, 3, 4), nrow = 3)
m <- nrow(A)
n <- ncol(A)

## Classic Gram-Schmidt
CGS <- function(A) {
  # Initialize Q and R matrices with zeros
  Q <- matrix(0, m, n)
  R <- matrix(0, n, n)
  for (j in 1:n) {
    v <- A[,j, drop = F]
    if (j == 1) {
      R[j,j] <- sqrt(sum(v^2))
      Q[,j] <- v / R[j,j]
      next
    }
    for (i in 1:(j-1)) {
      R[i,j] <- sum(Q[,i] * A[,j])
      v <- v - R[i,j] * Q[,i]
    }
    R[j,j] <- sqrt(sum(v^2))
    Q[,j] <- v / R[j,j]
  }
  QR <- list(Q = Q, R = R)
  return(QR)
}

L <- TMGS(A)
# Check if Q and R are orthogonal and upper triangular, respectively
t(L$Q) %*% L$Q
# Multiply Q and R
Q <- L$Q
R <- L$R
Q %*% R
L$R
L$Q


## Modified Gram-Schmidt From Textbook
TMGS <- function(A) {
  # Initialize Q and R matrices with zeros
  Q <- matrix(0, m, n)
  R <- matrix(0, n, n)
  for (i in seq_len(n)) {
    v <- A[, i, drop = FALSE]
    R[i, i] <- norm(v)
    Q[, i] <- v / R[i, i]
    for (j in seq_len(n)[-seq_len(i)]) {
      R[i, j] <- t(Q[, i]) %*% A[, j, drop = FALSE]
      A[, j] <- A[, j] - R[i, j] * Q[, i]
    }
  }
  QR <- list(Q = Q, R = R)
  return(QR)
}

L <- TMGS(A)
# Check if Q and R are orthogonal and upper triangular, respectively
t(L$Q) %*% L$Q
# Multiply Q and R
Q <- L$Q
R <- L$R
Q %*% R
L$R
L$Q


## Modified Gram-Schmidt from Class
MGS <- function(A) {
  Q <- matrix(0, m, n)
  R <- matrix(0, n, n)
  V <- A
  for (i in 1:n) {
    R[i, i] <- sqrt(c(crossprod(V[, i])))
    Q[,i] <- V[, i] / R[i, i]
    if (i < n) {
      for (j in (i+1):n) {
        R[i, j] <- sum(t(Q[, i]) * V[, j])
        V[, j] <- V[, j] - R[i, j] * Q[, i]
      }
    }
  }
  return(list(Q = Q, R = R))
}

L <- MGS(A)
# Check if Q and R are orthogonal and upper triangular, respectively
t(L$Q) %*% L$Q
# Multiply Q and R
Q <- L$Q
R <- L$R
Q %*% R
L$R
L$Q


## House Holder Method HHM
# Define the Householder QR factorization function
householder_qr <- function(A) {
  # initialize Q and R
  m <- nrow(A)
  n <- ncol(A)
  Q <- diag(m)
  R <- A
  # iterate over the columns of A
  for (j in 1:n) {
    # jth column of the matrix
    col <- R[j:m, j]
    # reflection vector v
    v <- col
    v[1] <- v[1] + sign(v[1]) * norm(v, type = "2")
    v <- v / norm(v, type = "2")
    # compute beta
    beta <- 2 / (norm(v, type = "2")^2)
    # apply the reflector to the submatrix of R
    R[j:m, j:n] <- R[j:m, j:n] - tcrossprod(beta * v, crossprod(R[j:m, j:n], v))
    # apply the reflector to the submatrix of Q
    Q[, j:m] <- Q[, j:m] - tcrossprod(Q[, j:m] %*% v, beta * v)
  }
  # return Q and R
  return(list(Q = Q, R = R))
}

A = matrix(c(1, 0, -1, 2, 3, 4), nrow = 3)
m <- nrow(A)
n <- ncol(A)
# Run the Householder QR function
L <- householder_qr(A)
# Check if Q and R are orthogonal and upper triangular, respectively
t(L$Q) %*% L$Q
# Multiply Q and R
Q <- L$Q
R <- L$R
Q %*% R
L$R
L$Q


# Verification
# Classic
A.qr <- qr(A)
A.qr.out <- list('Q'=qr.Q(A.qr), 'R'=qr.R(A.qr))
# Modified
gramSchmidt(A)
# Householder
householder(A)
