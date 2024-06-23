---
tags: 
links:
  - "[[Naive AI Algorithms]]"
  - "[[Regression]]"
---


# code examples
- see [[hypothesis testing#notebook code snippets]]

``` python
scaling = MinMaxScaler(feature_range=(-1,1)).fit(X_train)
X_train_scaled = scaling.transform(X_train)
X_test_scaled = scaling.transform(X_test)

# select kernel here
svm = SVC(
	kernel='linear', # swap with 'rbf' to use "radial basis function" kernel
	probability=True
) 
model = svm.fit(X= X_train_scaled, y = y_train)

# check performance
y_pred_train_svm = model.predict(X_train_scaled)
metrics_score(y_train, y_pred_train_svm) # prints metrics

# test performance
print("Testing performance:")
y_pred_test_svm = model.predict(X_test_scaled)
metrics_score(y_test, y_pred_test_svm) # prints metrics
```
print precision recall curve
``` python
# Predict on train data
y_scores_svm=model.predict_proba(X_train_scaled)
precisions_svm, recalls_svm, thresholds_svm = precision_recall_curve(y_train, y_scores_svm[:,1])
# Plot values of precisions, recalls, and thresholds
plt.figure(figsize=(10,7))
plt.plot(thresholds_svm, precisions_svm[:-1], 'b--', label='precision')
plt.plot(thresholds_svm, recalls_svm[:-1], 'g--', label = 'recall')
plt.xlabel('Threshold')
plt.legend(loc='upper left')
plt.ylim([0,1])
plt.show()
```
adjust threshold
``` python
optimal_threshold_svm=0.25
y_pred_train_svm = model.predict_proba(X_train_scaled)
metrics_score(y_train, y_pred_train_svm[:,1]>optimal_threshold_svm)

y_pred_test = model.predict_proba(X_test_scaled)
metrics_score(y_test, y_pred_test[:,1]>optimal_threshold_svm)
```
