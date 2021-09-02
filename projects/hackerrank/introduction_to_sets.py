def average(array):
    # your code goes here
    """
    Args:
        array: An array of space separated integers from STDIN
    Returns:
        float: The average of unique integers from array.
    """
    unique_ints = set(array)
    return sum(unique_ints) / len(unique_ints)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)