from random import randint

lottery_vals = (1,6,34,23,83,17,48,3,78,8,'z','a','b','y','c')

attempt_number = 0

while True:
    attempt_number += 1

    lottery_list = []
    my_ticket = []

    while len(lottery_list) < 4:
        lottery_list.append(lottery_vals[randint(0,len(lottery_vals)-1)])
    
    while len(my_ticket) < 4:
        my_ticket.append(lottery_vals[randint(0,len(lottery_vals)-1)])
    
    if my_ticket == lottery_list:
        break

print(f"It took {attempt_number} attempts to get the winning ticket.")