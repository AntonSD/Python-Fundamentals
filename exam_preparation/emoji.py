import re

text = input()
pattern = r"(:{2}|\*{2})(?P<emoji>[A-Z][a-z]{2,})\1"
matches = re.finditer(pattern, text)
numbers = []
pattern_for_numbers = r"\d"
matches_for_number = re.findall(pattern_for_numbers, text)
cool_score = 1
emojies = []
cointer = 0
for num in matches_for_number:
    cool_score *= int(num)
for match in matches:
    cointer += 1
    separator = match.group(1)
    emoji = match.group(2)
    score_of_emoji = 0
    for ch in emoji:
        score_of_emoji += ord(ch)
    new_emoji = separator + emoji + separator
    emojies.append(new_emoji)
print(f"Cool threshold: {cool_score}")
print(f"{cointer} emojis found in the text.")
print("The cool ones are:")
for emojie in emojies:
    print(emojie)