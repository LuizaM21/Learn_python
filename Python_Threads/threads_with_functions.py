"""Threads working with functions approach"""
from threading import Thread
from time import sleep

def hi():
    for i in range(5):
        print(f"Hi {i+1}")
        sleep(0.3)
def hello():
    for i in range(5):
        print(f"Hello {i+1}")
        sleep(0.3)

if __name__ == "__main__":
    t1 = Thread(target=hi)
    sleep(0.2)
    t2 = Thread(target=hello)

    t1.start()
    t2.start()

    #wait for these 2 threads to complete and JOIN back in order to have the last print at the end
    t1.join()
    t2.join()

    print("Bye!")