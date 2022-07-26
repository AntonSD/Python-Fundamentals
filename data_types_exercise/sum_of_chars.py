number_of_letters = int(input())
sumo_of_ascii_values = 0

for character in range(number_of_letters):
    next_character = input()
    sumo_of_ascii_values += ord(next_character)
print(f"The sum equals: {sumo_of_ascii_values}")
