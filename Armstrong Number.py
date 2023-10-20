from os import *
from sys import *
from collections import *
from math import *

n = input()
val = 0
for i in n:
    val += int(i)**len(n)

if val == int(n):
    print("true")
else:
    print("false")



from os import *
from sys import *
from collections import *
from math import *

b = int(input())
n = b
length = len(str(b))
res = 0
while n != 0:
    digit = n % 10
    res += digit ** length
    n = n// 10

if res == b:
    print("true")
else:
    print("false")