number_of_plants = int(input())
plants = {}

for _ in range(number_of_plants):
    data = input().split("<->")
    plant = data[0]
    rarity = int(data[1])
    plants[plant] = {'rarity': int(rarity), 'ratings': []}

command = input()
while command != "Exhibition":
    command_params = command.split(": ")
    action = command_params[0]
    value = command_params[1]
    if action == "Rate":
        plant, rating = value.split(" - ")
        plants[plant]['ratings'].append(float(rating))
    elif action == "Update":
        plant, rarity = value.split(" - ")
        plants[plant]['rarity'] = int(rarity)
    elif action == "Reset":
        plant = value
        plants[plant]['ratings'].clear()

    command = input()
print("Plants for the exhibition:")
for plant, value in plants.items():
    if value['ratings']:
        avg = sum(value['ratings']) / len(value['ratings'])
    else:
        avg = 0
    plants[plant]['avg'] = avg
    print(f"{plant}; Rarity: {plants[plant]['rarity']}; {avg:.2f}")