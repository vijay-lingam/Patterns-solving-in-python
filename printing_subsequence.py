def printingSubsequence(i,arr,emp,n):
    if(i >= n):
        print(emp)
        return

    # Take the index which means appending the index of arr to the new emp array
    emp.append(arr[i])
    printingSubsequence(i+1,arr,emp,n)
    emp.pop()

    # Not Taking the index which means not appending the index of arr to new emp array
    printingSubsequence(i+1,arr,emp,n)


arr = [3,1,2]
emp = []
n = len(arr)
index = 0

printingSubsequence(index,arr,emp,n)