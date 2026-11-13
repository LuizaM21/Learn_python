"""Compare serial, multi-threading and multi-process execution of CPU-bound work.

- GIL (Global Interpreter Lock): in CPython only one thread at a time can run
  Python code, so threads don't speed up CPU-bound work.

- Threads share memory and the same GIL. They are still useful for I/O-bound
  work, because a thread releases the GIL while waiting.

- Each Process has its own interpreter, GIL and memory, so CPU-bound work runs
  truly in parallel on multiple cores. Starting processes costs more, and data
  must be passed between them explicitly (e.g. with a Queue).
"""

from threading import Thread
from time import perf_counter
from multiprocessing import Process


def calculate(num1, num2):
    """Return the sum of the squares of all integers in [num1, num2).

    This is a purely CPU-bound task, used to compare execution models.

    Args:
        num1: Start of the range (inclusive).
        num2: End of the range (exclusive).

    Returns:
        The total of i * i for every i in the range.
    """
    total = 0
    for i in range(num1, num2):
        # add square root of i
        total += i * i
    return total


if __name__ == '__main__':
    # The __main__ guard is required for multiprocessing: on macOS and
    # Windows each child process re-imports this file, and without the
    # guard every child would start new processes itself.

    num = 50_000_000
    mid = num // 2  # split the range in two halves, one per worker

    # 1. Serial: one call on the whole range, used as the baseline.
    start =  perf_counter()
    calculate(0, num)
    end = perf_counter()
    print(f"total serial time: {end -  start:.2f} sec")

    # 2. Threads: expected to be about as slow as serial, because the GIL
    #    lets only one thread run Python code at a time.
    #    Note: a Thread's return value is discarded; use a shared list or a
    #    Queue if you need the results.
    t1 = Thread(target=calculate, args=(0, mid))
    t2 = Thread(target=calculate, args=(mid, num))

    start_threads = perf_counter()
    t1.start()
    t2.start()

    t1.join()   # wait for both threads to finish before stopping the timer
    t2.join()
    end_threads = perf_counter()
    print(f"total thread time: {end_threads - start_threads:.2f} sec")

    p1 = Process(target=calculate, args=(0,mid))
    p2 = Process(target=calculate, args=(mid, num))

    start_process_time = perf_counter()
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end_process_time = perf_counter()
    print(f"total process time: {end_process_time- start_process_time:.2f} sec")