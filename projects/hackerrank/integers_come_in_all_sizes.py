# Read four numbers, a, b, c, and d, and print the result of a**b + c**d.

if __name__ == '__main__':
    input_list = []
    for _ in range(0, 4):
        number_in = int(input())
        input_list.append(number_in)

    print((input_list[0] ** input_list[1]) + (input_list[2] ** input_list[3]))
