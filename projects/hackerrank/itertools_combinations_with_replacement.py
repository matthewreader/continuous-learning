# Enter your code here. Read input from STDIN. Print output to STDOUT
# Your task is to print all possible size k replacement combinations of
# the string in lexicographic sorted order.

from itertools import combinations_with_replacement

if __name__ == '__main__':
    input_string, input_int = input().split()
    sorted_string = sorted(input_string)
    combinations_list = []
    combinations_list.extend(list(combinations_with_replacement(sorted_string, int(input_int))))

    output_list = []
    for perm in combinations_list:
        output_list.append(''.join(perm))
    output_list.sort()
    output_list.sort(key=len, reverse=False)

    for item in output_list:
        print(item)
