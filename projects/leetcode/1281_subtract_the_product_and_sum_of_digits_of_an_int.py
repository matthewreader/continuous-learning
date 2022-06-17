import numpy as np

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = [int(x) for x in str(n)]
        return np.prod(nums) - np.sum(nums)
