current_users = ['hobbymath42', 'ted', 'Zach', 'kyle', 'chris']

current_users_lower = [user.lower() for user in current_users]

new_users = ['John', 'ZACH', 'stewie', 'james', 'brian']

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Username has already been used.")
    else:
        print("Username is available")