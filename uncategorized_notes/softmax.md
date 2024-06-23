---
links:
  - "[[AI]]"
  - "[[Statistics]]"
  - "[[Clustering]]"
  - "[[deep learning]]"
---

# definition

The `softmax` equation is a function used to convert a vector of arbitrary real values into a probability distribution. Given a vector $z$ of length $K$, the `softmax` function computes the probabilities $\sigma(z)_i$ for each element $z_i$ as follows:
$$ \sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^{K} e^{z_j}} $$
where 
- $e$ is the base of the natural logarithm ([[Euler's number (e)]])
- $K$ is the number of elements in the vector.
# example
$$z = [2, 1, 0.1]$$
$$\text{softmax}(2) = \frac{e^{2}}{e^{2} + e^{1} + e^{0.1}} \approx 0.664 $$
$$\text{softmax}(1) = \frac{e^{1}}{e^{2} + e^{1} + e^{0.1}} \approx 0.244$$
$$\text{softmax}(0.1) = \frac{e^{0.1}}{e^{2} + e^{1} + e^{0.1}} \approx 0.092$$

These values represent the probabilities associated with each element in the vector $z$ after applying the `softmax` function.

# how is softmax related to [[logistic regression]]?

Softmax regression, also known as multinomial logistic regression, is a generalization of logistic regression to handle multiple classes. It's closely related to logistic regression but extends it to handle multiple classes by using the softmax function to compute probabilities over multiple classes.

In logistic regression, the output is transformed using the sigmoid function to produce a probability between 0 and 1 for binary classification: #study-question

$$
P(y=1 | x) = \frac{1}{1 + e^{-z}}
$$

In softmax regression, we extend this idea to handle multiple classes. Instead of just one output node, we have multiple output nodes, one for each class. The softmax function is then applied to these outputs to convert them into probabilities that sum up to 1:

$$
P(y=j | x) = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}
$$

where $z_j$ is the score for class $j$, and $K$ is the total number of classes.

So, softmax regression is essentially an extension of logistic regression to handle multiple classes by using the softmax function to compute probabilities over those classes.