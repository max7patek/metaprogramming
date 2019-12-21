# Specializer Puzzle

Write a function called `specialize` that takes in a function, a list of positional
arguments, and a dictionary of keyword arguments and returns a function that
calls the parameter function on the arguments supplied along with any new arguments.

Here's an example of this function's usage:

```python
def sum(*args, **kwargs):
  out = 0
  for i in args:
    out += i
  for i in kwargs.values():
    out += i
  return out

p = specialize(sum, 5):
```

```python
>>> p(3)
8
>>> pp = specialize(p, keyword=10)
>>> pp(2)
17

```
