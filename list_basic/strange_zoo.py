tail = input()
body = input()
head = input()

meerkat = [tail, body, head]
temp = meerkat[0]
meerkat[0] = meerkat[2]
meerkat[2] = temp

print(meerkat)