command = input()
cities = dict()

while command != "Sail":
    city_params = command.split("||")
    city = city_params[0]
    population = int(city_params[1])
    gold = int(city_params[2])
    if city in cities:
        cities[city]["population"] += population
        cities[city]["gold"] += gold
    else:
        current_city_dict = dict()
        current_city_dict["population"] = population
        current_city_dict["gold"] = gold
        cities[city] = current_city_dict

    command = input()

new_command = input()

while new_command != "End":
    new_command_params = new_command.split("=>")
    action = new_command_params[0]
    city = new_command_params[1]
    if action == "Plunder":
        killed_citizen = int(new_command_params[2])
        taken_gold = int(new_command_params[3])
        if cities[city]["gold"] - taken_gold <= 0 or cities[city]["population"] - killed_citizen <= 0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")
        else:
            cities[city]["gold"] -= taken_gold
            cities[city]["population"] -= killed_citizen
            print(f"{city} plundered! {taken_gold} gold stolen, {killed_citizen} citizens killed.")
    if action == "Prosper":
        given_gold = int(new_command_params[2])
        if given_gold < 0:
            print("Gold added cannot be a negative number!")

        else:
            cities[city]["gold"] += given_gold
            print(f"{given_gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    new_command = input()
print(f"Ahoy, Captain! There are {len(cities.keys())} wealthy settlements to go to:")
for town in cities:
    print(f'{town} -> Population: {cities[town]["population"]} citizens, Gold: {cities[town]["gold"]} kg')
