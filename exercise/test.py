nums = [1, 3, 6, 8, 13, 13, 13, 21, 22, 28, 35]
target = 13


def binary_search_common(nums, target):
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if nums[m] < target:
            i = m + 1
        elif nums[m] > target:
            j = m - 1
        else:
            j = m - 1
    return j, i


def find_num(nums, target):
    j, i = binary_search_common(nums, target)
    if nums[i] != target:
        return -1
    return nums[i]


def find_insert_index(nums, target):
    j, i = binary_search_common(nums, target)
    return i


def find_left_index(nums, target):
    j, i = binary_search_common(nums, target)
    if nums[i] != target:
        return -1
    return i


def find_right_index(nums, target):
    j, i = binary_search_common(nums, target + 0.5)
    if nums[j] != target:
        return -1
    return j


print(find_right_index(nums, target))
