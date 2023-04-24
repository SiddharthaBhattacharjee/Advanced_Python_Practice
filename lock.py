import threading
# Create a Lock object
lock = threading.Lock()
# Define a shared variable
shared_variable = 0

def increment():
    global shared_variable
    # Acquire the lock
    lock.acquire()
    # Increment the shared variable
    for i in range(10):
       shared_variable += 1
       print(shared_variable)
    # Release the lock
    lock.release()

def decrement():
    global shared_variable
    # Acquire the lock
    lock.acquire()
    # Decrement the shared variable
    for i in range (10):
       shared_variable -= 1
       print(shared_variable)
    # Release the lock
    lock.release()

# Create two threads that access the shared variable
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

# Start the threads
t1.start()
t2.start()

# Wait for the threads to finish
t1.join()
t2.join()

# Print the final value of the shared variable
print("The value of the shared variable is:", shared_variable)
