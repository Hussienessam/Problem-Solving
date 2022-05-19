import math

def get_difference1(chars):
    middle_char = chars[0]
    sum = 0
    for char in chars:
        if ord(char) >= ord(middle_char):
            sum += ord(char) - ord(middle_char)
        else:
            sum += ord(middle_char) - ord(char)
    return sum

def get_difference2(chars):
    middle_char = chars[3]
    sum = 0
    for char in chars:
        if ord(char) >= ord(middle_char):
            sum += ord(char) - ord(middle_char)
        else:
            sum += ord(middle_char) - ord(char)
    return sum

def get_difference3(chars):
    middle_char = chars[2]
    sum = 0
    for char in chars:
        if ord(char) >= ord(middle_char):
            sum += ord(char) - ord(middle_char)
        else:
            sum += ord(middle_char) - ord(char)
    return sum

def get_difference4(chars):
    middle_char = chars[0]
    sum = 0
    for char in chars:
        if ord(char) >= ord(middle_char):
            sum += ord(char) - ord(middle_char)
        else:
            sum += ord(middle_char) - ord(char)
    return sum

print(get_difference1(['a', 'z', 'b','c', 'o', 'z']))
print(get_difference2(['b', 'b', 'e','d', 'o', 'z']))
print(get_difference3(['b', 'a', 'f','u', 'o', 'z']))
print(get_difference3(['a', 'y','u']))

