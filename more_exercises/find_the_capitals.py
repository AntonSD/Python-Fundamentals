text = input()

counter = 0

searched_word = "Water"
searched_word2 = "Sand"
searched_word3 = "Fish"
searched_word4 = "Sun"

if searched_word in text:
    counter += 1
if searched_word2 in text:
    counter += 1
if searched_word3 in text:
    counter += 1
if searched_word4 in text:
    counter += 1
print(counter)