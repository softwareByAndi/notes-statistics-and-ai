---
tags: 
links:
  - "[[Statistics]]"
  - "[[assessing the performance of linear regression]]"
  - "[[r squared]]"
---
$TSS$  is a measure of how far the data-points diverge from the <b><u>mean</b></u> ^2ec614
- it describes the "initial" variation in $Y$.
- compared to [[Residual Sum of Squares - RSS]] ![[Residual Sum of Squares - RSS#^90de8c]]
# $\text{TSS} = \sum_{i=1}^{n} (Y_i - \bar{Y})^2$

- $\bar{Y}$ = mean

### description
- for each datapoint, calculate the error ($R$) by calculating the difference between the dataset's mean and the actual value
	- $err=y-\bar{y}$
- squaring the error provides a positive value, and also makes bigger errors more sensitive, and smaller errors less sensitive
	- $err^2$
- summing the errors together provides a good metric of the initial variance inherent in the dataset.

### see also:
```dataview
LIST FROM [[Total Sum of Squares - TSS]] SORT file.name ASC
```
