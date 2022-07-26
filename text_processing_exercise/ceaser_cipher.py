text = input()
encrypted_text = []

for ch in text:
    ch_number = ord(ch)
    new_ch = ch_number + 3
    str_new_ch = chr(new_ch)
    encrypted_text.append(str_new_ch)
print("".join(encrypted_text))
