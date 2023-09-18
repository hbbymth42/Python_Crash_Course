favourite_places = {
    'hobbymath42': ['sardinia, italy', 'nicoya peninsula, costa rica', 'icaria, greece'],
    'gallaheg': ['berlin, germany','Amsterdam, netherlands'],
    'koolaidabeast': ['okinawa, japan'],
}

for name, places in favourite_places.items():
    print(f"\n{name.title()}'s favourite places:")
    for place in places:
        print(f"- {place.title()}")