info = input()

new_dict = {}
counter_names = 0
while True:
    split_info = info.split("-")
    name = split_info[0]
    if split_info[0].isdigit():
        counter_names = int(name)
        break
    number = int(split_info[1])
    if name not in new_dict:
        new_dict[name] = number
    else:
        new_dict[name] = number

    info = input()

for num in range(counter_names):
    searched_name = input()
    if searched_name in new_dict.items():
        print(f"{searched_name} -> {number}")
    else:
        print(f"Contact {searched_name} does not exist.")