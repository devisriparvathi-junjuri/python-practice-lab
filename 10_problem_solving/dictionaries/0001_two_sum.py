from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []


if __name__ == "__main__":
    print(Solution().twoSum([2, 7, 11, 15], 9))
