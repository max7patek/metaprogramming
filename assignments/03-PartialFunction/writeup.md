# Partial Puzzle

Write a function called `partial` that takes in a function, a list of positional
arguments, and a dictionary of keyword argumens and returns a function that
calls the parameter function on the arguments supplied along with any new arguments.

Here's an example of this function's usage:

`
def sum(*args):
  out = 0
  for i in args:
    out += i
  return out

p = partial(sum, 5):

#--------------#
>>> p(3)
8
>>> pp = partial(p, 10)
>>> pp(2)
17

`
