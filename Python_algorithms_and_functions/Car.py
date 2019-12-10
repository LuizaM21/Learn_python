
class Car(object):
    def __init__(self, name, year_of_fabrication, engine_type, color, _number):
        self.car_name = name
        self.engine = engine_type
        self.year = year_of_fabrication
        self.car_color = color
        self.plate_number = _number

    # create alternative constructor of the class
    @classmethod
    def from_string(cls, car_string):
        car_name, engine, year, car_color, plate_number = car_string.split('_')
        return cls(car_name, engine, year, car_color, plate_number)

    def __str__(self):
        return {'Car name': self.car_name,
                'Car color': self.car_color,
                'Car engine type': self.engine,
                'Car year': str(self.year),
                'Car plate': self.plate_number}

    def _number(self):
        return self.plate_number


car = Car('Toyota', 1992, 'gasoline', 'blue', 'IS-21-AER')

car_str = 'Mazda_2006_gasoline_red_BC-45-SKY'
car_1 = Car.from_string(car_str)

print(car.__str__())
print(car_1.__str__())

'''--------------- implicit set and get methods------------------------'''
car.car_name = "Opel"
print('Car name: ' + car.car_name)

car.year_of_fabrication = 2005
print('Car year: ' + str(car.year_of_fabrication))

car.engine = 'diesel'
print('Car engine type: ' + car.engine)

car.car_color = 'black'
print('Car color: ' + car.car_color)
print('How many times this letters occurs in the string: ' + str(car.car_color.count('a')))
print('Changed car color: ' + car.car_color.replace('black', 'yellow'))
