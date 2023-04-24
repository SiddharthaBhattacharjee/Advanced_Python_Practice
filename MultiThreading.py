import threading
import time

def print_numbers():
    """Prints the numbers 1 through 10"""
    for i in range(1, 11):
        print(i)
        time.sleep(1)

def print_letters():
    """Prints the letters 'A' through 'J'"""
    for letter in 'ABCDEFGHIJ':
        print(letter)
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=print_numbers)
    t2 = threading.Thread(target=print_letters)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
