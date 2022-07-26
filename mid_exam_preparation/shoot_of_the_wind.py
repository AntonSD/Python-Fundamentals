targets = input().split(" ")
targets = list(map(int, targets))
command = input()
counter = 0
while command != "End":
    index = int(command)
    if index < len(targets):
        counter += 1

        for num in range(len(targets)):
            if 0 < targets[num] < targets[index]:
                targets[num] += targets[index]

            elif 0 < targets[num] >= targets[index]:
                targets[num] -= targets[index]
        targets[index] = -1
    command = input()
output = list(map(str, targets))
print(f"Shot targets: {counter} -> {' '.join(output)}")