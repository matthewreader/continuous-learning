from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        add_candies = [candy + extraCandies for candy in candies]
        return [candy >= max_candies for candy in add_candies]
