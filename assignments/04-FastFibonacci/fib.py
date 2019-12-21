
"""
Please make my `fib` function by filling out `make_fast` in `decorator.py`.
"""

from decorator import make_fast
from assert_called import assert_called

@make_fast
@assert_called("original_fib")
def fib(n):
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)
