---
tags: 
links:
  - "[[Linear Regression]]"
key relations:
  - "[[latent variables]]"
---
After running regression, we get a coefficient vector that when applied to the input vector, produces an output. $\hat{Y}=\hat{\theta}^TX$ 

keep assuming the real structural model is $Y=(\theta^\star)^TX+W$ where $W$ represents random, normally distributed noise. *(see: [[central limit theorem]])*
- note that for linear regression, $\hat{\theta}^TX$ is an unbiased estimate of $(\theta^\star)^TX$ . <sup>*(and of Y)*</sup> 
# 2 sources of error
- unavoidable variance from $W$ 
	- **variance =** $\textcolor{red}{\sigma_W^2}$ 
- variance of $(\hat{\theta}-\theta^\star)^TX$ 
	- is this referencing the error in $\hat{Y}$ caused by the difference between the estimated coefficients $\hat{\theta}$ and the real coefficients $\theta^\star$ ? #study-question 
	- **variance equation** = $\textcolor{red}{\sigma_W^2X^T(\mathbb{X}^T\mathbb{X})^{-1}X}$ 
		- This is the equation to get the variance for this source of error, but I'm not sure what the equation implies... it looks like gibberish to me... #study-question 
## total prediction-error (variance):
it's just the sum of error variances
$$\sigma_W^2+\sigma_W^2X^T(\mathbb{X}^T\mathbb{X})^{-1}X$$


# also see:
- [[calculating confidence bands for linear regression predictions|confidence bands]]
- [[latent variables]]
