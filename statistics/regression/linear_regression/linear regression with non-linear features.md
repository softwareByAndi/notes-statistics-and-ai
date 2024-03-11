---
tags: 
links:
  - "[[Linear Regression]]"
  - "[[Datum Features]]"
  - "[[non-linear regression]]"
---
#### converting non-linear features into linear features

To perform [[Linear Regression]] with non-linear features, we can add new [[Datum Features|features]] which are a transformation of existing features, then perform regression on these new features to test if they are significant or not.

e.g. 
- $log(X_1)$
- $exp(X_1)$

such transformations can turn a non-linear [[correlation|correlation]] into a linear one 
- e.g. maybe there is a better linear [[correlation|correlation]] between $Y$ and $log(X_1)$ v.s. $X_1$ *(which may have a correlation with $Y$, just not a linear one...)* 

#### rescaling

note that especially for combination features like $X_C=X_1X_2$, it's important to [[Standardizing Data|scale]] the data into the same range as the other data points. 

If $X_C$ is significantly larger than the other [[Datum Features|features]], then the [[coefficients|coefficient]] of $X_C$ will be very small to account for the huge scale, and even if the [[r squared|R value]] improves significantly, we might mistake $X_C$ as not having an large effect on the output.
- see: [[feature selection in linear regression]] 
