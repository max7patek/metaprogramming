
"""
Run this file to check the speed of the fib function.
"""

from fib import fib
from assert_called import verify_called_count, _counts

import time 
import sys

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start

def reference_fib(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def test(n, microseconds_allowed=10000):
    expected = reference_fib(n)
    with Timer() as t:
        actual = fib(n)
    if expected != actual:
        print(f"Error: expected {expected} but got {actual} for n={n}")
        exit(1)
    else:
        microseconds = t.interval*1000000
        print(f"fib({n}) took {microseconds:.0f} microseconds")
        if microseconds > microseconds_allowed:
            print(f"Error: too slow, {microseconds_allowed} mircoseconds allowed")
            exit(1)

        
reference = "\n".join(f"{n}: {reference_fib(n)}" for n in range(11))

print(f"Reference fib:\n{reference}\n")

print("Running fib on some small imputs")
for n in range(2, 13):
    test(n)

print("\nRunning fib on some big inputs")
test(200)

print("\nNow running on slightly smaller")
test(199, 20)

print("\nNow running on slightly larger")
test(202, 20)

verify_called_count("original_fib", 203)

print("\nAll Tests Passed!!")
