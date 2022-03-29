from typing import List


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """
        Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

        Args:
            low: Lower boundary of the range
            high: Upper boundary of the range
        Returns:
            int: Total odd numbers between low and high (inclusive)
        """

        # Two even endpoints will have half the range
        if low % 2 == 0 and high % 2 == 0:
            return (high - low) // 2
            
        # Any other endpoint will have half the range plus 1
        else:
            return ((high - low) // 2) + 1

