# You are given a string and width .
# Your task is to wrap the string into a paragraph of width .
# More an exercise of using textwrap than coming up with my own solution.

import textwrap


def wrap(string, max_width):
    return "\n".join(textwrap.wrap(text=string, width=max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
