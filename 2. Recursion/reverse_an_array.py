def reverse_list(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end - 1)


if __name__ == "__main__":
    my_list = [3, 5, 1, 7, 8, 6, 5, 100]
    reverse_list(my_list, 0, len(my_list) - 1)
    print(my_list)
