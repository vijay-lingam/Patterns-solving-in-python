class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        b = str(x)
        if (c == b[::-1]):
            return True
        else:
            return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        temp = x
        res = 0

        while(temp != 0):
            digit = temp % 10 
            res = res * 10 + digit 
            temp = temp // 10

        return x == res 
