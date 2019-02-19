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

