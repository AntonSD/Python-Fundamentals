text = input()

while True:
    command = input()

    if command == "Generate":
        break

    command_args = command.split(">>>")
    commandings = command_args[0]
    if commandings == "Contains":
        substr = command_args[1]
        if substr in text:
            print(f"{text} contains {substr}")
        else:
            print("Substring not found!")
    elif commandings == "Flip":
        uplow = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        needed_str = text[start_index:end_index]
        if uplow == "Upper":
            needed_str = needed_str.upper()
        elif uplow == "Lower":
            needed_str = needed_str.lower()
        text = text[:start_index] + needed_str + text[end_index:]
        print(text)
    elif commandings == "Slice":
        start_slicing = int(command_args[1])
        end_slicing = int(command_args[2])
        text = text[:start_slicing] + text[end_slicing:]
        print(text)

print(f"Your activation key is: {text}")