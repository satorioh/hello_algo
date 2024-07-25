"""
二分查找
给定一个长度为n的数组 nums ，元素按从小到大的顺序排列且不重复。
请查找并返回元素 target 在该数组中的索引。若数组不包含该元素，则返回-1
"""
nums = [1, 3, 6, 8, 12, 15, 23, 26, 31, 35]
target = 6


def binary_search(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        mid = (j + i) // 2
        if nums[mid] < target:
            i = mid + 1
        elif nums[mid] > target:
            j = mid - 1
        else:
            return mid
    return -1


print(binary_search(nums, target))
