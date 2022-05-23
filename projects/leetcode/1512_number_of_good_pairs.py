from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if nums[i] == nums[j] and i < j:
                    good_pairs += 1
                    print(good_pairs)
        return good_pairs
        