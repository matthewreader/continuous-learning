from typing import List


class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Returns a defanged IP address using string replace method

        Args:
            address: a valid IP address
        Returns:
            defanged IP address
        """
        return address.replace(".", "[.]")

