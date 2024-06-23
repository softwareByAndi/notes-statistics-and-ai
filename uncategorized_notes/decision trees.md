---
tags:
  - artificial-intelligence
links:
  - "[[Naive AI Algorithms]]"
---

# pros
- white box
- can handle any data
- can model arbitrary functions
- little data prep
- good for large datasets
- built in feature selection
# limitations
- tend to overfit
- non-robust
	- slight changes to the data can change the structure of the decision tree, and alter decisions
- optimal solution is NP-Complete
# testing / validation
### mis-classification error:
the **mis-classification error** is calculated as a ratio of `misclassified : correct` for each item in the dataset.
### train v.s. validation split
an example of splitting data between training & validation
- train on 80%
- validate on 20%
# splitting
- see [[using entropy to learn decision trees]] & [[information gain]]
basically branches are made based on how the split affects the probability / ratio of the outcome results.
- e.g. a binary classification has 2 options: 1:0, T:F, Pass:Fail, and let's pretend that the ratio of T:F in the dataset is `60% True : 40% False`. when we select a feature-value-pair to branch from, we want this ratio to change in a way that most significantly increases that ratio. e.g. --> `90:10` or `10:90`, are both good.
- i.e. we want to select a branch that has the smallest [[using entropy to learn decision trees|entropy]] or the largest [[information gain|information gain]].
# pruning:
pruning is the art of dropping branches that do not improve the performance on the validation set; and it's used to help reduce overfitting in decision trees.

# referenced notes
- [[Decision Trees - Great Learning.pdf]]
- [[Construction of Decision Trees - Great Learning.pdf]]
- [[Tree Pruning - Great Learning.pdf]]


# code examples
- see [[hypothesis testing#notebook code snippets]]
``` python
model_dt = DecisionTreeClassifier(random_state=1)
model_dt.fit(X_train, y_train)

 # Checking performance on the training dataset
pred_train_dt = model_dt.predict(X_train)
metrics_score(y_train, pred_train_dt)

pred_test_dt = model_dt.predict(X_test)
metrics_score(y_test, pred_test_dt)
```
pruning / tuning to reduce overfitting
- #study-question how are the parameters selected...?
``` python
# Choose the type of classifier.
estimator = DecisionTreeClassifier(random_state=1)

# Grid of parameters to choose from
parameters = {
    "max_depth": np.arange(1,100,10),
    "max_leaf_nodes": [50, 75, 150, 250],
    "min_samples_split": [10, 30, 50, 70],
}
# Run the grid search
grid_obj = GridSearchCV(estimator, parameters, cv=5,scoring='recall',n_jobs=-1)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
estimator = grid_obj.best_estimator_

# Fit the best algorithm to the data.
estimator.fit(X_train, y_train)
```
checking performance after pruning
``` python
# Checking performance on the training dataset
dt_tuned = estimator.predict(X_train)
metrics_score(y_train,dt_tuned)

# Checking performance on the training dataset
y_pred_tuned = estimator.predict(X_test)
metrics_score(y_test,y_pred_tuned)
```
visualizing the decision tree
``` python
feature_names = list(X_train.columns)
plt.figure(figsize=(20, 10))
out = tree.plot_tree(
    estimator,
    max_depth=4,
    feature_names=feature_names,
    filled=True,
    fontsize=9,
    node_ids=False,
    class_names=None,
)
# below code will add arrows to the decision tree split if they are missing
for o in out:
    arrow = o.arrow_patch
    if arrow is not None:
        arrow.set_edgecolor("black")
        arrow.set_linewidth(1)
plt.show()
```
visualizing relative feature importance
``` python
# Importance of features in the tree building
importances = estimator.feature_importances_
indices = np.argsort(importances)

plt.figure(figsize=(8, 8))
plt.title("Feature Importances")
plt.barh(range(len(indices)), importances[indices], color="violet", align="center")
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.xlabel("Relative Importance")
plt.show()
```