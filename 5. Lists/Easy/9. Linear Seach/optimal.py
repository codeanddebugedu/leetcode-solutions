#This is a linear uptodate search code with time complexity o(n) 
# :')

def linearSearch(n: int, num: int, arr: [int]) -> int:
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
    return -1
