import test

def isPallindrome(num):
    """reverse = 0
    ncopy = num
    while num > 0:
        d = num % 10  # Corrected the calculation here
        reverse = reverse * 10 + d
        num //= 10
    if ncopy == reverse:  # Changed from num to reverse for comparison
        return True
    else:
        return False"""

# Run isPallindrome() from test.py
if __name__ == "__main__":
    test.test_pallindrome()
