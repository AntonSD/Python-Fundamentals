import re

patter = '\d+'
line = input()
while True:
    if line:
        match = re.findall(patter, line)
        if match:
            print(" ".join(match), end=" ")
        line = input()
    else:
        break