# Accuracy vs. Precision v.s. Recall:
**precision** tests the ratio how many positive estimates were actually positive, while **recall** tests the ratio of how well the model was able to identify positive results?

- **Accuracy:** How close measurements are to the true value.
	- $$\text{Accuracy} = \frac{\text{True Positives} + \text{True Negatives}}{\text{Total Predictions}}$$
- **Precision:** How close measurements are to each other, regardless of their accuracy.
	- $$\text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}$$
- **Recall**: measures the proportion of actual positives that are correctly identified by the model.
	- $$ \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}} $$
	- High recall means the model is good at capturing positives, but it may also capture more negatives as false positives.
	
While precision focuses on the accuracy of positive predictions, recall focuses on the model's ability to detect all positive instances. 

