my_char = {}
word = input()

for ch in word:
    if ch not in my_char:
        my_char[ch] = 1
    else:
        my_char[ch] += 1
for key, value in my_char.items():
    if key != " ":
        print(f"{key} -> {value}")
