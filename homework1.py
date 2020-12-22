car_brand = input('What is yours car? ')
car_model = input('What is yours car model? ')
car_color = input('What is your car color? ')
car_miles = input('What is the mileage of the your car? ')
car_doors = input('How many doors does it have?')
information = [car_brand,car_model,car_color,car_miles,car_doors]

print('Car Brand: {}\nCar Model: {}\nCar Color: {}\nCar Miles: {}\nCar Doors: {}'.format(information[0],information[1],information[2],information[3],information[4]))

print(type(car_brand))
print(type(car_model))
print(type(car_color))
print(type(car_miles))
print(type(car_doors))
