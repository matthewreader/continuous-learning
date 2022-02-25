from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i]
        and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

        Args:
            nums: A list containing integers
        Returns:
            list: A list concatenated to itself.
        """
        return [*nums, *nums]


s = Solution()

print(s.getConcatenation([1,2,3,4]))