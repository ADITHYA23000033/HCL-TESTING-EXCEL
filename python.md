
# HCL-TESTING

# hcl-test

# Python programming

# Date: 25.09.2026

# PROGRAM 1 – Student Attendance Analysis

```python
students = list(map(int, input().split(',')))

seen = set()
left = 0
longest = 0

for right in range(len(students)):
    while students[right] in seen:
        seen.remove(students[left])
        left += 1

    seen.add(students[right])
    longest = max(longest, right - left + 1)

print(longest)
```

# PROGRAM 2 – Online Shopping Price Analysis

```python
discounts = list(map(int, input().split(',')))

current = discounts[0]
maximum = discounts[0]

for i in range(1, len(discounts)):
    current = max(discounts[i], current + discounts[i])
    maximum = max(maximum, current)

print(maximum)
```

# PROGRAM 3 – Rainwater Collection System

```python
heights = list(map(int, input().split(',')))

left = 0
right = len(heights) - 1
left_max = 0
right_max = 0
water = 0

while left < right:
    if heights[left] < heights[right]:
        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water += left_max - heights[left]
        left += 1
    else:
        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water += right_max - heights[right]
        right -= 1

print(water)
```

# PROGRAM 4 – Employee Performance Analysis

```python
scores = list(map(int, input().split(',')))

current = scores[0]
maximum = scores[0]

for i in range(1, len(scores)):
    current = max(scores[i], current + scores[i])
    maximum = max(maximum, current)

print(maximum)
```

# PROGRAM 5 – Product Sales Analysis

```python
sales = list(map(int, input().split(',')))

maximum = sales[0]
minimum = sales[0]
result = sales[0]

for i in range(1, len(sales)):
    value = sales[i]

    if value < 0:
        maximum, minimum = minimum, maximum

    maximum = max(value, maximum * value)
    minimum = min(value, minimum * value)

    result = max(result, maximum)

print(result)
```

# PROGRAM 6 – Customer Purchase History

```python
products = list(map(int, input().split(',')))

seen = set()
left = 0
longest = 0

for right in range(len(products)):
    while products[right] in seen:
        seen.remove(products[left])
        left += 1

    seen.add(products[right])
    longest = max(longest, right - left + 1)

print(longest)
```

# PROGRAM 7 – Bank Transaction Analysis

```python
transactions = list(map(int, input().split(',')))
target = int(input())

count = 0
prefix_sum = 0
seen = {0: 1}

for i in range(len(transactions)):
    prefix_sum += transactions[i]

    if prefix_sum - target in seen:
        count += seen[prefix_sum - target]

    seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

print(count)
```

# PROGRAM 8 – Employee Skill Grouping

```python
skills = input().split(',')

groups = {}

for skill in skills:
    key = ''.join(sorted(skill))

    if key not in groups:
        groups[key] = []

    groups[key].append(skill)

for group in groups.values():
    print(group)
```

# PROGRAM 9 – Network Packet Analysis

```python
packets = list(map(int, input().split(',')))

numbers = set(packets)
longest = 0

for num in numbers:
    if num - 1 not in numbers:
        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)
```

# PROGRAM 10 – Hospital Appointment Scheduling

```python
intervals = []

n = int(input())

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

merged = []

for interval in intervals:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
    else:
        merged[-1][1] = max(merged[-1][1], interval[1])

for interval in merged:
    print(interval[0], interval[1])
```
