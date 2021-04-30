# You are given a string and your task is to swap cases. In other words, convert all lowercase letters
# to uppercase letters and vice versa.

def swap_case(input_string):
    new_string = ''
    for character in input_string:
        if character == character.upper():
            new_string += character.lower()
        elif character == character.lower():
            new_string += character.upper()
        else:
            new_string += character
    return new_string


if __name__ == '__main__':
    s = input()
    print(swap_case(s))
