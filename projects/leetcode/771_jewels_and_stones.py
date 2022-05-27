from typing import List


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       return sum([stones.count(x) for x in jewels])
       

