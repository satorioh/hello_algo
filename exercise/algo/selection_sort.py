import random

nums = [random.randint(1, 20) for _ in range(10)]
print(nums)


def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):  # n-1轮后，前n-1个数已排序，故第n个数不用动
        min = i
        for j in range(i + 1, n):  # 到最后一个数
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]


selection_sort(nums)
print(nums)
