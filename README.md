# Bubble Sort

A simple implementation of the Bubble Sort algorithm in Python.

## Features

- Sorting algorithm implementation
- In-place sorting with O(n²) time complexity
- O(1) space complexity

## Usage

```python
from bubble_sort import bubble_sort

data = [64, 34, 25, 12, 22, 11, 90]
sorted_data = bubble_sort(data)
print(sorted_data)  # [11, 12, 22, 25, 34, 64, 90]
```

## Run Tests

```bash
python bubble_sort/bubble_sort.py
```

## Complexity

- Time: O(n²)
- Space: O(1)