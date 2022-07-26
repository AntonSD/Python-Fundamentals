current_year = int(input())

while True:
    current_year += 1
    current_year_as_str = str(current_year)
    if len(current_year_as_str) == len(set(current_year_as_str)):
        print(current_year_as_str)
        break
