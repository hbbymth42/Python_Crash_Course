print("Give me two numbers, and I'll add them!"+
      "(Enter 'q' at any time to quit)")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break

    try:
        print(int(first_number) + int(second_number))
    except ValueError:
        print("Please make sure both numbers are valid numbers!")