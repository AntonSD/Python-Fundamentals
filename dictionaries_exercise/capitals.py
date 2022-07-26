countries = input().split(", ")
cities = input().split(", ")

new_dict = zip(countries, cities)

for key, value in new_dict:
    print(f"{key} -> {value}")