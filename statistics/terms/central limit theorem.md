---
tags: 
links:
---
basically implies that any random samples of a dataset are approximately normally distributed.

- also applies to noise, which means that a model that considers some noise ($W$) will have an unavoidable but known error with a variance of $\sigma_W^2$ which can be used differentiate between [[sources of error]]

### definition:
the sampling distribution of the sample means will approach normal distribution as the sample size gets bigger, no matter what the shape of the population distribution is.
- i.e. the averages of random samples are approximately normally distributed.

### assumptions:
- data must be randomly sampled
- sample values must be independent of each other
- sample size must be sufficiently large (n > 30)
- Samples should come from the same distribution

### we'll also notice some other behaviors:
- the mean of the sample means will be approximately equal to the population mean

- as the sample size gets bigger, the standard deviation of the sample means gets smaller
    - i.e. the sample means become more accurate and samples are more concentrated around the sample mean
    - i.e. the distribution becomes more normal and **narrower**
    
- the standard deviation of the sample means will be approximately equal to the population standard deviation divided by the square root of the sample size
#### $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$

