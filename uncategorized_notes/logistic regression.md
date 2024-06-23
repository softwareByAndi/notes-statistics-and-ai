---
tags: 
links:
  - "[[Regression]]"
---
# raw, disjointed notes
- used for binary classification
- used to predict the probability that an observation belongs to one of two possible classes

the sigmoid function is a popular function for logistic regression
![[img_sigmoid_function.png]]

**Assumptions :**

1. Binary logistic regression requires the dependent variable to be categorical and binary.
2. Logistic regression requires the observations to be independent of each other. In other words, the observations should not come from repeated measurements or matched data.
3. Logistic regression requires there to be little or no multicollinearity among the independent variables.  This means that the independent variables should not be too highly correlated with each other.


# code examples
- see [[hypothesis testing#notebook code snippets]]
```python
# Fitting logistic regression model
lg = LogisticRegression()
lg.fit(X_train,y_train)
# Checking the performance on the training data
y_pred_train = lg.predict(X_train)
metrics_score(y_train, y_pred_train)
```
![[Pasted image 20240325052656.png]]
![[Pasted image 20240325052717.png]] 
``` python
# Checking the performance on the test dataset
y_pred_test = lg.predict(X_test)
metrics_score(y_test, y_pred_test)
```
![[Pasted image 20240325052916.png]]
![[Pasted image 20240325052939.png]]

