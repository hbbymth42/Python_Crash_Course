print("Give me two numbers, and I'll add them!")

first_number = input("First number: ")
second_number = input("Second number: ")

try:
    print(int(first_number) + int(second_number))
except ValueError:
    print("Please make sure both numbers are valid numbers!")