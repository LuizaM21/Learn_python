"""Abstract Factory is a creational design pattern, which solves the problem
of creating entire product families without specifying their concrete classes.
In other words, creates an instance of several families of classes"""


from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, numbers_of_doors, plate_number, no_of_pistons, engine_type, horse_power):
        self.numbers_of_doors = numbers_of_doors
        self.plate_number = plate_number
        self.no_of_pistons = no_of_pistons
        self.engine_type = engine_type
        self.horse_power = horse_power

    @abstractmethod
    def create_doors(self):
        print('Call Car abstract class create_doors')
        pass

    @abstractmethod
    def display_plate_number(self):
        pass

    @abstractmethod
    def create_car_engine(self):
        pass


class SportCar(Car):

    def _init__(self, numbers_of_doors, plate_number, no_of_pistons, engine_type, horse_power, is_sport=False):
        self.numbers_of_doors = numbers_of_doors
        self.plate_number = plate_number
        self.no_of_pistons = no_of_pistons
        self.engine_type = engine_type
        self.horse_power = horse_power
        self.is_sport = is_sport

        super().__init__(numbers_of_doors, plate_number, no_of_pistons, engine_type, horse_power)

    def create_doors(self):
        return self.numbers_of_doors

    def display_plate_number(self):
        return str(self.plate_number)

    def create_car_engine(self):
        return {'number of pistons': self.no_of_pistons,
                'engine type': self.engine_type,
                'horse power': self.horse_power}

    def __str__(self):
        return f'number of doors: {self.numbers_of_doors}\n' \
               f'plate number: {self.plate_number}\n' \
               f'number of pistons: {self.no_of_pistons}\n' \
               f'engine type: {self.engine_type}\n' \
               f'horse power: {self.horse_power}\n'


if __name__ == '__main__':
    audi_tt = SportCar(3, 'IS-91-AER', 6, 'DIESEL', 107, True)
    print(audi_tt)
    print(audi_tt.create_doors())
    print(audi_tt.display_plate_number())
    print(audi_tt.create_car_engine())


