# test.py

import pickle
from fibonacci import generate_fibonacci

def test_fibonacci():
    correct_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    fib_sequence = generate_fibonacci(10)
    if fib_sequence == correct_sequence:
        print("First 10 Fibonacci numbers are correct.")
        file_path = "Error-404.png"
        with open(file_path, "wb") as file:
            pickle.dump("Lab 05", file)
        print("Open the image Error-404 on Notepad")
    else:
        print("First 10 Fibonacci numbers are incorrect, try again")

if __name__ == "__main__":
    test_fibonacci()
