import re

some_string = input().lower()
searched_word = input().lower()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, some_string)
print(len(matches))