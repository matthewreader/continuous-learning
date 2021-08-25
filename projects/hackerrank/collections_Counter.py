# Enter your code here. Read input from STDIN. Print output to STDOUT
# Create a collection of shoes and calculate sales only if that shoe is in stock
# for the size requested.  Exercise should focus on using collections module.
from collections import Counter

if __name__ == '__main__':
    number_of_shoes = int(input())
    inventory_counter = Counter(list(map(int, input().split())))
    number_of_customers = int(input())

    total_sales = 0
    for customer in range(number_of_customers):
        size_request, price = map(int, input().split())

        if size_request in inventory_counter:
            total_sales += int(price)
            inventory_counter -= Counter([size_request])

    print(total_sales)
