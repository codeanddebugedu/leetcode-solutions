#This is a linear search code with time complexity o(n) 
# :')
#this is new.git stsuts
def linearSearch(n: int, num: int, arr: [int]) -> int:
    for i in range(0, len(arr)):
        if arr[i] == num:
            return i
    return -1
