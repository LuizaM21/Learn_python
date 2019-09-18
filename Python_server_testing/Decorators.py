import functools
from timeit import default_timer as timer


def request_duration(input_function):
    @functools.wraps(input_function)
    def new_function(*args, **kwargs):
        start_time = timer()
        value = input_function(*args, **kwargs)
        end_time = timer()
        duration = end_time - start_time
        print("\nRequest duration: {:.3f}".format(duration))
        return value
    return new_function


def decorator_test(inside_function):
    initial_value = 1
    print('initial_value= ', initial_value)
    print("Ran function outside")

    def new_function(*args, **kwarg):
        value = inside_function(*args, **kwarg)
        print("Ran function inside")
        return value
    return new_function


@decorator_test
def decorator_display(message):
    return f"{message} Run original function"


if __name__ == '__main__':
    print(decorator_display('message test'))


