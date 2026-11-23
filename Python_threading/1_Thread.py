from threading import Thread
import time
def Task1():
    print("Task 1 started!!")
    time.sleep(2)
    print("Task 1 finished")
t1 = Thread(target=Task1)

t1.start()
t1.join()

