## Classic GS

## INPUT:
## A - A is an m x n matrix
##
## OUTPUT:
## QR decomposition

CGS <-function(A){
  Q <- matrix(0, nrow = nrow(A), ncol = ncol(A))
  R <- matrix(0, nrow = ncol(A), ncol = ncol(A))
  for(j in 1:ncol(A)){
    v <- A[,j, drop = F]
    if(j == 1){
      R[j,j] <- sqrt(sum(v^2))
      Q[,j] <- v / R[j,j]
      next
    }
    for(i in 1:(j - 1)){
      R[i,j] <- sum(Q[,i] * A[,j])
      v <- v - R[i,j] * Q[,i]
    }
    R[j,j] <- sqrt(sum(v^2))
    Q[,j] <- v / R[j,j]
  }
  
  QR <- list(Q = Q, R = R)
  return(QR)
}

## Testing
A = matrix(c(1,0,-1,2,3,4), nrow = 3)
L <- CGS(A)
t(L$Q) %*% L$Q
