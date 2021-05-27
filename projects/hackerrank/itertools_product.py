from itertools import product


def cartesian_product(a=input().split(), b=input().split()):
    """Compute cartesian product of two space separated elements A and B"""
    a = list(map(int, a))
    b = list(map(int, b))
    print(*product(a, b))


if __name__ == '__main__':
    cartesian_product()
