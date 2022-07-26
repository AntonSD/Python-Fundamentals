number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmets = number_of_lost_fights // 2
total_swords = number_of_lost_fights // 3
total_shields = number_of_lost_fights // 6
total_armor = total_shields // 2
total_money = total_helmets * helmet_price + total_swords * sword_price + total_shields * shield_price + total_armor * armor_price
print(f"Gladiator expenses: {total_money:.2f} aureus")