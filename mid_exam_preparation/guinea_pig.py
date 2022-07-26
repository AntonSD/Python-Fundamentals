quantity_of_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
pigs_weight = float(input())

food_grams = quantity_of_food * 1000
hay_grams = quantity_hay * 1000
cover_grams = quantity_cover * 1000
pigs_grams = pigs_weight * 1000
counter = 0
enough = True
while counter < 30:
    counter += 1
    food_grams -= 300
    if food_grams < 0:
        not_enough = False
        break
    if counter % 2 == 0:
        needed_hay = 0.05 * food_grams
        hay_grams -= needed_hay
        if hay_grams < 0:
            not_enough = False
            break
    if counter % 3 == 0:
        needed_cover = pigs_grams / 3
        cover_grams -= needed_cover
        if cover_grams < 0:
            not_enough = False
            break
food = float(food_grams / 1000)
hay = float(hay_grams / 1000)
cover = float(cover_grams / 1000)
if food > 0 and hay > 0 and cover > 0:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print("Merry must go to the pet store!")
