import re

some_string = input()
patttern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(patttern, some_string)
print(",".join(matches))