def binary_to_decimal(binary_string):
    decimal_number = 0
    power = 0

    index = len(binary_string) - 1

    while index >= 0:
        bit = int(binary_string[index])
        decimal_number += bit * (2**power)
        power += 1
        index -= 1

    return decimal_number


binary_string = "1101"
decimal_representation = binary_to_decimal(binary_string)
print(f"The decimal representation of {binary_string} is {decimal_representation}")
