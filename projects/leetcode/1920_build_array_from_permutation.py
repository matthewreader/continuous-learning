from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        """
        Given a zero-based permutation nums (0-indexed), build an array ans of the same length where
        ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

        Args:
            nums: A list containing integers
        Returns:
            list: The permutation of nums
        """

        return [nums[nums[i]] for i in range(len(nums))]
