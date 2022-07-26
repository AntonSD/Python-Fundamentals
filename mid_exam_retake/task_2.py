genres = input().split(" | ")

line = input()

while line != "Stop!":

    command_args = line.split(" ")
    act = command_args[0]

    if act == "Join":
        genre = command_args[1]
        if genre not in genres:
            genres.append(genre)
    elif act == "Drop":
        genre = command_args[1]
        if genre in genres:
            genres.remove(genre)
    elif act == "Replace":
        genre = command_args[1]
        new_genre = command_args[2]
        if genre in genres:
            if new_genre not in genres:
                index = genres.index(genre)
                genres[index] = new_genre
    elif act == "Prefer":
        index1 = int(command_args[1])
        index2 = int(command_args[2])
        genres[index1], genres[index2] = genres[index2], genres[index1]

    line = input()

print(" ".join(genres))