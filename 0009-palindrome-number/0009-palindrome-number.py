class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x = x  
        reversed_x = 0
        if x < 0 : 
            return False
        while x:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x = x // 10
        
        if original_x == reversed_x:
            return True
        else:
            return False