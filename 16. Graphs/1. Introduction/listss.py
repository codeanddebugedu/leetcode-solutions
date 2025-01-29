connections = [[2, 1], [1, 3], [2, 4], [3, 4], [2, 5], [4, 5]]
n = 5

lst = [[] for _ in range(n + 1)]

for n1, n2 in connections:
    lst[n1].append(n2)
    lst[n2].append(n1)

print(lst)
