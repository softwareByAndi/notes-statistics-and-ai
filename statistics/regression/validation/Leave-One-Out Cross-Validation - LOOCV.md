---
tags:
  - "#statistics"
links:
  - "[[cross-validation techniques]]"
---
1. train on $n-1$ datapoints and test on the last datapoint. 
2. repeat until all datapoints have used for validation.
# advantages
- no variability due to random choices of validation set
- uses all data for training
# drawbacks
- have to train $n$ times
- the $n$ prediction errors are highly dependent
