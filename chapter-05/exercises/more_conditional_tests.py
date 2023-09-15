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

print("\nIs car == 'audi' or has 4 wheels? I predict True.")
print(car == 'audi' or numWheels == 4)


print("\nGood News! We have got more cars!")

cars = ['subaru', 'toyota', 'honda', 'nissan']

print("\nIs the first car a toyota? I predict False.")
print(cars[0] == 'toyota')

print("\nIs the first car not an audi? I predict True.")
print(cars[0] != 'audi')

print("\nIs the second car a ford? I predict False.")
print(cars[1].lower() == 'ford')

print("\nIs the second car a toyota? I predict True.")
print(cars[1].lower() == 'toyota')

print("\nIs the number of cars greater than 6? I predict False")
print(len(cars) > 6)

print("\nIs the number of cars less than 6? I predict True.")
print(len(cars) < 5)

print("\nIs the number of cars less than or equal to 3? I predict False.")
print(len(cars) <= 3)

print("\nIs the number of cars greater than or equal to 3? I predict True.")
print(len(cars) >= 3)

print("\nAre there 5 cars? I predict False.")
print(len(cars) == 5)

print("\nAre there not 5 cars? I predict True.")
print(len(cars) != 5)

print("\nAre there not 4 cars? I predict False.")
print(len(cars) != 4)

print("\nAre there 4 cars? I predict True.")
print(len(cars) == 4)

print("\nAre the number of cars greater than 2 and equal to 3? I predict False.")
print(len(cars) > 2 and len(cars) == 3)

print("\nAre the number of cars greater than 3 and equal to 4? I predict True.")
print(len(cars) > 3 and len(cars) == 4)

print("\nIs the first car a honda or a nissan? I predict False")
print(cars[0] == 'honda' or cars[0] == 'nissan')

print("\nIs the third car a honda or a nissan? I predict True.")
print(cars[2] == 'honda' or cars[2] == 'nissan')

print("\nIs a nissan not in the list? I predict False.")
print('nissan' not in cars)

print("\nIs a ford not in the list? I predict True.")
print('ford' not in cars)

print("\nIs a holden in the list? I predict False.")
print('holden' in cars)

print("\nIs a nissan in the list? I predict True.")
print('nissan' in cars)