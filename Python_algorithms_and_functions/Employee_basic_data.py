def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        results = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in {} sec'.format(orig_func.__name__, t2))
        return results
    return wrapper


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {} and kwargs: {} '.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


class Employee(object):

    def __init__(self, first_name, last_name, income):
        self.first = first_name
        self.last = last_name
        self.email = first_name + '.' + last_name + '@company.com'
        self.fullEmployeeName = first_name + ' ' + last_name
        self.budget = income

    def apply_raise(self, raise_amount_value):
        self.budget = int(self.budget * raise_amount_value)

    @my_timer
    @my_logger
    def full_employee_details(self):
        return '{} {} {} {}'.format(' Employee first name: ' + self.first + '\n',
                                    'Employee email: ' + self.email + '\n',
                                    'Employee last name: ' + self.last + '\n',
                                    'Employee salary: ' + str(self.budget) + '\n')


emp_1 = Employee('Kelly', 'Fisher', 5000)
emp_2 = Employee('Katie', 'Lawrence', 10000)
emp_3 = Employee('Jake', 'Martin', 1000)
emp_4 = Employee('Mike', "Bloom", 2000)

print('Employee email = ' + emp_1.email)
print('Employee full name = ' + emp_2.fullEmployeeName)

print(emp_1.full_employee_details())
print(Employee.full_employee_details(emp_2))

print('Employee ' + emp_1.fullEmployeeName + ' salary: ' + str(emp_1.budget))
emp_1.apply_raise(1.5)

print('Employee ' + emp_1.fullEmployeeName + 'salary after raise: ' + str(emp_1.budget))
emp_1.apply_raise(1.7)

print('Employee ' + emp_1.fullEmployeeName + 'salary after second raise: ' + str(emp_1.budget))

print('\nEmployee ' + emp_2.fullEmployeeName + ' salary: ' + str(emp_2.budget))
emp_2.apply_raise(1.3)
emp_3.apply_raise(1.5)

print('Employee ' + emp_2.fullEmployeeName + ' salary after raise: ' + str(emp_2.budget))

new_employee_list = []
for x in range(1, 5):
    add_employee = 'emp_{:d}'.format(x)
    new_employee_list.insert(x, eval(add_employee).__dict__)

print('\n\nnew employee list')
print(new_employee_list)

print('\nList of new employee')
for index, emp in enumerate(new_employee_list, start=1):
    print([index], emp)

