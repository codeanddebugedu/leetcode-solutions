string = "aerrropllane"

char_hash = [0] * 26

# Pre store
for ch in string:
    index = ord(ch) - 97
    char_hash[index] += 1

print(char_hash)

char = input("Enter char to count = ")
print(char_hash[ord(char) - 97])
