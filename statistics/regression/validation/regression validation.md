---
tags:
  - "#statistics"
links:
  - "[[Regression]]"
  - "[[assessing the performance of linear regression]]"
  - "[[cross-validation techniques]]"
---
```toc
```

# problem statement

the problem that's presented is that we have too many "optimal" predictors to chose from 
- assessing [[standard error|standard errors]]
- setting [[hyper parameters]]
- [[feature selection in linear regression|feature selection]]
- trying more and less "complex" models 
	- see [[linear regression with non-linear features]]
- choosing between different learning algorithms
	- see [[regularization]]
	- see [[ridge regression v.s. lasso regression]]

# goal statement

what we're really interested in is: 
- fitting and explaining existing data
- generalization - the goal is for the model to perform well on new data
	- i.e. avoid [[overfitting]]

and this is especially the case when there are no applicable formulas, where we need to just rely on the data we have.


# presented solutions

1. validation
2. [[bootstrap sampling]]

# validation

I believe this means to split the dataset into 3 sets #study-question 
These sets are typically chosen randomly

## 1. training set

the set of data that the model will be trained on.

## 2. validation set

this is used to test the fit of the training set
- see [[assessing the performance of linear regression]]

unfortunately, validation assessment is prone to [[overfitting]], so we need one more set to check for that.

## 3. test set

this is used to check the results of testing & validation for [[overfitting]]

# drawbacks

1. some data is "wasted"/not used for training, so we need enough data for each set
2. error on validation set has significant randomness because it depends on the choice of random division

these drawbacks are mitigated by using [[cross-validation techniques]]

# see also:
- [[cross-validation techniques]]
	- [[k-fold cross-validation]]
- [[bootstrap sampling]]
	- [[validation v.s. bootstrap]]
  
