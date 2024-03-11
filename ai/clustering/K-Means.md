Tags: #artificial-intelligence #naive-ai #clustering
Links: [[Clustering]] | [[Naive AI Algorithms]] | [[Estimating Number of Clusters]]

k means is a clustering algorithm used to find groups of clusters.

#### beyond k-means
- [[K-Medoids]]
- [[Gaussian Mixture Models]]
- [[Spectral Clustering]]
- [[DP-Means]]
- [[BP-Means]]
- [[Soft Clustering]]
## applications

- [[Document Clustering]]
- [[Customer Segmentation]]
- [[Image Segmentation]]
- [[Image Compression]]
- [[Data Mining]]

## algorithm

1. take a number of (k) centroids / nodes
2. place the centroids randomly in the [[Vectors |vector]] space 
3. for each item in the vector space, calculate it's [[Measurements of Distance |distance]] to each of the centroids
	1. [[BigO]]$(k * n)$ .
	2. Typically [[Euclidean Distance]]
4. assign each item to whichever centroid is closest to it
5. move the position of each centroid to the center ([[Mean]]) of the items assigned to it
6. repeat steps 3-5 until stable.
	1. typically measured by minimizing [[Residual Sum of Squares - RSS]]

### also see:
- [[Soft Clustering]] can be used to provide a probability of belonging in any of the centroids
- [[Clustering Penalty Evaluators]]

## assumptions

;TLDR:
1. cluster data is normalized
2. number of clusters is known
3. cluster boundaries are linear
4. clusters are the same size
5. clusters have similar densities

;TSDU:
1. it's always best to [[Standardizing Data |standardize]] / [[Normalizing Data |normalize]] the data first
2. . assumes you know the number of clusters in advance
	1. there are ways of estimating this algorithmically. [[Estimating Number of Clusters]]
3. limited to linear cluster boundaries
	1. in other words, clusters that wrap around other clusters be problematic
4. clusters need to be the same size
	1. otherwise a small cluster at the boundary of a large cluster would steal items that should belong to the large cluster
5. clusters should have a similar number of points assigned to them
	1. not sure why... #is-this-important

## hurdles

1. sometimes difficult to identify and get out of a local optimum to find the [[Finding Global Optimums |global optimum]]. 
	1. ![[Finding Global Optimums]]
2. 