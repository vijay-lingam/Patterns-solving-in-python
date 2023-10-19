class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = str(x)
        b = str(x)
        if (c == b[::-1]):
            return True
        else:
            return False
