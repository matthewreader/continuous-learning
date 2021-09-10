# Exercise in using set.add() to add new entries to a set from STDIN.

if __name__ == '__main__':
    s = set()
    for i in range(int(input())):
        s.add(input())
    print(len(s))
