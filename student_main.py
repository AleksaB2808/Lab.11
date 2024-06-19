def task1(arr):
    return sum(x ** 2 for x in arr)

print(task1([1, 2, 3])) # Output: 14

def task2(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)

print(task2([1, 2, 3, 4, 10])) # Output: 14

from collections import Counter

def task3(arr):
    freq_map = Counter(arr)
    return sorted(arr, key=lambda x: (-freq_map[x], x))

print(task3([4, 6, 2, 6, 4, 4, 6])) # Output: [4, 4, 4, 6, 6, 6, 2]

def task4(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

print(task4([1, 2, 4, 5])) # Output: 3

def task5(nums):
    nums = set(nums)
    max_len = 0
    for num in nums:
        if num - 1 not in nums:
            curr_num = num
            curr_len = 1

            while curr_num + 1 in nums:
                curr_num += 1
                curr_len += 1

            max_len = max(max_len, curr_len)

    return max_len

print(task5([100, 4, 200, 1, 3, 2])) # Output: 4

def task6(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

print(task6([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3]

def task7(arr):
    left_products = [1]
    right_products = [1]

    for i in range(len(arr) - 1):
        left_products.append(left_products[-1] * arr[i])
        right_products.append(right_products[-1] * arr[-i - 1])

    right_products = right_products[::-1]

    return [left * right for left, right in zip(left_products, right_products)]

print(task7([1, 2, 3, 4])) # Output: [24, 12, 8, 6]

def task8(nums):
    max_sum = curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(task8([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6

def task9(matrix):
    if not matrix:
        return []

    result = []
    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

import math

def task10(points, k):
    points.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
    return points[:k]

print(task10([(1, 2), (1, 1), (3, 4)], 2)) # Output: [(1, 1), (1, 2)]
