def convert2Binary(num: int) -> str:
    result = ""
    while num > 0:
        if num % 2 == 1:
            result += "1"
        else:
            result += "0"
        num = num // 2
    return result[::-1]


print(convert2Binary(13))
