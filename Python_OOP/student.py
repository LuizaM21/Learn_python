"""A Student that has at least one year recorded by default"""

class Student:
    """The Student class with an empty grade list  by default
    Attributes:
        name (str): The name of the student
        year (int): The study year of the student
        grades (list[str]): The grades of the student"""

    def __init__(self,name, year=1, grades=None):
        self.name = name.capitalize()
        self.year = year
        self.grades = list(grades) if grades is not None else []

    def add_grade(self, grade: int):
        return self.grades.append(grade)

    def add_grades(self, grade: list[int]) -> None:
        return self.grades.extend(grade)

    def average(self):
        return sum(self.grades) / len(self.grades) if len(self.grades) > 0 else None

    def __repr__(self):
        return (f"Student: {self.name}, "
                f"Year: {self.year}, "
                f"Grades: {self.grades}")

    @classmethod
    def from_string(cls, text):
        parts = text.split(";")
        if len(parts) != 2:
            raise ValueError(f"Expected 'Student;year' but got {text!r}" )
        student = parts[0].strip()
        year =  parts[1].strip()
        if not student or not year:
            raise ValueError(f"One of the values is missing, got {student!r},{year!r}")
        if not student.isalpha():
            raise ValueError(f"Name must contain only letters, got {student!r}")
        try:
            year = int(year)
            if not 1 <= year <= 6:
                raise ValueError
        except:
            raise ValueError(f"The year of the student is not valid, got {year!r}")
        return cls(student, year)


if __name__ == '__main__':
    ana = Student("ana", 2)
    ana.add_grades([9, 10, 8, 10])
    print(ana.name, ana.year, ana.grades, ana.average())

    mihai = Student("mihai")
    mihai.add_grade(3)
    print(mihai.name, mihai.year, mihai.grades, mihai.average())

    teo = Student("Teo")
    print(teo.name, teo.year, teo.grades, teo.average())
    print(teo.__repr__())


    bad_inputs = ["Ana", "Ana;2;x", "Ana;abc", "Ana;0", "Ana;7", "ana;", ";2", "23; 6"]
    for text in bad_inputs:
        try:
            print(Student.from_string(text))
        except ValueError as e:
            print(f"{text!r} → Error: {e}")
    print(Student.from_string(" ana ; 1 "))  # Student('Ana', 1)