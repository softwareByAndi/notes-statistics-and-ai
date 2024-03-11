---
tags:
  - "#uncategorized"
  - "#TODO"
links:
  - "[[Linear Regression]]"
  - "[[coefficients]]"
  - "[[hypothesis testing]]"
  - "[[Reducing Feature Dimensionality]]"
---
after training, we get a bunch of data and included in it is the p-value for each feature.
- note that we only care about p-values for which we can reject the null hypothesis
- i.e. we only care about features that have p-values that are lower than 0.05
	- a high p-value is basically saying *"there's a high probability that this coefficient is 0, and therefore is not important"* 
- this is because the coefficient's magnitude measures the importance of the feature, and the p-value tests the null hypothesis which asserts that the true coefficient value is 0.
	- a coeff of 0 means that the feature has **no impact** on the output
- so a low p-value means we reject the hypothesis that the coeff is 0 *(that the feature has no impact on the output)* which in turn implies that the feature *may* be important.

# see related:

- [[coefficients]]
- [[r squared]]
- [[statistics/lecture_notes.ipynb]] (see p-value & hypothesis testing)
- [[Datum Features]]
- [[hypothesis testing]]