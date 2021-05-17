# Mat size must be N x M. (N is an odd natural number, and is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Enter your code here. Read input from STDIN. Print output to STDOUT

def designer_door_mat(height, width):
    pattern = [('.|.' * (2 * i + 1)).center(width, '-') for i in range(height // 2)]
    print('\n'.join(pattern + ['WELCOME'.center(width, '-')] + pattern[::-1]))


if __name__ == '__main__':
    n, m = map(int, input().split())
    designer_door_mat(n, m)
