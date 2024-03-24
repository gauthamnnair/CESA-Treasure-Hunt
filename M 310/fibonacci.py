#To check the answer
import test

# Fibonacci sequence generation
# Store the answer in a array named fibonacci
fibonacci = []
def generate_fibonacci(n):
    """if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        fibonacci.append(0)
        return [0]
    elif n == 2:
        fibonacci.extend([0, 1])
        return [0, 1]
    else:
        fibonacci.extend([0, 1])  # Initialize with first two Fibonacci numbers
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            fibonacci.append(b)
        return fibonacci
    """
# Run test_fibonacci() from test.py after generating the Fibonacci sequence
if __name__ == "__main__":
    test.test_fibonacci()
