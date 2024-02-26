Tags: #statistics #central-tendency
Tags: [[Central Tendency Measures]]

## definition

Middle value of a data set.
- median of odd sample count and even sample count are calculated differently
- **odd sample count**: middle value of sorted data set
- **even sample count**: average of the two middle values of sorted data set

## code examples
#### odd number values takes middle entry
``` python
values = [7, 12, 2, 6, 10]
sorted_values = sorted(values)
print('sorted values:', sorted_values) # [2, 6, 7, 10, 12]

median_index = len(values) // 2
median = sorted_values[ median_index ]

print(f'median = {median}') # 7
```
	sorted values: [2, 6, 7, 10, 12]
	median = 7

#### even number values takes average of middle two entries
``` python
values = [4, 8, 9, 7, 2, 1]
sorted_values = sorted(values)
print('sorted values:', sorted_values) # [1, 2, 4, 7, 8, 9]

high_index = len(sorted_values) // 2
low_index = high_index - 1

median_high = sorted_values[ high_index ]
median_low = sorted_values[ low_index ]
median = (median_low + median_high) / 2

# median = avg(4, 7) = 5.5
print(f'median = avg({median_low}, {median_high}) = {median}') 
```
	sorted values: [1, 2, 4, 7, 8, 9]
	median = avg(4, 7) = 5.5
