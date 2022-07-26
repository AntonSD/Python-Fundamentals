energy = int(input())

command = input()
counter = 0
is_winner = True
while command != "End of battle":
    distance = int(command)

    if energy - distance >= 0:
        energy -= distance
        counter += 1
        if counter % 3 == 0:
            energy += counter
    else:
        is_winner = False
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break

    command = input()

if is_winner:
    print(f"Won battles: {counter}. Energy left: {energy}")
