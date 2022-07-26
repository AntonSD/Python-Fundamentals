def sum_numbers(first, second):
    return first + second


def sub_numbers(sum, third):
    return sum - third


first_number = int(input())
second_number = int(input())
third_number = int(input())
sum_of_first_digits = sum_numbers(first_number, second_number)
result = sub_numbers(sum_of_first_digits, third_number)
print(result)