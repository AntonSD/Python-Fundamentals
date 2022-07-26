message = input()

while True:
    command_input = input()

    if command_input == "Reveal":
        break
    command_args = command_input.split(":|:")
    command_name = command_args[0]

    if command_name == "InsertSpace":
        index = int(command_args[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif command_name == "Reverse":
        substr = command_args[1]
        old_message = message
        message = message.replace(substr, "", 1)
        if old_message == message:
            print("error")
            continue
        a = list(substr)
        a.reverse()
        substr_reversed = "".join(a)
        message += substr_reversed
        print(message)
    elif command_name == "ChangeAll":
        substr = command_args[1]
        replacement = command_args[2]
        message = message.replace(substr, replacement)
        print(message)
print(f"You have a new text message: {message}")
