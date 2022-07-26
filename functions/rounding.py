base_list = input().split()
new_list = []

for n in base_list:
    round_number = round(float(n))
    new_list.append(round_number)
print(new_list)