import sys


def smallest_number(number):
    min_number = sys.maxsize
    for numbers in number:
        if numbers < min_number:
            min_number = numbers
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())
numbers = [first_number, second_number, third_number]
print(smallest_number(numbers))
