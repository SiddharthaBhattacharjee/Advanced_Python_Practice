import multiprocessing
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
    p1 = multiprocessing.Process(target=print_numbers)
    p2 = multiprocessing.Process(target=print_letters)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
