import re

pattern = r"((www)\.([A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+))"
some_sentence = input()
valid_urls = list()
while some_sentence:
    matches = re.finditer(pattern, some_sentence)
    for match in matches:
        valid_urls.append(match.group(1))

    some_sentence = input()
for valid_url in valid_urls:
    print(valid_url)