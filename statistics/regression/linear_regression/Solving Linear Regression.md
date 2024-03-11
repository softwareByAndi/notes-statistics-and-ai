---
tags:
  - "#statistics"
links:
  - "[[Linear Regression]]"
---
# linear regression equation: 
![[Linear Regression#^e184e6]]
# equation to solve for optimal solution: 

## $$\min_{\theta} \sum_{i=1}^{n} \left( \theta^T X_i - Y_i \right)^2$$ 
- n data points
- $X_i$ and $\theta$ have dimension $m + 1$ 

## formula: 
note that the [[derivative]] of something [[quadratic]] is [[linear]].
### $$\hat{\theta} = \left( \mathbb{X}^T\mathbb{X} \right)^{-1} \mathbb{X}^T Y$$ 

- $Y$ is a vector
- $\mathbb{X}$ is a matrix of $[1|X]$  $$
\begin{pmatrix}
1 & X_1 \\
1 & X_2 \\
1 & X_3 \\
\vdots & \vdots \\
1 & X_n
\end{pmatrix}
$$

# justifications
1. the world is non-linear
	1. produce a best linear predictor that can be used for naive estimations
2. the world is linear
	1. learn the coefficients of the structural relation
	2. this is a stronger assumption that we know (or pretend to know) that the structure of the relation is linear
	3. see [[maximum likelihood justification for linear regression]]


# see also:

- [[linear regression with non-linear features]]
- [[latent variables]]
- [[assessing the performance of linear regression]] 
- [[calculating confidence bands for linear regression predictions]]