text = input()
filtered_letter = ""
last_letter = ''

for current_letter in text:
    if current_letter != last_letter:
        filtered_letter += current_letter
        last_letter = current_letter
print(filtered_letter)