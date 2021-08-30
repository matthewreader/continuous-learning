# Enter your code here. Read input from STDIN. Print output to STDOUT
# Takes a string and integer separated by a space and returns sorted
# combinations of length N.

from itertools import combinations

if __name__ == '__main__':
    input_string, input_int = input().split()
    sorted_string = sorted(input_string)
    combinations_list = []
    for i in range(int(input_int)):
        combinations_list.extend(list(combinations(sorted_string, i+1)))

    output_list = []
    for perm in combinations_list:
        output_list.append(''.join(perm))
    output_list.sort()
    output_list.sort(key=len, reverse=False)

    for item in output_list:
        print(item)
