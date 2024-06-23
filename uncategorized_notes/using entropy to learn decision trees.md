entropy is a measure of purity / homogeneity in the dataset
- A low entropy value indicates a high degree of homogeneity or purity. 
- i.e. Low entropy means the data is very similar (or pure), whereas high entropy indicates a mix of different classes (or impurity).


# entropy equation
$$ \text{Entropy}(S) = -\sum_{i=1}^{n} p_i \log_2(p_i) $$
- $S$ is the set for which entropy is being calculated.
- $n$ is the number of classes in the set $S$.
- $p_i$ is the proportion (or probability) of class $i$ within the set.
