string = input()
com = input()

while com != "End":
    com = input().split(" ")
    command = com[0]

    if command == "Translate":
        char = com[1]
        repl = com[2]
        string = string.replace(char, repl)
        print(string)
    elif command == "Includes":
        char = com[1]
        if char in string:
            print('True')
        else:
            print('False')
    elif command == "Start":
        start = com[1]
        string.startswith(start)

    elif command == "Lowercase":
        string = string.lower()
        print(string)
    elif command == "FindIndex":
        char = com[1]
        print(string.rfind(char))
    elif command == "Remove":
        start = int(com[1])
        count = int(com[2])
        string.replace(string[start:start+count, ''])
        print(string)
    com = input()