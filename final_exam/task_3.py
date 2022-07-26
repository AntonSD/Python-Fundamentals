import collections

text = input().split(" | ")
words = collections.defaultdict(list)

for searched_word in text:
    word_split = searched_word.split(": ")
    word = word_split[0]
    definition = word_split[1]
    new_list = definition
    words[word].append(new_list)

needed_words = input().split(" | ")

command = input()
new = []
if command == "Hand Over":
    print(" ".join(words.keys()))

elif command == "Test":
    for w in needed_words:
        if w in words.keys():
            for key, value in sorted(words.items()):
                print(f"{w}:")
                for v in words[key]:
                    print(f" -{v}")


