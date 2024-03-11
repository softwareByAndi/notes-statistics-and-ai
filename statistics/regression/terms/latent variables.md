---
tags:
  - "#statistics"
links:
  - "[[Linear Regression]]"
---
The concept that the [[Datum Features|features]] $X$ and $Y$ are [[correlation|correlated]] / [[collinearity|collinear]], and $X$ predicts $Y$ very well, however, both X & Y are actually determined by the **hidden / latent variable $Z$.**

If this is the case, then any estimates of $\hat{Y}$ as an effect of $X$ will be wrong, and we may not even know it.

- note that the latent variable(s) ($Z$) usually cannot be measured directly.

# good estimators, bad predictors

we can get a good estimator based on current state, but we cannot answer `what if` questions

# solutions & mitigation

we can create new variables to account for the missing variables... not sure how to do this though... #study-question 

# examples

### incorrect model due to missing key / causal features

#### markets example:
lets say that we have multiple markets, which on their own show similar trends in their data, but when displayed on the same graph, will result in a trend that does not match.
- likely due to differing scales or [[Standardizing Data|standards]] that cause a fake trend to appear when overlayed over-top of each other

all trends for the individual markets may show a positive correlation between X & Y, but when put on the same graph, they may show a negative correlation between X & Y. 

The only issue is that we are not aware of, (or maybe the dataset simply does not include), this extra categorical data, so the resulting model is incorrect, and we may not even know it.
#### housing prices example
consider housing prices between 2 states which might show different trends when cost of living and avg. income are & aren't considered.

- housing prices in `state1` could be $800k compared to $300k in `state2`
- but avg income in `state1` could be $150k compared to $40k in `state2` 
- etc...

i.e. the trend might change if the prices were standardized as a ratio of `price:income` instead of comparing price alone