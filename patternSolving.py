Pattern-1: Rectangular Star Pattern
a = 5
for i in range(a):
    print(("*") * 5)

*****
*****
*****
*****
*****

Pattern-2: Right-Angled Triangle Pattern
a = 5
for i in range(1,a+1):
    print(i * ("*"))

*
**
***
****
*****

Pattern – 3: Right-Angled Number Pyramid
a = 5
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

1
12
123
1234
12345

Pattern – 4: Right-Angled Number Pyramid – II
a = 5
for i in range(1,a+1):
    for j in range(i):
        print(i,end="")
    print()

1
22
333
4444
55555

Pattern-5: Inverted Right Pyramid
a = 5
for i in range(a,-1,-1):
    print(i * "*")

*****
****
***
**
*

Pattern – 6: Inverted Numbered Right Pyramid
a = 5
for i in range(a,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()

54321
4321
321
21
1

Pattern – 7: Star Pyramid
a = 4
for i in range(a):
    #Printing the right side spaces
    for j in range(a-i-1):
        print(" ",end="")

    #Printing the stars
    for k in range(2*(i)+1):
        print("*",end="")

    #Printing the left side spaces
    for l in range(a-i-1):
        print("",end="")

    #Printing line space after each loop
    print()

    *
   ***
  *****
 *******


Pattern – 8: Inverted Star Pyramid
a = 4
for i in range(a,-1,-1):
    #Printing the right side spaces
    for j in range((a-i)):
        print(" ",end="")

    #Printing the stars
    for k in range(2*(i)+1):
        print("*",end="")

    #Printing the left side spaces
    for l in range((a-i)):
        print("",end="")

    #Printing line space after each loop
    print()

*********
 *******
  *****
   ***
    *

Pattern – 9: Diamond Star Pattern
a = 4
for i in range(a):
    #Printing the right side spaces
    for j in range(a-i-1):
        print(" ",end="")

    #Printing the stars
    for k in range(2*(i)+1):
        print("*",end="")

    #Printing the left side spaces
    for l in range(a-i-1):
        print("",end="")

    #Printing line space after each loop
    print()

for i in range(a-1,-1,-1):
    #Printing the right side spaces
    for j in range((a-i-1)):
        print(" ",end="")

    #Printing the stars
    for k in range(2*(i)+1):
        print("*",end="")

    #Printing the left side spaces
    for l in range((a-i-1)):
        print("",end="")

    #Printing line space after each loop
    print()

   *
  ***
 *****
*******
*******
 *****
  ***
   *

Pattern – 10: Half Diamond Star Pattern
a = 3
for i in range(1,a+1):
    print("*"*i)
for j in range(a-1,0,-1):
    print("*"*j)

*
**
***
**
*

Pattern – 11: Binary Number Triangle Pattern

a = 5
for i in range(a):
    if i % 2 == 0:
        for j in range(i+1):
            if j % 2 == 0:
                print("1",end="")
            else:
                print("0",end="")
        print()
    else:
        for j in range(i + 1):
            if j % 2 == 0:
                print("0", end="")
            else:
                print("1", end="")
        print()

1
01
101
0101
10101

# Pattern – 12: Number Crown Pattern
a = 4
for i in range(1,a+1):
    for j in range(1,i+1):
        print(j,end="")
    for k in range(a-i):
        print(" ",end="")
    for k in range(a-i):
        print(" ",end="")
    for j in range(i,0,-1):
        print(j,end="")

    print()

1      1
12    21
123  321
12344321

Pattern – 13: Increasing Number Triangle Pattern
a = 5
val = 1
for i in range(a):
    for j in range(i+1):
        print(val,end=" ")
        val += 1
    print()
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Pattern-14: Increasing Letter Triangle Pattern
def IncreasingLetter(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j),end="")
        print()
IncreasingLetter(5)

A
AB
ABC
ABCD
ABCDE

Pattern-15: Reverse Letter Triangle Pattern

def reverseLetter(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(chr(65+j),end="")
        print()

reverseLetter(5)

ABCDE
ABCD
ABC
AB
A

Pattern – 16: Alpha-Ramp Pattern

def alphaRamp(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end="")
        print()


alphaRamp(5)

A
BB
CCC
DDDD
EEEEE

Pattern – 17: Alpha-Hill Pattern

def alpha_hill_pattern(n):
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end="")
        ch = 65
        breakk = (2*i+1)//2-1
        for j in range(2*(i)+1):
            print(chr(ch),end="")
            if j <= breakk:
                ch += 1
            else:
                ch -= 1
        for k in range(n-i-1):
            print(" ",end="")
        print()

alpha_hill_pattern(5)

    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA

Pattern-18: Alpha-Triangle Pattern
def alpha_triangle_pattern(n):
    ch = 65
    for i in range(n):
        for j in range(i+1,0,-1):
            print((chr(ch+n-j)),end="")
        print()
alpha_triangle_pattern(5)

E
DE
CDE
BCDE
ABCDE

Pattern-19: Symmetric-Void Pattern

def symmetric_void_pattern(n):
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for j in range(i + 1):
            print("*", end="")
        print()
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for j in range(i + 1):
            print("*", end="")
        print()

symmetric_void_pattern(5)

**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********

Pattern – 20: Symmetric-Butterfly Pattern

def symmetric_butterfly_pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for j in range(i + 1):
            print("*", end="")
        print()
    for i in range(n - 2, -1, -1):
        for j in range(i+1):
            print("*",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for k in range(n-i-1):
            print(" ",end="")
        for j in range(i + 1):
            print("*", end="")
        print()
symmetric_butterfly_pattern(5)

*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

Pattern – 21: Hollow Rectangle Pattern

def hollow_rectangle_pattern(n):
    if n == 1:
        print("*")
    else:
        print("*" * n)
        for i in range(n-2):
            for j in range(n-1):
                if j == 0 or j == n-2:
                    print("*",end=" ")
                else:
                    print(" ",end="")
            print()

        print("*" * n)

hollow_rectangle_pattern(4)

****
*  *
*  *
****

# Pattern – 22: The Number Pattern

def number_pattern(n):
    for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            left = j
            right = (2*n-2) - j
            down = (2*n-2) - i

            print(n - min(min(top,down),min(right,left)),end="")

        print()

number_pattern(6)

66666666666
65555555556
65444444456
65433333456
65432223456
65432123456
65432223456
65433333456
65444444456
65555555556
66666666666