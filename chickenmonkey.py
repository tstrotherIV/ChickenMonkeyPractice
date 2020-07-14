numbers = range(100)


for n in numbers:
    if n % 5 == 0 and n % 7 == 0:
        print("ChickenMonkey")
    elif n % 5 == 0:
        print("chicken")
    elif n % 7 == 0:
        print("monkey")
    else:
        print(n)
