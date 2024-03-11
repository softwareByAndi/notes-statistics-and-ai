---
tags:
  - "#statistics"
links:
  - "[[Regression]]"
  - "[[validation v.s. bootstrap]]"
  - "[[regression validation]]"
---
generate a sample-set by randomly sampling the dataset with replacement.
- note that some of the records can be selected multiple times

training on this sample-set will produce a **prediction** of the model's [[coefficients]]

repeat until $m$ samples are produced which are used to build a [[sampling distribution]] to model a an estimation of the true [[coefficients]].
- note that a [[sampling distribution]] is produced for each [[coefficients|coefficient]] in the model... #study-question 

does this method provide "more correct, more reliable" data? #study-question


# also see:
- [[validation v.s. bootstrap]]
- [[cross-validation techniques]]
- [[statistics/lecture_notes.ipynb]] see distributions & sampling distribution
- [[sampling distribution]]
	- [[standard error]]
- [[re-sampling]]
