# You are given a positive integer N (1-9). Print a numerical triangle of height N -1
# Use only arithmetic operations, a single loop and print statement.

for i in range(1, int(input())):  # More than 2 lines will result in 0 score. Do not leave a blank line also
    print((10 ** i // 9) * i)
