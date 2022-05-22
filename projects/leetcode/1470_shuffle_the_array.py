from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output_list = []
        x = n * 2
        for i in range(0, n):
            output_list.append(nums[i])
            output_list.append(nums[n + i])
        return output_list