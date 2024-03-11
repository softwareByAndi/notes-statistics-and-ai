---
tags:
  - "#statistics"
links:
  - "[[Linear Regression]]"
---
It's important to note that these evaluation methods have nothing to do with accuracy.
They simply measure the fit of the model to the data. ^9cfba0

# evaluation methods
- [[r squared]] provides a good metric for assessing fit
- [[adjusted r squared]]
	- sometimes a model can have too much freedom (too many features)
	- in such a case, r-squared should not be trusted, and we should use adjusted r squared instead
- [[mean absolute error - MAE]]
- [[root mean square error - RMSE]] 

![[img_adjusted_r_squared_equation.png]]

![[img_regression_evaluation_equations_1.png]]

same equations but with context

![[img_regression_evaluation_equations_2.png]]


# see also:
- [[regression validation]]
- [[calculating confidence bands for linear regression predictions]]
- [[overfitting]]
