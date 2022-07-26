number_of_days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
counter = 0
for day in range(number_of_days):
    counter += 1
    daily_plunder = 40
    if counter % 3 == 0:
        daily_plunder += 0.5 * daily_plunder
    total_plunder += daily_plunder
    if counter % 5 == 0:
        total_plunder *= 0.7
difference = abs(expected_plunder - total_plunder)

percentage = (total_plunder / expected_plunder) * 100
if expected_plunder <= total_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {percentage:.2f}% of the plunder.")