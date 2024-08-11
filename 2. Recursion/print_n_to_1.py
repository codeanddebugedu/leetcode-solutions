def printNumberWithBackTracking(num, i=0):
    # with back tracking
    if i > num:
        return
    printNumberWithBackTracking(num, i + 1)
    print(i)


def printNumberWithOutBackTracking(num, i=0):
    # with back tracking
    if i > num:
        return
    print(num - i)
    printNumberWithOutBackTracking(num, i + 1)


if __name__ == "__main__":
    n = int(input("Enter number : "))
    # cc = printNumberWithBackTracking(n)
    cc = printNumberWithOutBackTracking(n)
