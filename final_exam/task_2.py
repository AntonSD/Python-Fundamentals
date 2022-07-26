import re

text = input()

patterns = r"[@#]([a-z]{2,})[@#]([~`!@#$%^&*()/,.\?/-=]+)(\/+)(\d+)(\/+)"
matches = re.finditer(patterns, text)

for match in matches:
    color = match.group(1)
    number = match.group(4)
    print(f"You found {number} {color} eggs!")