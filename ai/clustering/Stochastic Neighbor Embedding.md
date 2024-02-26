Links: [[AI]] | [[Datum Features]] | [[Principal Component Analysis (PCA)]]

SNE is a non-linear embedding that tries to keep close-by points close.

more accurately, it's a probabilistic approach to place samples from high-dimensional space into low-dimensional space so as to preserve the identity of neighbors with the intention of **preserving clusters** so that close points remain close and far points remain far away.

- the goal is to find which embedding gives the best low-dimensional approximation of high-dimensional data
- for a faster, linear version, see [[Principal Component Analysis (PCA)]]

[[t-SNE]] uses [[Kullback-Leibler Divergence]] to [[Measurements of Distance|measure ''distance"]] between distributions
- also see: [[T-Distributions]]
