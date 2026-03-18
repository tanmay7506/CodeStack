from collections import Counter
nums = [int(input()) for i in range(int(input()))]

value_counts = dict(Counter(nums))
max_frequency = max(value_counts.values())

most_common_values = sorted([
    value 
    for value, count in value_counts.items() 
    if count == max_frequency
])

print(most_common_values)
