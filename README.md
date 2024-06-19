# Lab.11
def task1(arr):
    return sum(x ** 2 for x in arr)

print(task1([1, 2, 3]))  # Output: 14
Ця функція обчислює суму квадратів елементів списку arr. Використовується генератор списку для підрахунку квадратів кожного елемента x в arr, і потім сумується ці значення.

Функція task2

def task2(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)

print(task2([1, 2, 3, 4, 10]))  # Output: 14
Ця функція обчислює суму тих елементів списку arr, які більше або рівні середньому значенню цього списку.

Функція task3

from collections import Counter

def task3(arr):
    freq_map = Counter(arr)
    return sorted(arr, key=lambda x: (-freq_map[x], x))

print(task3([4, 6, 2, 6, 4, 4, 6]))  # Output: [4, 4, 4, 6, 6, 6, 2]
Ця функція сортує список arr за частотою входження кожного елемента, спочатку за спаданням частоти, а потім за зростанням значення.

Функція task4

def task4(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

print(task4([1, 2, 4, 5]))  # Output: 3
Ця функція знаходить відсутній елемент у послідовності чисел від 1 до n, де n = len(arr) + 1. Використовується формула суми арифметичної прогресії для обчислення загальної суми чисел від 1 до n, а потім віднімається сума елементів списку arr.

Функція task5

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

print(task5([100, 4, 200, 1, 3, 2]))  # Output: 4
Ця функція знаходить найбільшу довжину послідовності неперервних чисел у заданому списку nums. Використовується множина для ефективної перевірки наявності числа, а потім ітеративно знаходить послідовності за допомогою циклу while.

Функція task6

def task6(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

print(task6([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
Ця функція реалізує циклічний зсув елементів списку arr на k позицій вправо. Використовується оператор зсуву за допомогою зрізів списку.

Функція task7

def task7(arr):
    left_products = [1]
    right_products = [1]

    for i in range(len(arr) - 1):
        left_products.append(left_products[-1] * arr[i])
        right_products.append(right_products[-1] * arr[-i - 1])

    right_products = right_products[::-1]

    return [left * right for left, right in zip(left_products, right_products)]

print(task7([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
Ця функція обчислює масив добутків лівих і правих елементів для кожного елемента вхідного списку arr. Для цього використовуються два масиви left_products і right_products, які обчислюються у двох напрямках (ліворуч і праворуч від кожного елемента).

Функція task8

def task8(nums):
    max_sum = curr_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

print(task8([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
Ця функція знаходить найбільшу суму підмасиву (підрядка) в масиві nums. Використовується алгоритм з лінійною складністю за часом, що базується на принципі динамічного програмування.

Функція task9

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

print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Ця функція обходить матрицю по круговій спіралі (ззовні в середину) і повертає список з її елементів в такому порядку.

Функція task10

import math

def task10(points, k):
    points.sort(key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))
    return points[:k]

print(task10([(1, 2), (1, 1), (3, 4)], 2))  # Output: [(1, 1), (1, 2)]
Ця функція вибирає перші k точок зі списку points, які мають найменшу відстань до початку координат (0, 0). Використовується сортування з використанням lambda-функції для обчислення відстані від кожної точки до початку
