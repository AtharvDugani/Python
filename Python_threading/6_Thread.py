import threading

def greet(name , age):
    print("Hello", name)
    print(age)

t1 = threading.Thread(target=greet, args=("Nitya",22))
t1.start()
t1.join()
