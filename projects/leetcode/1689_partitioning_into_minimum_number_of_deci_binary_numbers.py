from typing import List


class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Given a string n that represents a positive decimal integer, return the
        minimum number of positive deci-binary numbers needed so that they sum 
        up to n.

        Args:
            n: A string containing only digits
        Returns:
            int: the minimum number of positive deci-binary numbers
        """

        return max([num for num in n])
