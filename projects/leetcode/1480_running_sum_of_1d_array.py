from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

        Args:
            nums: A list containing integers
        Returns:
            list: A list containing a running sum of the list for each list index i.
        """

        return [sum(nums[:i+1]) for i in range(len(nums))]
