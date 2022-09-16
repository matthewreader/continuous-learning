from typing import List
import numpy as np


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = [nums[i] for i in range(0, len(nums), 2)]
        val = [nums[i] for i in range(1, len(nums), 2)]
        return np.concatenate([np.repeat(val[i], freq[i]) for i in range(len(freq))])
