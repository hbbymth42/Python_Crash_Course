from random import randint

lottery_vals = (1,6,34,23,83,17,48,3,78,8,'z','a','b','y','c')

lottery_list = []

while len(lottery_list) < 4:
    lottery_list.append(lottery_vals[randint(0,len(lottery_vals)-1)])

print(f"Tickets matching these 4 numbers/letters wins a prize: {lottery_list}")