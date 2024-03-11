Tags: #statistics 
Tags: [[Mean]] | [[Central Tendency Measures]]

Reciprocal of the arithmetic mean of reciprocals.
- Used for average rates and speeds. 

# $HM = \frac{n}{\sum \limits _{i=1} ^{n} \frac{1}{X_{i}}}$
<br>

## Example: 

_(For 60 miles at 60 mph and 60 miles at 30 mph, the average speed is 40 mph, not 45mph.)_

**easy to read example**: 
- 60 miles / 60 mph = 1 hour
- 60 miles / 30 mph = 2 hours
- 60 miles / 1.5 hours = 40 mph

## Code Examples
#### step by step description of the harmonic mean algorithm

``` python
# step by step description of the harmonic mean algorithm

sample_data = [37, 82, 65, 84, 70, 90, 44, 39, 27, 49, 33, 99, 58, 26, 74]
# 1. take the reciprocal of each value
reciprocals = [1/x for x in sample_data]
# 2. take average of reciprocals
avg_reciprocal = sum(reciprocals) / len(reciprocals)
# 3. take reciprocal of average
harmonic_mean = 1 / avg_reciprocal

print('sample data:      ', sample_data)
print('reciprocals:      ', [round(x, 4) for x in reciprocals])
print('avg_reciprocal:   ', round(avg_reciprocal, 4))
print('harmonic_mean:    ', round(harmonic_mean, 2))
print('arithmetic_mean:  ', round(sum(sample_data) / len(sample_data), 2))

"""
sample data:       [37, 82, 65, 84, 70, 90, 44, 39, 27, 49, 33, 99, 58, 26, 74]
reciprocals:       [0.027, 0.0122, 0.0154, 0.0119, 0.0143, 0.0111, 0.0227, 0.0256, 0.037, 0.0204, 0.0303, 0.0101, 0.0172, 0.0385, 0.0135]
avg_reciprocal:    0.0205
harmonic_mean:     48.81
arithmetic_mean:   58.47
"""
```

#### Example : Harmonic Mean of Speeds

``` python
# Harmonic Mean of Speeds Example
# average speed of 60 mph & 30 mph (is not 45 mph)
speeds = [60, 30]
avg = sum(speeds) / len(speeds) # for comparison
n = len(speeds)

reciprocals = [1/s for s in speeds]

h_mean = 1 / ( sum(reciprocals) / n )
# the equation can be simlified to: `n / sum(reciprocals)`
hm_short = n / sum(reciprocals)

print('speeds:                ', speeds)   # [60, 30]
print('arithmetic mean:       ', avg)      # 45.0 mph
print('Harmonic Mean:         ', h_mean)   # 40.0 mph
print('Harmonic Mean (short): ', hm_short) # 40.0 mph

"""
speeds:                 [60, 30]
arithmetic mean:        45.0
Harmonic Mean:          40.0
Harmonic Mean (short):  40.0
"""
```

#### fractions step by step

``` python
# fractions step by step
# speeds = 60 mph, 30 mph
avg_of_reciprocals = """
( 1/60 + 1/30 ) / 2 
    = ( 1/60 + 2/60 ) / 2 
    = ( 3/60 ) / 2 
    = 3/120 
    = 1/40 mph
"""

harmonic_mean = """
1 / (1/40 mph) = 40 mph
"""
```