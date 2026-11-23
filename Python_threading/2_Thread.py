from threading import Thread
import time

def number():
    for i in range(1,6):
        print(i,end=" ")
        time.sleep(1)
def alpha():
    for ch in ['A','B','C','D','E']:
        print(ch)
        time.sleep(1)
t1 = Thread(target=number)
t2 = Thread(target=alpha)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both Tasks completed!!")