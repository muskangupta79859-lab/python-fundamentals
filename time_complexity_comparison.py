import time
import math

# Linear Search O(n)
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False


# Binary Search O(log n)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test data
arr = list(range(1, 1000000))
target = 999999

# Linear search timing
start = time.time()
linear_search(arr, target)
end = time.time()
print("Linear Search Time:", end - start)

# Binary search timing
start = time.time()
binary_search(arr, target)
end = time.time()
print("Binary Search Time:", end - start)
