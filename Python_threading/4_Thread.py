
import threading
import time

orders_processed = 0
lock = threading.Lock()


# Order Verification
def verify_order():
    global orders_processed

    for i in range(3):
        print(f"{threading.current_thread().name}: Verifying Order {i + 1}")
        time.sleep(2)

        lock.acquire()
        orders_processed += 1
        lock.release()


# Payment Processing
def process_payment():
    global orders_processed

    for i in range(3):
        print(f"{threading.current_thread().name}: Processing Payment {i + 1}")
        time.sleep(1)

        lock.acquire()
        orders_processed += 1
        lock.release()


# Inventory Update
def update_inventory():
    global orders_processed

    for i in range(3):
        print(f"{threading.current_thread().name}: Updating Stock {i + 1}")
        time.sleep(1.5)

        lock.acquire()
        orders_processed += 1
        lock.release()


# Creating Threads
t1 = threading.Thread(
    target=verify_order,
    name="Verification Thread"
)

t2 = threading.Thread(
    target=process_payment,
    name="Payment Thread"
)

t3 = threading.Thread(
    target=update_inventory,
    name="Inventory Thread"
)


# Starting Threads
t1.start()
t2.start()
t3.start()


# Waiting for Completion
t1.join()
t2.join()
t3.join()


print("\nAll threads completed.")
print("Total Operations Processed:", orders_processed)
