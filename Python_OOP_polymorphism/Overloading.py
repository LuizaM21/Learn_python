"""
Overloading allows different methods to have the same name,
but different signatures where the signature can differ by the number of input parameters
or type of input parameters or both.
Overloading is related to compile-time (or static) polymorphism."""


"""------------Overload build-in methods-------------"""


class Student:
    def __init__(self, grade_1, grade_2):
        self.grade_1 = grade_1
        self.grade_2 = grade_2

    def __add__(self, other):
        param1 = self.grade_1 + other.grade_1
        param2 = self.grade_2 + other.grade_2
        result = Student(param1, param2)
        return result

    def __gt__(self, other):
        param1 = self.grade_1 + self.grade_2
        param2 = other.grade_1 + other.grade_2
        if param1 > param2:
            return True
        return False

    def __str__(self):
        return f"{self.grade_1}, {self.grade_2}"

    def __repr__(self):
        return f"{self.grade_1}, {self.grade_2}"


if __name__ == '__main__':
    student_1 = Student(6, 8)
    student_2 = Student(7, 9)

    s3 = student_1 + student_2
    print(s3.grade_1)
    print(s3.grade_2)

    if student_1 > student_2:
        print("student1 is greater than student2")
    else:
        print("student2 is greater that student1")

    print(student_1)
    print(student_2)
