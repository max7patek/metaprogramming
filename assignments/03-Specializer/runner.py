"""
Run this file to test your partial implementation.
"""

from specialize import specialize

def sum(*args, **kwargs):
  out = 0
  for i in args:
    out += i
  for i in kwargs.values():
    out += i
  return out

p = specialize(sum, 5)
out = p(3)
if out != 8:
    print(f"Error, expected 8, got {out}  (for 5 + 3)")
    exit(1)

pp = specialize(p, keyword=10)
out = pp(2)
if out != 17:
    print(f"Error, expected 17, got {out}  (for 5 + 10 + 2)")
    exit(1)

print("All Tests Passed!!")

