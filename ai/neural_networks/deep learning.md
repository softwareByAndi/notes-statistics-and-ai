---
links:
  - "[[AI]]"
  - "[[module - deep learning]]"
  - "[[softmax]]"
---
# random and dis-jointed notes

the goal is to data encoded as useful [[feature vectors]]
- e.g. category, sentiment or properties-of

what's a good encoding for an image? regression on datapoints can draw some linear function to classify, but general data (such as images) is more difficult...
- neural networks learn this encoding (+prediction) automatically.
- this is why they include a lot of data

specialized methods to encode
- CNN - images / categories
- RNN - text / sentiment
- GNN - molecule / properties-of

## feed forward neural network

3+ layers
- input layer
- 1+ hidden layers
	- each of these layers basically [[re-encoding of data|re-encodes the data]]
	- increasing the # of nodes in a layer will allow the decision boundary more flexibility to make a shape that fits.
		- note that this may lead to overfitting.
- output layer

1. each feature is the input for a node in the input layer
2. each node has an output that attaches to 1~n nodes of the next layer
3. the inputs for each node in the hidden layer(s) are weighted to determine & adjust the importance of each input for each node. 
4. the weighted inputs are summed together and passed through an activation function which produces the node's output
	1. sigmoid : (0-1)
	2. tanh : (-1,1)
	3. rectifier / (ReLU) rectified linear unit : [0,~)
		1. used heavily in computer vision
		2. computationally less expensive

## hierarchical representations: multiple layers

a NN basically breaks the problem into steps (1 step for each layer)
- e.g. input --> edges --> simple parts --> parts --> scenes

## output probability distribution
see [[softmax]]
![[softmax#example]]

## loss functions

loss functions measure the error in the prediction.
- **regression** uses [[mean squared error (MSE)]]
- **classification** uses [[negative log-likelihood]] / cross-entropy

## adjusting weights

Taking the partial derivative of the loss function for each weight shows the current slope for that weight. Move the weight in the opposite direction of that slope (towards 0) in order to minimize the loss function.
- $w_i > 0$ : decrease the weight
- $w_i < 0$ : increase the weight

#study-question calculus's chain rule applies here, for adjusting previous layers
- see [[back-propagation]]
- note the issue of [[vanishing & exploding gradients]] when weights are too small (close to 0) or too large.

## initialization
initializing weights has a huge impact on which local minima the algorithm will find.
typical initialization is random, with [[gaussian distribution]], zero mean.
- variance depends on number of nodes in a layer 
	- e.g. $\sigma^2 = \frac{2}{\text{\#nodes}}$ 

note that if all weights are initialized to the same value, then all neurons would learn the same thing. 

## step size
- too small and it will take too long to learn
- too large and the algorithm will keep jumping the local minima and never converge.

one method of determining step size is to plot the error for each epoc across a range of step sizes. 
- if the plot is jagged, then the step size is too big.
- if the plot is very slow to reach the minimum, then it's probably too small
![[Pasted image 20240411184114.png]]

### improvements
- adjust the step size for each network weight adaptively, according to the gradient.
	- see [[AdaGrad]]
- use momentum
- combine momentum with adaptive step size
- stochastic approaches

## regularization methods
- adding a [[regularization]] term to the training loss function
	- #study-question squared norm / weight decay
		- $+\frac{\lambda}{2}||\theta||^2$ 
- early stopping
	- check the error on validation set after each epoc, and stop the training early if the error plot plateaus
- data augmentation
	- perturbations (rotation, noise, ... )
	- averaging
- dropout
	- For each training data point, randomly switch of $\frac{1}{2}$ of the units. don't update the units that have been switched off; at test time, turn all weights on and scale all weights by $\frac{1}{2}$. This creates a sparse network that trains on only half of its available resources and works as something like an ensemble when all weights are on.
	- #study-question not sure why one wouldn't just train an ensemble instead though...
- batch normalization
	- normalize the inputs of each layer