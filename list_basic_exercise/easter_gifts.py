command = input().split()
not_gifts = []
bought_gifts = []
temp_list = []
removing_word = "OutOfStock"
final_list = []
replacing_word = "Required"
while command != "No Money":
    temp_list.append(command)
    for element in temp_list:
        if removing_word == temp_list[0]:
            if temp_list[1] in temp_list:
                temp_list[1] = "None"
        if replacing_word in temp_list:
            number = temp_list[2]
            if 0 <= number < len(final_list):
                final_list.append[number] = temp_list[1]

        temp_list = []
    command = input().split()
print(final_list)
