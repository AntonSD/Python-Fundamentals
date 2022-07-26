products_list = input().split("!")

command = input()

while command != "Go Shopping!":
    command_params = command.split(" ")
    to_do = command_params[0]
    if to_do == "Urgent":
        item = command_params[1]
        if item not in products_list:
            products_list.insert(0, item)
    elif to_do == "Unnecessary":
        item = command_params[1]
        if item in products_list:
            products_list.remove(item)
    elif to_do == "Correct":
        old_item = command_params[1]
        new_item = command_params[2]
        if old_item in products_list:
            index = products_list.index(old_item)
            products_list[index] = new_item

    elif to_do == "Rearrange":
        item = command_params[1]
        if item in products_list:
            moved_item = item
            products_list.remove(item)
            products_list.append(item)

    command = input()
print(", ".join(products_list))