"""List problems: frequency counting and two pointers.

Problem: return two indexes whose values sum to target.
Example: [2, 7, 11, 15], 9 -> (0, 1).
Practice variation: return every unique pair.
Time: O(n) average. Space: O(n).
"""


def two_sum(values: list[int], target: int) -> tuple[int, int] | None:
    seen: dict[int, int] = {}
    for index, value in enumerate(values):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index
    return None


def move_zeroes(values: list[int]) -> list[int]:
    non_zeroes = [value for value in values if value != 0]
    return non_zeroes + [0] * (len(values) - len(non_zeroes))
