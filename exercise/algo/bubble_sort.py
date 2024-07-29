import random

nums = [random.randint(1, 20) for _ in range(10)]
print(nums)


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1, 0, -1):  # 反向遍历，n-1轮
        flag = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True  # 有交换元素
        if not flag:
            break  # 此轮“冒泡”未交换任何元素，说明数组已经有序


bubble_sort(nums)
print(nums)
