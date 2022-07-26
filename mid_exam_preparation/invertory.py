inventory = input().split(", ")

command = input()

while command != "Craft!":
    command_args = command.split(" - ")
    act = command_args[0]
    if act == "Collect":
        item = command_args[1]
        if item in inventory:
            continue
        else:
            inventory.append(item)
    elif act == "Drop":
        item = command_args[1]
        if item in inventory:
            inventory.remove(item)
    elif act == "Combine Items":
        new_items = command_args[1].split(":")
        old_item = new_items[0]
        new_item = new_items[1]
        for i in range(len(inventory)):
            if inventory[i] == old_item:
                inventory.insert(i + 1, new_item)
                break
    elif act == "Renew":
        item = command_args[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input()
print(", ".join(inventory))
