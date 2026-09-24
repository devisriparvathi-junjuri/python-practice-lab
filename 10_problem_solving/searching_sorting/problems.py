"""Searching and sorting exercises.

Binary search requires sorted input. Example: search [1, 3, 5, 8] for 5 -> index 2.
Practice variation: return the insertion position when the value is missing.
Time: O(log n). Space: O(1).
"""


def binary_search(values: list[int], target: int) -> int:
    left, right = 0, len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values[:]
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    result: list[int] = []
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    return result + left + right
