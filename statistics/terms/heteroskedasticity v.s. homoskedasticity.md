---
tags: 
links:
  - "[[assessing the performance of linear regression]]"
  - "[[calculating confidence bands for linear regression predictions]]"
---
something about plotting the trend of variance in the datapoints and determining if that variance is constant or if it changes / shows a trend... #study-question 
- for more details, see `#description` below
- in [[Linear Regression]], the comparison is made using the `error variance of the prediction`

![[img_heteroskedasticity_example.webp]]
#### heteroskedasticity
variance in the plot has a clearly defined trend
- for example, $\hat{Y}$ might have low $\sigma^2$ for small values of $X$ and increasingly higher $\sigma^2$ as the value of $X$ increases.
#### homoskedasticity
variance in the plot does not have a trend

# description

I think it's used as a term of how the variance changes as a function of the input.
###### Lets say that the datapoints are plotted via a scatter plot:
- then the ideal shape would be a line. 
	- this would be an example of `homoskedasticity`
- if the data points are grouped like a stream / bar shape, that would also be ideal, 
	- *(i.e. a line with consistent width / thickness = consistent variance)* 
	- this is also an example of `homoskedasticity`
- however, a triangle / diverging shape is another commonly seen pattern which implies a trend, where the spread of the datapoints *(i.e. the variance in $Y$)* grows or shrinks as $X$ changes 
	- this is an example of `heteroskedasticity` since the variance is not constant.

###### In other words: 
- if a linear regression were to be performed on the low-high parts of the [[calculating confidence bands for linear regression predictions|confidence bands]] then would the resulting confidence boundary lines be parallel? or would they diverge.
	- if parallel, that would imply `homoskedasticity`
	- if divergent, that would imply `heteroskedasticity`

