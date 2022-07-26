text = input()

command = input()

while command != "End":
    command_params = command.split()
    action = command_params[0]
    if action == "Translate":
        old_string = command_params[1]
        new_string = command_params[2]
        text = text.replace(old_string, new_string)
        print(text)
    elif action == "Includes":
        include = command_params[1]
        if include in text:
            print(True)
        else:
            print(False)
    elif action == "Start":
        new_list = text.split()
        substring = command_params[1]
        needed_string = new_list.pop(0)
        if substring == needed_string:
            print(True)
        else:
            print(False)
    elif action == "Lowercase":
        text = text.lower()
        print(text)
    elif action == "FindIndex":
        char = command_params[1]
        index_of_char = text.rfind(char)
        print(index_of_char)
    elif action == "Remove":
        start_index = int(command_params[1])
        end_index = int(command_params[2])
        text = text[:start_index] + text[end_index+2:]
        print(text)

    command = input()