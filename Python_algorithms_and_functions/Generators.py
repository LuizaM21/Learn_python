"""Generators provides the means for describing iterable series with code and functions
- are lazily evaluates: they execute one value on demand
- can run infinite sequences with no defined end
- instead of return the generators uses yield key word"""


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


if __name__ == "__main__":
    g = gent123()
    # to retrieve a value of a generator we can use next() function
    [print(gen) for gen in g]
    print()
    items = [0, 2, 4, 6, 8, 10]
    [print(item) for item in take(4, items)]
    print('Eliminate distinct values')
    duplicate_values = [2, 2, 3, 3, 7, 7, 8, 9]
    [print(item) for item in eliminate_duplicate_value(duplicate_values)]
    print('lucas series')
    [print(x) for x in (p for p in lucas_series() if is_prime(p))]




