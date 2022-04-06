from typing import List


class Solution:
    """Determine whether or not an input word is a palindrome
    
    Args:
        x: an integer
    Returns:
        bool: whether or not the input integer is a palindrome
    """    
    def isPalindrome(self, x: int) -> bool:
        
        int_as_str = str(x)
        
        if len(int_as_str) < 2:
            return True
            
        elif int_as_str[0:1] == int_as_str[-1:]:
            int_as_str = int_as_str[1:len(int_as_str) - 1]
            return self.isPalindrome(int_as_str)
            
        else:
            return False
