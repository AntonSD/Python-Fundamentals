import re

text = input()

pattern = r"([=/])([A-Z][A-Za-z]{2,})\1"
matches = re.finditer(pattern, text)
cities = list()
points = 0
for match in matches:
    city = match[2]
    cities.append(city)
    points += len(city)

output_cities = ", ".join(cities)
print(f"Destinations: {output_cities}")
print(f"Travel Points: {points}")