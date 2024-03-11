---
tags:
  - "#statistics"
links:
  - "[[Regression]]"
  - "[[regularization]]"
  - "[[assessing the performance of linear regression]]"
  - "[[feature selection in linear regression]]"
  - "[[loss function]]"
---
basically just different ways to perform [[regularization]] 

```toc
```

# what is regularization?
![[regularization#^3f8aa2]] 

# Ridge Regression (L2 Regularization):

- An L2 penalty is the sum of the squares of the coefficients
- Shrinks the coefficients evenly but doesn't necessarily bring them exactly to zero.
- **Useful when there are many small/medium-sized effects.**

$$
\text{Ridge Loss} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} \beta_j^2
$$

where:
- $y_i$ is the actual value of the dependent variable for the \(i\)-th observation,
- $\hat{y}_i$ is the predicted value for the \(i\)-th observation,
- $n$ is the number of observations,
- $\beta_j$ are the coefficients of the model (excluding the intercept),
- $p$ is the number of predictors,
- $\lambda$ is the tuning parameter that controls the strength of the penalty.

# Lasso Regression (L1 Regularization):

- an L1 penalty is the sum of the absolute values of the coefficients.
- Can shrink some coefficients to zero, effectively performing feature selection.
	- see also [[feature selection in linear regression]]
- **Useful when there are a few variables with medium/large effects.**

$$
\text{Lasso Loss} = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 + \lambda \sum_{j=1}^{p} |\beta_j|
$$

where:
- $y_i$ is the actual value of the dependent variable for the \(i\)-th observation,
- $\hat{y}_i$ is the predicted value for the \(i\)-th observation,
- $n$ is the number of observations,
- $\beta_j$ are the coefficients of the model (excluding the intercept),
- $p$ is the number of predictors,
- $\lambda$ is the tuning parameter that controls the strength of the penalty.

# Key Differences:

- Ridge regression 
	- is good for cases with many small coefficients
- Lasso regression
	- can select out the most significant variables
	- more suitable for models with fewer predictors.
	- can reduce the number of variables by setting coefficients to zero, which Ridge cannot do.
s