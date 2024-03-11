---
tags:
  - "#statistics"
links:
  - "[[explanatory statistics]]"
  - "[[Solving Linear Regression]]"
  - "[[Linear Regression]]"
---
assumes the dataset/world is linear, and learns the coefficients.
![[Solving Linear Regression#linear regression equation]]

# equation representing a linear assumption: 
- $W_i$ represents noise
- variables follow a Normal distribution - *(see [[central limit theorem]])*
## $$Y_i = \theta_0^* + \theta_1^* X_i + W_i$$

I'm not exactly sure about the following details, so look it up somewhere #research-topic


<hr>


## representing the linear equation as a probability: $$\max_{\theta} \mathbb{P}(Y | X; \theta)$$
# equation to solve: $$\prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp \left( -\frac{(Y_i - \theta_0 - \theta_1 X_i)^2}{2\sigma^2} \right)$$ 
## simplifies to solving for just this part: $$(Y_i - \theta_0 - \theta_1 X_i)^2$$ 
## which is basically? $$\min_{\theta} \sum_{i=1}^{n} \left( \theta^T x_i - y_i \right)^2$$ 
## and is solved by:  $$\hat{\theta} = \left( X^T X \right)^{-1} X^T Y$$
