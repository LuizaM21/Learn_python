"""Practice with classes, instances and __init__.

Creates Car objects in a loop and with a list comprehension,
and converts each object into a dictionary with vars().
"""
from pprint import pprint


class Car:
    """A car with a brand, model, color and production year.

    Class attributes:
        color_factory (set[str]): Colors available for all cars.
            It is a set, so the order is not guaranteed.

    Attributes:
        brand (str): The manufacturer, for example "Mazda".
        model (str): The model name, for example "M3".
        color (str): The car's color.
        year (int): The production year.
    """

    # Class attribute: shared by every Car instance
    color_factory = {"red", "green", "blue", "yellow", "white"}

    def __init__(self, brand, model, color, year):
        """Initialize a new Car.

        Args:
            brand (str): The manufacturer.
            model (str): The model name.
            color (str): The car's color.
            year (int): The production year.
        """
        # Instance attributes: unique to each Car object
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year


if __name__ == '__main__':
    # Loop style: one car per color, each one year newer than the previous
    car_models = []
    for index, color in enumerate(Car.color_factory):
        start_year = 2020 + index
        new_car = Car("Mazda", "M3", color, start_year)
        # vars() returns the object's attributes as a dict;
        # dict() makes a copy so changing the dict won't change the car
        car_models.append(dict(vars(new_car)))
    pprint(car_models)

    # List comprehension style: same result as the loop above
    new_toyota_cars = [
        dict(vars(Car("Toyota", "RAV-4", color, 2020 + index)))
        for index, color in enumerate(Car.color_factory)
    ]

    print("new_toyota_cars")
    pprint(new_toyota_cars)