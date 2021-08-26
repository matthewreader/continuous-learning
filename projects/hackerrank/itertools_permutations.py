# Enter your code here. Read input from STDIN. Print output to STDOUT
# Takes a string and integer separated by a space and returns sorted
# permutations of length N.

from itertools import permutations

if __name__ == '__main__':
    input_string, input_int = input().split()
    permutations_list = list(permutations(input_string, int(input_int)))

    output_list = []
    for perm in permutations_list:
        output_list.append(''.join(perm))
    output_list.sort()

    for item in output_list:
        print(item)