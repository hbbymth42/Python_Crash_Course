def make_car(manufacturer, model, **car):
    car['manufacturer'] = manufacturer
    car['model'] = model
    return car

car = make_car('ford', 'falcon', turbo=True, v8=True, year=1998)
print(car)