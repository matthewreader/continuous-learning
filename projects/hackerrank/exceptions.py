if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        a, b = input().split()
        try:
            print(int(a) / int(b))
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")
