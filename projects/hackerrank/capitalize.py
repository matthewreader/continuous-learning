# string.title() does not work because of test case "1 w 2 r 3g"
# string.title will return "1 W 2 R 3G" and we want "1 W 2 R 3g"

def solve(name):
    for word in name.split():
        name = name.replace(word, word.capitalize())
    return name


if __name__ == '__main__':
    s = input()
    solve(s)
