from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        """
        Returns a defanged IP address using string replace method

        Args:
            accounts: an m x n integer grid where accounts[i][j] is the amount of money
            customer i has in the jth bank account.
        Returns:
            the amount of money the most wealthy account holds
        """
        return sum(max(accounts, key=sum))

