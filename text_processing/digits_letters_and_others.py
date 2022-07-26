text = input()
digits = ""
letters = ""
symbols = ""
for character in text:
    if character.isdigit():
        digits += character
    elif character.isupper() or character.islower():
        letters += character
    else:
        symbols += character
print(digits)
print(letters)
print(symbols)