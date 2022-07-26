number_of_electrons = int(input())
counter = 0
shells = []

for shell in range(1, number_of_electrons + 1):
    new_shell = 2 * (shell ** 2)
    if counter + new_shell > number_of_electrons or new_shell > number_of_electrons:
        difference = abs(number_of_electrons - counter)
        shells.append(difference)
        break
    counter += new_shell
    shells.append(new_shell)
    if counter == number_of_electrons:
        break
print(shells)
