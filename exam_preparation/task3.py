count = int(input())
heroes = dict()
for i in range(count):
    current_hero = input().split()
    hero_name = current_hero[0]
    hero_hp = int(current_hero[1])
    hero_mp = int(current_hero[2])
    current_hero_dict = dict()
    current_hero_dict["HP"] = hero_hp
    current_hero_dict["MP"] = hero_mp
    heroes[hero_name] = current_hero_dict

command = input()

while command != "End":
    command_params = command.split(" - ")
    command_name = command_params[0]
    hero_name = command_params[1]
    value = int(command_params[2])

    if command_name == "Heal":
        if heroes[hero_name]["HP"] + value > 100:
            value = 100 - heroes[hero_name]["HP"]
            heroes[hero_name]["HP"] = 100
        else:
            heroes[hero_name]["HP"] += value
        print(f"{hero_name} healed for {value} HP!")
    elif command_name == "Recharge":
        if heroes[hero_name]["MP"] + value > 200:
            value = 200 - heroes[hero_name]["HP"]
            heroes[hero_name]["HP"] = 200
        else:
            heroes[hero_name]["MP"] += value
        print(f"{hero_name} recharged for {value} MP!")
    elif command_name == "TakeDamage":
        attacker = command_params[3]
        heroes[hero_name]["HP"] -= value
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif command_name == "CastSpell":
        spell = command_params[3]
        if heroes[hero_name]["MP"] >= value:
            heroes[hero_name]["MP"] -= value
            print(f"{hero_name} successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")

    command = input()

for hero in heroes:
    print(f"{hero}")
    print(f"  HP: {heroes[hero]['HP']}")
    print(f"  MP: {heroes[hero]['MP']}")