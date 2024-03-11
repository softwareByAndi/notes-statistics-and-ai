---
tags:
  - "#statistics"
links:
  - "[[cross-validation techniques]]"
---
1. split the data into $k$ groups *(a.k.a. folds)*
2. train on $k$ - 1 folds, and test on the last fold
3. repeat until each fold has been used for validation

note that if $k$ = $n$, this is the same as [[Leave-One-Out Cross-Validation - LOOCV]]
# advantages
- the prediction errors are less dependent than with [[Leave-One-Out Cross-Validation - LOOCV|LOOCV]]. does this mean that they're not highly dependent though? #study-question 
# disadvantages
#study-question