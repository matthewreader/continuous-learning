from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Given an array of integers nums and an integer target, return indices of the two numbers such that they
        add up to target.

        Args:
            nums: list of integers
            target: the target sum of two integers from nums
        Returns:
            list: A list of length 2 containing the indices of numbers from nums that add up to target.
        """
        prev_map = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prev_map:
                return [prev_map[diff], index]
            prev_map[number] = index
