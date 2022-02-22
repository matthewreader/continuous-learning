from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times.
        You may assume that the majority element always exists in the array.

        Args:
            nums: list of integers
        Returns:
            list: A list of length 2 containing the indices of numbers from nums that add up to target.
        """
        counts = {}
        majority_target = len(nums) / 2

        for item in nums:
            if item in counts:
                counts[item] += 1
            else:
                counts[item] = 1

        result = [key for (key, value) in counts.items() if value >= majority_target]
        return result[0]
