"""Generators provides the means for describing iterable series with code and functions
- are lazily evaluates: they execute one value on demand
- can run infinite sequences with no defined end
- instead of return the generators uses yield key word"""


""""    
    stop = int(num_product/2+1)
    for item in range(1, stop):
        if item % num_product == 0:
            print(item)
            yield item
    yield num_product
    
    24 = 2 * 2 * 2 * 3
"""


def sum_of_input(num):
    """"Return a list of all numbers that the sum of them equals the input number"""
    for c1 in range(10):
        if c1 == num:
            item_list = [c1, 0, 0]
            yield item_list
        for c2 in range(10):
            if c1 + c2 == num:
                item_list = [c1, c2, 0]
                yield item_list
            for c3 in range(10):
                if c1 + c2 + c3 == num:
                    item_list = [c1, c2, c3]
                    yield item_list


def divisor_gen(num_product):
    # prime_factors = [x for x in range(2, num_product) if not x % 2 == 0 or x == 2]
    # print(prime_factors)
    print(num_product)
    divider = 2
    # factors_list = []
    while divider * divider <= num_product:
        if num_product % divider:
            divider += 1
        else:
            num_product //= divider
            yield divider
    if num_product > 1:
        yield num_product


# yield must be used at least once in generator function
def gent123():
    yield 1
    yield 2
    yield 3


# stateful generator function
def take(count, iterable):
    counter = 0
    for item in iterable:
        if count == counter:
            return
        counter += 1
        print('counter = ' + str(counter))
        yield item


def eliminate_duplicate_value(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def lucas_series():
    yield 2
    a = 2
    b = 1
    while a <= 25:
        yield b
        a, b = b, a + b


def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def even_number(start, stop=None, step=2):
    interval_list = []
    step = 1 if step is None else step

    def in_interval(element):
        if element < stop:
            return start <= element < stop
        return start >= element > stop

    if stop is None:
        stop, start = start, 0
    if stop == start:
        return interval_list
    if not in_interval(start + step):
        return interval_list

    current_elem = start
    while in_interval(current_elem):
        interval_list.append(current_elem)
        yield interval_list
        current_elem += step


if __name__ == "__main__":
    [print(x, end=' ')for x in divisor_gen(300)]
    print()
    [print(x) for x in sum_of_input(7)]
    # [print("even_num: ", i) for i in even_number(11)]
    # g = gent123()
    # # to retrieve a value of a generator we can use next() function
    # [print(gen) for gen in g]
    # print()
    # items = [0, 2, 4, 6, 8, 10]
    # [print(item) for item in take(4, items)]
    # print('Eliminate distinct values')
    # duplicate_values = [2, 2, 3, 3, 7, 7, 8, 9]
    # [print(item) for item in eliminate_duplicate_value(duplicate_values)]
    # print('lucas series')
    # [print(x) for x in (p for p in lucas_series() if is_prime(p))]
    #



