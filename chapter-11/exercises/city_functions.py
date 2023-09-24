def city_country(city, country, population=''):
    if population:
        formatted_city_country = f"{city.title()}, {country.title()}" + \
        f" - population {population}"
    else:
        formatted_city_country = f"{city}, {country}"
    return formatted_city_country