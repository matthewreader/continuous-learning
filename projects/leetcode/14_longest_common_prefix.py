from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        sorted_strs = sorted(strs, key=len)
        shortest_word = sorted_strs[0]
        
        for i in range(0, len(shortest_word)):
            for word in strs:
                if shortest_word != word[0:len(shortest_word)]:
                    shortest_word = shortest_word[:-1]
        
        return shortest_word
        
