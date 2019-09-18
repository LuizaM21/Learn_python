

class Car(object):
    def __init__(self, name, year_of_fabrication, engine_type, color, _number):
        self.engine = engine_type
        self.car_name = name
        self.year = year_of_fabrication
        self.type_of_the_engine = engine_type
        self.color_of_the_car = color
        self.plate_number = _number

    def display_car_properties(self):
        return '{} {} {} {}'.format('\nCar name: ' + self.car_name + '',
                                    '\nCar color: ' + self.color_of_the_car + '',
                                    '\nCar engine type: ' + self.type_of_the_engine + '',
                                    '\nCar year: ' + str(self.year) + '\n')

    def _number(self):
        return self.plate_number


car = Car('Toyota', 1992, 'gasoline', 'blue')

print(car.display_car_properties())

'''--------------- implicit set and get methods------------------------'''
car.car_name = "Opel"
print('Car name: ' + car.car_name)

car.year_of_fabrication = 2005
print('Car year: ' + str(car.year_of_fabrication))

car.engine = 'diesel'
print('Car engine type: ' + car.engine)

car.color_of_the_car = 'black'
print('Car color: ' + car.color_of_the_car)
print('How many times this letters occurs in the string: ' + str(car.color_of_the_car.count('a')))
print('Changed car color: ' + car.color_of_the_car.replace('black', 'yellow'))




