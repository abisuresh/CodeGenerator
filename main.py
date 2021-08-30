import random
import string


def check_invalid_string(value):
    return any(char.isdigit() for char in value)


def encode_string(str_value):
    count = 0
    new_string = ""
    for i in str_value:
        letter = random.choice(string.ascii_letters)
        new_string = new_string + letter
        count = count + 1

    return new_string


val = input("Enter a string\n")

while check_invalid_string(val):
    print("Please input a string with only alpha characters.")
    val = input("Enter a string\n")

result = encode_string(val)

print("Encoded string: " + str(result))




