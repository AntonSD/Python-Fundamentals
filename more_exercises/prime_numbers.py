number = int(input())

if number > 1:
    for i in range(2, number + 1):
        if (number % i) == 0:
            print("False")
        else:
            print("True")

