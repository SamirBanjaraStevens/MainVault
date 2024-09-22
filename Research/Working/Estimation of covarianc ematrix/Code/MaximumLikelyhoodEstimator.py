{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How to estimate the maximum likelihood estimator, also known as the empirical covariance matrix.  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given an observed $p$-dimensional Gaussian multivariate samples $X_1, X_2, \\dots, X_n$ i.i.d. with mean 0, covariance matrix $\\Sigma$. \n",
    "The empirical covariance matrix is defined as follows, \n",
    "$$\\Sigma_{p} = \\frac{1}{n}\\sum_{i=1}^{n} \\ (X_{i}-\\mu_{X})(X_{i}-\\mu_{X})^T$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Where, $\\mu_{X} = \\cfrac{\\sum_{i=1}^nX_{i}}{n}$ is the sample mean vector, $(X_{i}-\\mu_{X})$ is the deviation of each observation from the mean, and $(X_{i}-\\mu_{X})(X_{i}-\\mu_{X})^T$ is the outter product of this deviation vector with itself."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's generate a random matrix where the mean is 0. The size of the matrix is also randomly generated with the number of rows being generated is between 1-10, and the number of columns being generated is between 2-10."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Random Matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[ 1.76405235,  0.40015721,  0.97873798,  2.2408932 ,  1.86755799,\n",
       "        -0.97727788,  0.95008842],\n",
       "       [-0.15135721, -0.10321885,  0.4105985 ,  0.14404357,  1.45427351,\n",
       "         0.76103773,  0.12167502],\n",
       "       [ 0.44386323,  0.33367433,  1.49407907, -0.20515826,  0.3130677 ,\n",
       "        -0.85409574, -2.55298982],\n",
       "       [ 0.6536186 ,  0.8644362 , -0.74216502,  2.26975462, -1.45436567,\n",
       "         0.04575852, -0.18718385],\n",
       "       [ 1.53277921,  1.46935877,  0.15494743,  0.37816252, -0.88778575,\n",
       "        -1.98079647, -0.34791215]])"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import random\n",
    "\n",
    "# Generate random dimensions for the matrix\n",
    "rows = random.randint(1, 10)  # For example, random number of rows between 1 and 10\n",
    "cols = random.randint(2, 10)  # Random number of columns between 1 and 10\n",
    "\n",
    "np.random.seed(0) # Set seed to 0 for reproducibility\n",
    "\n",
    "# Create a random matrix of the specified size\n",
    "random_matrix = np.random.randn(rows, cols)\n",
    "\n",
    "print(\"Random Matrix\")\n",
    "random_matrix"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now to calculate the sample mean vector."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Estimate:\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([ 0.84859124,  0.59288153,  0.45923959,  0.96553913,  0.25854956,\n",
       "       -0.60107477, -0.40326448])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_est = np.mean(random_matrix, axis=0)\n",
    "print(\"Mean Estimate:\")\n",
    "mean_est"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now to calculate the sample covariance matrix $\\Sigma_S$ using the numpy algorithm."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sample Covariance Matrix:\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[ 0.62697455,  0.29281769,  0.03285966,  0.45166048, -0.04876998,\n",
       "        -0.66853518,  0.39495629],\n",
       "       [ 0.29281769,  0.35771027, -0.23186273,  0.1172121 , -0.65661435,\n",
       "        -0.46093069,  0.00954561],\n",
       "       [ 0.03285966, -0.23186273,  0.71977601, -0.47428437,  0.81021465,\n",
       "        -0.22019941, -0.45588329],\n",
       "       [ 0.45166048,  0.1172121 , -0.47428437,  1.42947617, -0.13868269,\n",
       "         0.08786893,  1.01518739],\n",
       "       [-0.04876998, -0.65661435,  0.81021465, -0.13868269,  2.06744984,\n",
       "         0.37081386,  0.56361495],\n",
       "       [-0.66853518, -0.46093069, -0.22019941,  0.08786893,  0.37081386,\n",
       "         1.09573103,  0.2033035 ],\n",
       "       [ 0.39495629,  0.00954561, -0.45588329,  1.01518739,  0.56361495,\n",
       "         0.2033035 ,  1.69454982]])"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the sample covariance matrix\n",
    "sample_cov = np.cov(random_matrix, rowvar=False)\n",
    "print(\"Sample Covariance Matrix:\")\n",
    "sample_cov"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally we can now approximate the covariance matrix by calculating the empirical covariance matrix $\\Sigma_p$."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Covariance Estimate: The emperical covariance matrix\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([[ 0.50157964,  0.23425415,  0.02628773,  0.36132838, -0.03901598,\n",
       "        -0.53482814,  0.31596503],\n",
       "       [ 0.23425415,  0.28616821, -0.18549019,  0.09376968, -0.52529148,\n",
       "        -0.36874455,  0.00763649],\n",
       "       [ 0.02628773, -0.18549019,  0.57582081, -0.37942749,  0.64817172,\n",
       "        -0.17615953, -0.36470663],\n",
       "       [ 0.36132838,  0.09376968, -0.37942749,  1.14358094, -0.11094615,\n",
       "         0.07029514,  0.81214991],\n",
       "       [-0.03901598, -0.52529148,  0.64817172, -0.11094615,  1.65395987,\n",
       "         0.29665109,  0.45089196],\n",
       "       [-0.53482814, -0.36874455, -0.17615953,  0.07029514,  0.29665109,\n",
       "         0.87658482,  0.1626428 ],\n",
       "       [ 0.31596503,  0.00763649, -0.36470663,  0.81214991,  0.45089196,\n",
       "         0.1626428 ,  1.35563986]])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate Empirical Covariance Matrix\n",
    "cov_est = np.dot((random_matrix - mean_est).T, (random_matrix - mean_est)) / (rows)\n",
    "print(\"Covariance Estimate: The emperical covariance matrix\")\n",
    "cov_est"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0163487151223662"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "MSE = np.mean((sample_cov - cov_est) ** 2)\n",
    "MSE"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As we can see the mean squared error between the sample covariance and the maximum likelihood estimator (empirical covariance matrix) is $0.0163$. The sample covariance matrix is not a consistent estimator of the covariance matrix $\\Sigma$ when $p\\gg n$, and thus structural assumptions are required in order to estimate $\\Sigma$ consistently. We considered the case $X_{i} : N(0,\\Sigma)$. The empirical covariance matrix $\\Sigma_{p}$ is a consistent estimator. It is simple to construct, unbiased, and intuitive. However, when $n<p$ the rank is at most $n$ thus $\\Sigma_{p}$ is not invertible, in the sense that $p/n\\to c\\in(0,\\infty)$. Additionally, when $n\\geq p$, $\\Sigma_{p}$ has significant sampling error, in terms of $||\\cdot||_{2}$ (forbinus norm), thus $\\Sigma_{p}$ is not consistent and so its inverse is a poor estimator for $\\Omega$. While $\\Sigma_{p}$ is unbiased for $\\Sigma$, $\\Sigma_{p}^{-1}$ is highly biased for $\\Sigma^{-1}$ if $p$ is close to $n$. For $\\Sigma=I_{p}$, the empirical spectral density -distribution of the eigenvalues- converges to large distribution. If $p/n\\to c(0,1)$ $\\Sigma_{p}$ is supported on $((1-\\sqrt{ c }^{2}), (1+{\\sqrt{ c }^{2}}))$. Additionally, If $\\frac{p}{n}\\to c >0$ the smallest and largest eigenvalues of $\\Sigma_p$ will converge to $\\mathrm{max}(0, (1-\\sqrt{ c }^{2}))$ and $\\mathrm{max}(0,(1+\\sqrt{ c }^{2}))$ "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In general, structural assumptions of $\\Sigma$ or $\\Omega$ are needed for consistent estimation. \n",
    "\n",
    "In the following sections, we will examine methods with structural assumptions that estimate the covariance matrices that avoid undesirable properties of the sample covariance matrix. And their application in financial setting. \n",
    "\n",
    "Estimators include regularization techniques like the maximum likelihood estimator examined above, modified Cholesky decomposition with regularization.\n",
    "\n",
    "Another branch of estimator we will be investigating assume $\\Sigma$ does not have diverging eigenvalues as $n,p \\to \\infty$. Focus is not on the estimators conforming to any structures on $\\Sigma$, but shrinking the eigenvalues of $\\Sigma_{X}$. These estimators include the shrinkage method, Bayesian & empirical Bayes estimators, and the method based on random matrix theory. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First lets examine the shrinkage method."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
