from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        answer = []
        for i in range(0, len(nums)):
            answer.append(sum([j < nums[i] for j in nums]))
        
        return(answer)
