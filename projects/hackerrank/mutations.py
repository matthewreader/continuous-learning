def mutate_string(string, position, character):
    """Replaces a character in a string with a new character at a given position

    Parameters
    __________
    string : string
        The string to change
    position : int
        The index of the character to be changed
    character : string
        The character to insert
    """

    string_list = list(string)
    string_list[position] = character
    string_return = ''.join(string_list)
    return string_return


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
