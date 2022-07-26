import re

text = input()
pattern = r"([#|])(?P<food>[A-Za-z]+)(\1)(?P<date>\d{2}/\d{2}\/\d{2})(\1)(?P<cal>\d+)(\1)"
result = re.finditer(pattern, text)
items = {}

total_calories = 0
daily_calories = 2000
for match in result:
    food = match.group("food")
    date = match.group("date")
    calories = match.group("cal")
    items[food][date] = calories
    total_calories += int(calories)
number_of_days = total_calories // daily_calories

print(f'You have food to last you for: {number_of_days} days!')
for food, date, calories in items.items():

    print(f"Item: {items[food]}, Best before: {date}, Nutrition: {calories}")

# for item in result:
#     current_item = [el for el in item if el != '']
#     items.append(current_item)
#     total_calories += int(current_item[2])

# for data in items:
#     product = data[0]
#     date = data[1]
#     calories = data[2]
#     print(f"Item: {product}, Best before: {date}, Nutrition: {calories}")