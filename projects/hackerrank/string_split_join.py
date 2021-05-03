# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    word_list = line.split(" ")
    string_hyphen = "-".join(word_list)
    return string_hyphen


if __name__ == '__main__':
    print(split_and_join(line=input()))
