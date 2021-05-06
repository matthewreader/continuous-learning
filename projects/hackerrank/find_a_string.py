def count_substring(string, sub_string):
    """Print the number of times that the substring occurs in the given string. String traversal will take place
    from left to right, not from right to left.

    Parameters
    __________
    string : string
        The string to search
    sub_string : string
        The substring to search for in string
    """

    count = 0
    start = 0
    while True:
        start = string.find(sub_string, start) + 1
        if start > 0:
            count += 1
        else:
            return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
