---
tags: 
links:
  - "[[ensemble learning]]"
  - "[[decision trees]]"
  - "[[Naive AI Algorithms]]"
---
random forests apply [[ensemble learning]] using [[decision trees]], but each actor only has access to a random subset of features from the dataset.
- i.e. we [[bootstrap sampling|bootstrap sample]] data for each actor & then randomly sample a subset of features to train on.

feature sampling can also be done at every depth level too, instead of just on every tree.

# generalization error
$$Error \le \hat{p}\frac{(1-s^2)}{s^2}$$
- $\hat{p}$ = correlation between classifiers #study-question
	- increasing the number of features each actor uses, increases the correlation between classifiers
- $s$ = a measure of the strength of the classifier *(1-error)* #study-question
	- increasing the number of features each actor uses, increases the strength of the classifier
- these two terms are connected
![[Screenshot 2024-03-25 at 1.16.18 AM 1.png]]



# code examples
- see [[hypothesis testing#notebook code snippets]]
``` python
rf_estimator = RandomForestClassifier( random_state = 1)
rf_estimator.fit(X_train, y_train)

y_pred_train_rf = rf_estimator.predict(X_train)
metrics_score(y_train, y_pred_train_rf) # visualize metrics

y_pred_test_rf = rf_estimator.predict(X_test)
metrics_score(y_test, y_pred_test_rf) # visualize metrics
```
check feature importance
``` python
importances = rf_estimator.feature_importances_
columns = X_train.columns
importance_df = pd.DataFrame(
	importances, 
	index=columns, 
	columns=['Importance']
).sort_values(by='Importance', ascending=False)
plt.figure(figsize=(8, 8))
plt.title("Feature Importances")
sns.barplot(x=importance_df.Importance, y=importance_df.index, color="violet")
```
