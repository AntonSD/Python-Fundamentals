list_of_numbers = input().split(', ')
list_of_digits = []
for number in list_of_numbers:
    if number == number[::-1]:
        print(True)
    else:
        print(False)