"""
Run this to test your print function.
"""

from contextlib import redirect_stdout
import io
import sys

from esoteric_print import Printer


inputs = ["aaa", "aaa aaa", "b", "b", "c", "c", "c"]


sys.stdout.write("Testing: Printer(1)\n")
f = io.StringIO()
printer = Printer(1)
with redirect_stdout(f):
    for s in inputs:
        printer(s)

outputs = list(map(str.strip, f.getvalue().split("\n")))[:-1]

sys.stdout.write(f"Inputs:  {inputs}\n")
sys.stdout.write(f"Outputs: {outputs}\n\n")

for expected, actual in zip(inputs[:3], outputs[:3]):
    if expected != actual:
        sys.stderr.write(f"Error: trying to print \"{expected}\" printed \"{actual}\".\n")
        exit(1)
    else:
        sys.stdout.write(f"Successful printed \"{expected}\"!\n")
if inputs[3] != outputs[3]:
    sys.stdout.write(f"Successfully did not print \"{expected}\" a second time!\n")
else:
    sys.stderr.write(f"Error: was allowed to print \"{expected}\" a second time.\n")
    exit(1)

if inputs[4] != outputs[4]:
    sys.stderr.write(f"Error: trying to print \"{expected}\" printed \"{actual}\".\n")
    exit(1)
else:
    sys.stdout.write(f"Successful printed \"{expected}\"!\n")

if inputs[5] != outputs[5]:
    sys.stdout.write(f"Successfully did not print \"{expected}\" a second time!\n")
else:
    sys.stderr.write(f"Error: was allowed to print \"{expected}\" a second time.\n")
    exit(1)


sys.stdout.write("\nTesting: built-in print\n")
f = io.StringIO()

with redirect_stdout(f):
    for s in inputs:
        print(s)

outputs = list(map(str.strip, f.getvalue().split("\n")))[:-1]

sys.stdout.write(f"Inputs:  {inputs}\n")
sys.stdout.write(f"Outputs: {outputs}\n\n")

for expected, actual in zip(inputs[:-1], outputs[:-1]):
    if expected != actual:
        sys.stderr.write(f"Error: trying to print \"{expected}\" printed \"{actual}\".\n")
        exit(1)
    else:
        sys.stdout.write(f"Successful printed \"{expected}\"!\n")
if inputs[-1] != outputs[-1]:
    sys.stdout.write(f"Successfully did not print \"{expected}\" a third time!\n")
else:
    sys.stderr.write(f"Error: was allowed to print \"{expected}\" a third time.\n")
    exit(1)



sys.stdout.write("All Tests Passed!\n")
