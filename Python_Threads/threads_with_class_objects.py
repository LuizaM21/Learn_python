"""Threads class allows you to run multiple threads at the same time in a single process
Here are couple examples of how to run in parallel 2 threads:
1-thread is represented by 1 class object"""
from threading import Thread
from time import sleep

# Make this class to inherit Threads
class Hello(Thread):
    # the name of the class function must be "run" in order to run
    def run(self):
        for i in range(5):
            print(f"Hello {i+1}!")
            sleep(0.3) #slow the process in order to observe in the console the effect of threads

class Hi(Thread):
    # the name of the class function must be "run" in order to run
    def run(self):
        for i in range(5):
            print(f"Hi {i+1}!")
            sleep(0.3)


if __name__ == '__main__':      # without threads, normally the execution is happening sequentially
    t1 = Hello() #create the class obj as a threads
    t2 = Hi()   #create the class obj as a threads

    t1.start()  #the start method from Threads must be called in order to work
    t2.start()