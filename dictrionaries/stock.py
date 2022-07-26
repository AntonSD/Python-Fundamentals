data = input().split()
search_data = input().split()

bakery = dict()

for i in range(0, len(data), 2):
    product = data[i]
    quantity = data[i + 1]
    bakery[product] = quantity

for search_term in search_data:
    if search_term in bakery:
        print(f"We have {bakery[search_term]} of {search_term} left")
    else:
        print(f"Sorry, we don't have {search_term}")