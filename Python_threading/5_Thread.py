import threading
import time
def greet1():
    print("Hello from greet1")
    time.sleep(2)
    print("After wait")
def greet2():
    print("Hello from greet2")
    time.sleep(5)
    print("Finished 2")
def greet3():
    print("Hello from greet3")

t1 = threading.Thread(target=greet1)
t2 = threading.Thread(target=greet2)
t3 = threading.Thread(target=greet3)


t1.start()
t1.join()
t2.start()
t2.join()
t3.start()

print("Main program executed!!")


