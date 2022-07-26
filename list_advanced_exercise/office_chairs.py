number_of_rooms = int(input())
number_of_chairs = 0
needed_chairs = 0
not_enough_chairs_rooms = []
needed_chairs_list = []
for room in range(1, number_of_rooms + 1):
    info = input().split()
    number_chair = len(info[0])
    visitors = int(info[1])
    if number_chair < visitors:
        not_enough_chairs_rooms.append(room)
        more_chairs = visitors - number_chair
        needed_chairs_list.append(more_chairs)
    number_of_chairs += len(info[0])
    needed_chairs += int(info[1])

difference = abs(number_of_chairs - needed_chairs)
if number_of_chairs >= needed_chairs:
    print(f"Game On, {difference} free chairs left")
else:
    for r in range(len(not_enough_chairs_rooms)):
        print(f"{needed_chairs_list[r]} more chairs needed in room {not_enough_chairs_rooms[r]}")

