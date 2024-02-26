Tags: #statistics
Tags: [[Mean]] [[Central Tendency Measures]]

#### equation definition:
Nth root of the product of N values.

Indicates the central tendency or typical value of a set of numbers.
- It is particularly useful when comparing different items with very different ranges
- e.g. like growth rates, financial ratios, etc.

# $GM = \left( \prod \limits _{i=1} ^{n} X_{i} \right)^{\frac{1}{n}}$

<br>

#### example code

``` python
# Example data
data = [1.5, 2.5, 3.5, 4.5, 5.5]

# Manual implementation
def geometric_mean_manual(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product ** (1 / len(numbers))
gm_manual = geometric_mean_manual(data)
print("Geometric Mean (manual implementation):   ", gm_manual)

# Using the statistics module
from statistics import geometric_mean
gm = geometric_mean(data)
print("Geometric Mean (using statistics module): ", gm)
```
	Geometric Mean (manual implementation):    3.1793248390897833
	Geometric Mean (using statistics module):  3.179324839089783
