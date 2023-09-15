numbers = [number for number in range(1, 10)]

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    else:
        print(f"{number}th")