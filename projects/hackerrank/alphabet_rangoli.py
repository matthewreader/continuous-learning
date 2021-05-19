# Solution from discussion.  Really clever once you work through it.

import string
alpha = string.ascii_lowercase


def print_rangoli(size):
    # your code goes here
    rangoli = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        rangoli.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
    print('\n'.join(rangoli[:0:-1] + rangoli))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)