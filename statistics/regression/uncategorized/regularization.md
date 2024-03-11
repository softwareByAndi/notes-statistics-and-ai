---
tags:
  - "#statistics"
links:
---
Regularization is the art of adjusting the [[loss function]] *(which determines the fit and accuracy of a model)* to also account for the values/magnitudes of the [[coefficients]] in some way.

By considering the magnitude of [[coefficients]], the [[loss function]] can encourage the selection of a more generalizable model.

I believe this refers to the idea that we want [[coefficients]] to stay as small as possible to prevent [[overfitting]], and to help keep *(/find?)* an optimal [[bias-variance trade-off]].
- Error functions like [[ridge regression v.s. lasso regression|ridge & lasso regression]] "incentivize" [[coefficients]] to stay small, rather than fitting the noise. 

# definition

regularization is a technique used in [[Regression]] analysis to prevent [[overfitting]] by penalizing large [[coefficients]]. It adds a penalty term to the [[loss function|loss function]], encouraging simpler models that generalize better for new data. ^3f8aa2

# see also:
- [[bias-variance trade-off]]
- [[ridge regression v.s. lasso regression]]
- [[linear regression with non-linear features#rescaling|rescaling features]]