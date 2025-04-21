def reverse_list(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end - 1)


# Alternate Method using just one Index
def revAr(arr, ind):
    n = len(arr)
    if ind == n // 2:
        print(arr)
        return
    arr[ind], arr[n - 1 - ind] = arr[n - 1 - ind], arr[ind]
    revAr(arr, ind + 1)


if __name__ == "__main__":
    my_list = [3, 5, 1, 7, 8, 6, 5, 100]
    reverse_list(my_list, 0, len(my_list) - 1)
    print(my_list)

    new_list = [3, 5, 1, 7, 8, 6, 5, 100]
    revAr(new_list, 0)
