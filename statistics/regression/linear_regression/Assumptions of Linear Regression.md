---
tags:
  - "#TODO"
links:
  - "[[Linear Regression]]"
---
Linear regression models rely on several key assumptions. Addressing these helps ensure model reliability and accuracy.

1. **Linearity**: The relationship between the independent variables and the dependent variable is linear.
   - **Test**: Scatter plots of residuals vs. predicted values or independent variables.
   - **Fix**: Transformation of variables (log, square root, etc.).

2. **Independence**: Observations are independent of each other.
   - **Test**: Durbin-Watson statistic.
   - **Fix**: Use time series analysis techniques if data are time-dependent.

3. **Homoscedasticity**: Constant variance of error terms.
   - **Test**: Scatter plot of residuals vs. predicted values.
   - **Fix**: Transform the dependent variable, adjust weights, or use robust regression methods.

4. **Normal Distribution of Errors**: Residuals are normally distributed.
   - **Test**: Q-Q plot or Shapiro-Wilk test.
   - **Fix**: Transformation of the dependent variable or using non-parametric regression methods.

5. **No multicollinearity**: Independent variables are not too highly correlated.
   - **Test**: Variance Inflation Factor (VIF).
   - **Fix**: Remove correlated variables, use Principal Component Analysis (PCA), or Ridge regression.

Addressing these assumptions ensures your linear regression model's validity and accuracy.