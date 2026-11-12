"""A Student that has at least one year recorded by default"""
class Student:
    """The Student class with an empty grade list  by default
    Attributes:
        ""name (str): The name of the student
        ""year (int): The study year of the student
        ""grades (list[str]): The grades of the student"""

    def __init__(self,name, year=1, grades=None):
        self.name = name
        self.year = year
        self.grades = list(grades) if grades is not None else []

    def add_grade(self, grade: int):
        return self.grades.append(grade)

    def add_grades(self, grade: list[int]) -> None:
        self.grades.extend(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else None

if __name__ == '__main__':
    ana = Student("Ana", 2)
    ana.add_grades([9, 10, 8, 10])
    print(ana.name, ana.year, ana.grades, ana.average())

    mihai = Student("Mihai")
    mihai.add_grade(3)
    print(mihai.name, mihai.year, mihai.grades, mihai.average())

    teo = Student("Teo")
    print(teo.name, teo.year, teo.grades, teo.average())