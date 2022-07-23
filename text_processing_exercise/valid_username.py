def lenght(username):
    if 3 <= len(username) <= 16:
        return True
    return False


def type_of_symbols(username):
    for character in username:
        if not(character.isalnum() or character == '-' or character == "-"):
            return False
    return True


def redudant(username):
    for character in username:
        if character == " ":
            return False
    return True

def username_is_valid(username):
    if lenght(username) and type_of_symbols(username) and redudant(username):
        return True
    return False

usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)