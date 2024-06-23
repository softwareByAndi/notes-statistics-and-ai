
#study-question #cleanup

The Likelihood Ratio Test (LRT) is a statistical test used to compare the goodness of fit between two models: a more complex one (with more parameters) and a simpler one (with fewer parameters). The test evaluates whether the addition of more parameters significantly improves the model's ability to explain the variability in the data.

In the context of logistic regression, it compares a model with at least one predictor against a null model with no predictors (just the intercept). The LRT statistic is calculated as:

$$\text{LRT statistic} = -2 \times (\text{log-likelihood of the null model} - \text{log-likelihood of the full model})$$

The resulting statistic approximately follows a chi-squared distribution, and the LLR p-value is the probability of obtaining a test statistic at least as extreme as the one that was actually observed, under the null hypothesis that the simpler model is true. A small p-value indicates that the complex model provides a significantly better fit than the simpler model.

# log likelihood
The log-likelihood for a model is the logarithm of the likelihood function, which measures the probability of observing the given data under the specific model. In logistic regression, for a binary outcome, the log-likelihood (\( \ell \)) of a model with parameters \(\beta\) is given by:

$$\ell(\beta) = \sum_{i=1}^{n} [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)] $$

Where:
- $n$ is the number of observations.
- $y_i$ is the observed outcome for observation $i$ (0 or 1).
- $p_i$ is the predicted probability of the outcome being 1 for observation \( i \), given by the logistic function $$p_i = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + ... + \beta_k x_{k})}}$$ 
	- where $\beta_0$ is the intercept, 
	- $\beta_1 ... \beta_k$ are the coefficients for each predictor $x_1 ... x_k$
	- and $e$ is the base of the natural logarithm.

The log-likelihood is used because it simplifies the calculations and leads to more stable numerical properties when maximizing the likelihood to estimate the model parameters.