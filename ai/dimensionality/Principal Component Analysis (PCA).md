Tags: #artificial-intelligence #data-cleaning #linear-algebra 
Links: [[AI]] | [[Datum Features]] | [[Stochastic Neighbor Embedding]]

- [[PCA_via_SVD]]

a linear projection of that spreads data as much as possible

- PCA is used to simplify the set of [[Datum Features]] in a dataset to improve [[AI]] & training performance 
- PCA should be used before [[Clustering]] to find out the dimension of data that maximizes the [[Variance and Standard Deviation |variance]] of the features. 
	- *This eventually helps to reduce dimensions and decrease computation costs.*
- super fast!
- for a non-linear version, see [[Stochastic Neighbor Embedding]]

#### intuition
the goal is to find a low-dimensional projection that maximizes the spread / [[Variance and Standard Deviation |variance]] of the [[Datum Features]].

- **PC 1** = a straight line crossing through the dataset, from which the orthogonal distance to all points is minimized. see [[Sum of Squares]]?
- **PC 1 & PC 2** = a plane with the smallest orthogonal distance to all points


see: [[Spectral Decomposition Theorem]] and [[Covariance Matrix]]
- [[Eigenvectors]] --> the PCs
- [[Eigenvectors#Eigenvalues |Eigenvalues]]   --> the [[Variance and Standard Deviation |variances]] along PCs

