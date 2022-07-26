text = input()

command = input()

while command != "Travel":
    command_params = command.split(":")
    if command_params[0] == "Add Stop":
        index = int(command_params[1])
        string = command_params[2]
        if index < len(text):
            text = text[:index] + string + text[index:]
        print(text)
    elif command_params[0] == "Remove Stop":
        start_index = int(command_params[1])
        end_index = int(command_params[2])
        if end_index < len(text):
            text = text[:start_index] + text[end_index + 1:]
        print(text)
    elif command_params[0] == "Switch":
        old_string = command_params[1]
        new_string = command_params[2]
        if old_string in text:
            text = text.replace(old_string, new_string)
        print(text)
    command = input()
print(f"Ready for world tour! Planned stops: {text}")