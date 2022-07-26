start = int(input())
end = int(input())
for char in range(start, end + 1):
    ascii = chr(start)
    start += 1
    print(f"{ascii} ", end="")