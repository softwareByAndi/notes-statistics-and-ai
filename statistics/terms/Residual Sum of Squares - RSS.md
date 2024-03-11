---
tags: 
links:
  - "[[Statistics]]"
  - "[[assessing the performance of linear regression]]"
  - "[[r squared]]"
---
$RSS$ is a measure of how far the data-points diverge from the <b><u>predicted value</u></b> ^90de8c
- it describes the unexplained variation in $Y$  ^e0b4ec
- compared to [[Total Sum of Squares - TSS]] ![[Total Sum of Squares - TSS#^2ec614]]
# $\hat{Y_i}=\hat{\theta}^TX_i$ 
- see [[Linear Regression]] 
# $\sum_{i=1}^{n} (Y_i - \hat{Y_i})^2$ 

- what is $\hat{\theta}^T$ in this equation? the [[coefficients]]  matrix? #study-question

### description
- for each datapoint, calculate the error ($R$) by calculating the difference between the estimated / predicted value and the actual value
	- $err=\hat{y}-y$
- squaring the error provides a positive value, and also makes bigger errors more sensitive, and smaller errors less sensitive
	- $err^2$
- summing the errors together provides a good metric of how the algorithm compares to previous iterations
	- e.g. does a given change make the model better or worse...

### see also:
```dataview
LIST FROM [[Residual Sum of Squares - RSS]] SORT file.name ASC
```
