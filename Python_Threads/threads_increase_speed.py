"""Compare serial and multi-threaded execution of I/O-bound work.

- download() simulates an I/O-bound task: sleep() stands in for waiting on
  the network or disk.
- While a thread waits on I/O it releases the GIL, so the other threads can
  run. The waits overlap, and the threaded run takes about as long as one
  download (~0.5 s) instead of the sum of all downloads (~1.5 s).
- Threads are a good fit for I/O-bound work. For CPU-bound work use
  multiprocessing instead.
"""

from threading import Thread
from time import sleep, time

def download(file_name):
    """Simulate downloading a file by sleeping for 0.5 seconds.

    Args:
        file_name: Name of the file to "download".
    """
    print("Download file... ",file_name)
    sleep(0.5)
    print("Download complete")


if __name__ == '__main__':
    files = ['video.mp4', 'image.png', 'data.csv']

    start_time =  time()
    for f in files:
        download(f)
    end_time = time()
    print(f"serial time {end_time - start_time:.2f} seconds")
    print("Bye!")

    # create a list for threads
    threads = []
    # create a thread number equal with the length of the files to process
    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)

    # measure execution time
    start_threads_time =  time()
    # start the threads
    for t in threads:
        t.start()
    # wait for every thread to finish before stopping the timer
    for t in threads:
        t.join()
    # measure end time
    end_threads_time =  time()
    print(f"parallel run with threads run: {end_threads_time - start_threads_time:.2f} seconds")