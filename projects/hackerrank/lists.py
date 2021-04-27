# Initialize your list and read in the value of followed by lines of commands where each command will be of the
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(input())

    start_list = []
    for step in range(1, N + 1):
        command, *value = input().split()

        if command == "print":
            print(start_list)
        elif command == "insert":
            start_list.insert(int(value[0]), int(value[1]))
        elif command == "remove":
            start_list.remove(int(value[0]))
        elif command == "sort":
            start_list.sort()
        elif command == "reverse":
            start_list.reverse()
        elif command == "pop":
            start_list.pop()
        elif command == "append":
            start_list.append(int(value[0]))
        else:
            print("Unknown or unapproved command")
