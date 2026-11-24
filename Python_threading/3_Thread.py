from threading import Thread
from time import sleep

def product_search():
    print("Sarching Product!!")
    sleep(3)
    print("Product found sucessfuly!!")
def Add_to_cart():
    print("Adding Product to cart")
    sleep(2)
    print("Product added to cart")
def payment_processing():
    print("Payment in progress")
    sleep(2)
    print("Payment Successfuly!!")

print("Online Shopping Started!!")

t1 = Thread(target=product_search())
t2 = Thread(target=Add_to_cart())
t3 = Thread(target=payment_processing())

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("Order placed Successfully!!")
print("Thanks for Shopping!!")
