size_of_side = float(input())
number_of_sheets = int(input())

total_size = size_of_side * size_of_side * 6
sum = 0
counter = 0
for sheet in range(number_of_sheets):
    counter += 1
    length = float(input())
    width = float(input())
    cover_of_sheet = length * width
    if counter % 3 == 0:
        if counter % 5 == 0:
            continue
        cover = cover_of_sheet * 0.75
        sum += cover
        continue
    elif counter % 5 == 0:
        continue
    else:
        sum += cover_of_sheet

area_covered = (sum / total_size) * 100
difference = 100 - area_covered
left_cover = (total_size / sum) * 100
diff_left_cover = 100 - left_cover
if total_size <= sum:
    print("You've covered the gift box!")
    print(f"{diff_left_cover:.2f}% wrap paper left.")
else:
    print("You are out of paper!")
    print(f"{difference:.2f}% of the box is not covered.")
