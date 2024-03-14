lst = []
list_length = int(input("Enter length = "))
for i in range(list_length):
    num = int(input("Enter number = "))
    lst.append(num)
print(lst)

# Pre compute
hash_list = [0] * 13  # [0,0,0,0,0,0..13 times]
for num in lst:
    hash_list[num] += 1

print(hash_list)
n = int(input("Enter number to count = "))  # 1
print(hash_list[n])  # Fetch
