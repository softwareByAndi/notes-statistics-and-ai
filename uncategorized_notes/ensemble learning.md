---
tags: 
links:
  - "[[decision trees]]"
  - "[[AI]]"
---
1. train multiple [[AI]] models using [[bootstrap sampling]] of the dataset for each model. -- **these are referred to as actors**
	1. subsets are chosen via random sampling with replacement
2. get prediction from each of the actors -- **this is referred to as voting**
3. aggregate the votes to get final prediction.
	1. aggregation is different for different types of models. 
	2. e.g. 
		1. [[Linear Regression]] would average the results
		2. [[Clustering]] would take the majority vote.
	3. in the event of a tie, the winning prediction is chosen randomly

ensemble learning, a.k.a. [[bagging]] helps reduce variance, and by extension, prevents overfitting. 