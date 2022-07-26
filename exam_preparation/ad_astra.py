import re

text = input()
pattern = r"([|#])([A-Z][a-z]+( [A-Z]?[a-z]+)?)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
matches = re.finditer(pattern, text)
cal = []
cal_pattern = r"([|#])(\d+)\1"
cal_match = re.finditer(cal_pattern, text)
for cals in cal_match:
    calo = cals.group(2)
    cal.append(int(calo))
all_cal = sum(cal)
days = all_cal // 2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    food = match.group(2)
    date = match.group(4)
    calories = match.group(5)
    print(f"Item: {food}, Best before: {date}, Nutrition: {calories}")