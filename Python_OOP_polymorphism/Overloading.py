"""
Overloading allows different methods to have the same name,
but different signatures where the signature can differ by the number of input parameters
or type of input parameters or both.
Overloading is related to compile-time (or static) polymorphism.
"""


"""
-----------------------------------------------------------------------------------------------------------------
OVERLOADING IS NOT POSSIBLE IN PYTHON BECAUSE WE CAN`T DEFINE 2 METHODS WITH THE SAME NAME IN THE SAME CLASS
WE CAN ONLY IMPLEMENT THIS MANUALLY IT IS NOT SUPPORTED IN PYTHON BY DEFAULT
-----------------------------------------------------------------------------------------------------------------
"""


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


"""------------Overload User-Defined Functions---------------"""


class Employee:

    # the method can be called with or without a parameter
    def __init__(self, employee_name=None, list_of_empl=None):
        self.employee = employee_name
        if list_of_empl is None:
            self.employee_list = []
        self.employee_list = list_of_empl

    def hello(self):
        if self.employee is None:
            return 'Hello!'
        return f'Hello, {self.employee}'

    def count_employee(self):
        if len(self.employee_list) is 0:
            return 'Length of the list: 0'
        return 'Length of the list: '.format(len(self.employee_list))


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

    unknown_employee = Employee()
    employee_1 = Employee('Kevin')
    empl_list = Employee('Kevin', ['empl_1', 'empl_2'])

    print(unknown_employee.hello())
    print(employee_1.hello())
    print(empl_list.count_employee())


