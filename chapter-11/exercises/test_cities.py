from city_functions import city_country

def test_city_country():
    formatted_string = city_country('santiago', 'chile', 5000000)
    assert formatted_string == 'Santiago, Chile - population 5000000'