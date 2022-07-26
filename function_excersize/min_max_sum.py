list_of_numbers = input().split()
list_as_digits = []
for number in list_of_numbers:
    list_as_digits.append(int(number))

print(f"The minimum number is {min(list_as_digits)}")
print(f"The maximum number is {max(list_as_digits)}")
print(f"The sum number is: {sum(list_as_digits)}")

