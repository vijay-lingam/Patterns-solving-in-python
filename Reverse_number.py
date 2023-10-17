class Solution:
    def reverse(self, x: int) -> int:
        des = 1 if x > 0  else -1
        max_int = 2**31 -1
        s = str(abs(x)) #removing the negative sign from the give value
        x = int(s[::-1]) #reversed the string and converted it to integer
        if x > max_int:
            return 0
        else:
            return x * des

class Solution:
    def reverse(self, x: int) -> int:
        des = 1 if x > 0 else -1
        max_int = 2**31 -1
        num = abs(x)
        rev = 0
        #1 2 3
        #3 2 1
        while num!= 0:
            if rev > max_int / 10:
                return 0
            digit =  num % 10 # gives the reminder 3 2 1
            rev = rev * 10 + digit # 32 * 10 + 1 = 321
            num = num // 10 #give the quotient 0
        return rev * des