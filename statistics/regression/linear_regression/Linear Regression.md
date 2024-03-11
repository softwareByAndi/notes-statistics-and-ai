---
tags:
  - "#core-algorithm"
  - "#statistics"
  - "#artificial-intelligence"
links:
  - "[[explanatory statistics]]"
  - "[[Regression]]"
  - "[[Naive AI Algorithms]]"
key relations:
  - "[[assessing the performance of linear regression]]"
  - "[[Solving Linear Regression]]"
  - "[[Simple Linear Regression]]"
---
pretty straight forward... adjust [[coefficients]] so that a "straight line model" matches the data as close as possible.
# definition

In Linear Regression we try to find a line such that the [[Residual Sum of Squares - RSS|sum of the squared residuals]] is as small as possible.
## $$\hat{y}=b + c_1x_1 + c_2x_2 + ... + c_nx_n$$
## $$\hat{Y}=\hat{\theta}^TX$$

^e184e6

# TOC:
- [[Assumptions of Linear Regression]]
- [[Datum Features]]:
	- [[linear regression with non-linear features]]
	- [[latent variables]]
	- [[feature selection in linear regression|feature selection]]
- [[Solving Linear Regression]]
	- [[assessing the performance of linear regression|assessing performance]] 
	- [[calculating confidence bands for linear regression predictions|confidence bands]]
		- [[heteroskedasticity v.s. homoskedasticity]]
- [[Making New Predictions in Linear Regression|making predictions]]

# also see:
- [[loss function]] 
- [[ridge regression v.s. lasso regression]]

# equations

- **Structural model:** $\hat{Y_i} = (\theta^*)^T X_i + W_i$ 
- **Estimator**: $\hat{\Theta} = (X^T X)^{-1} X^T Y$ 
- **Predictor**: $\hat{Y} = \hat{\Theta}^T X$ 
- **Standard error $\sigma_j$:**  standard deviation of $\hat{\Theta}_j$ 
- **95% confidence interval**: $CI = [\hat{\Theta}_j - 2\sigma_j, \hat{\Theta}_j + 2\sigma_j]$ 
- **Wald test:** reject "$\theta^*_j = 0$" if $0 \notin CI$ 
