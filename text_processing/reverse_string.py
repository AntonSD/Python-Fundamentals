word = input()

while word != "end":
    rev = reversed(word)
    reversed_word = "".join(rev)
    print(f"{word} = {reversed_word}")

    word = input()