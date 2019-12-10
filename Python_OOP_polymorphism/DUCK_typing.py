"""Polymorphism means that a designed method can have multiple forms meaning it can behave in many ways.
First concept is called:
 -----------DUCK TYPING------------
From the concept if it is a bird and walk like a duck and quacks like a duck then it`s a duck!
If we have a defined object of a class and we pass as an argument the object of another class
which has the same method name and implementation the program will work without error.
------------------------------------------------------------------------------------------------------
In conclusion if an object has the same methods as another object it is considered to be the same object"""


class Duck:

    def make_steps(self):
        print("duck walk method ")

    def speak(self):
        print("quack quack")


class Chicken:
    def make_steps(self):
        print('chicken walk method')

    def speak(self):
        print('speak like a chicken')


class Bird:

    def walk(self, step):
        step.make_steps()

    def talk(self, word):
        word.speak()


if __name__ == '__main__':
    animal = Bird()

    duck_1 = Duck()
    chicken = Chicken()

    animal.walk(duck_1)
    animal.talk(duck_1)

    animal.walk(chicken)
    animal.talk(chicken)


