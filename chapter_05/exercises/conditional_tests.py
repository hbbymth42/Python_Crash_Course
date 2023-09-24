car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

numWheels = 4

print("\nDo cars have 4 wheels? I predict True.")
print(numWheels == 4)

print("\nDo cars have more than or less than 4 wheels? I predict False.")
print(numWheels > 4 or numWheels < 4)

print("\nIs car == 'subaru' and has 4 wheels? I predict True.")
print(car == 'subaru' and numWheels == 4)

print("\nIs car == 'audi' and has 4 wheels? I predict False.")
print(car == 'audi' and numWheels == 4)

print("\nIs car == 'subaru' and has more than 4 wheels? I predict False.")
print(car == 'subaru' and numWheels > 4)

print("\nIs car == 'audi' or has 4 wheels? I predict True")
print(car == 'audi' or numWheels == 4)