Tags: #artificial-intelligence #definition 
Links: [[AI]] | [[Reducing Feature Dimensionality]] | [[Correlation v.s. Covariance]]

features are variables that are used to describe a data point.
	e.g. columns in a record

**feature engineering** = the creation of new input or target features from existing features.

**it's important to:**
- convert [[Categorical Data]] into numbers *(for most applications)*.
- [[Normalizing Data |normalize]] all values in the dataset. 
	- *(comparing values on differing scales is difficult)*
	- but also because features with differing scales will affect the results of [[Principal Component Analysis (PCA)|PCA]]
	- use [[Correlation v.s. Covariance|Correlation instead of Covariance]] if different units are compared.
	
- the more features included in a dataset, the more difficult, expensive and time consuming it is to parse anything meaningful from that dataset.
	- see [[Reducing Feature Dimensionality]]


### see also:
```dataview
LIST FROM [[Datum Features]] SORT file.name ASC
```
