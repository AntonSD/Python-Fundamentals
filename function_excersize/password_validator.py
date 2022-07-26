def long(password):
    if len(password) > 6 and len(password) < 10:
        return True
    else:
        return False
def characters(password):
    for character in password:

password = input()
