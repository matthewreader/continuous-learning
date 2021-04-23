# Find the second highest number in an input list of integers.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = list(arr)

    # Case for when all scores are the same
    if max(arr_list) == min(arr_list):
        print(max(arr_list))
    # Case where there are at least two unique scores
    else:
        print(max([num for num in arr_list if num != max(arr_list)]))
