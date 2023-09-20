def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_prof = build_profile('hobby', 'math',
                             location='somewhere',
                             favourite_numbers=[42,21,7],
                             num_pets=3)