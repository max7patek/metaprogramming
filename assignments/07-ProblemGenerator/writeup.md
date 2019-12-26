# Problem Generator

This assignment has two parts, and you will have a week for each part.

## Part 1: Generator

Assume the roll of a CS exam writer. You need to write some exams, and 
you like the questions that provide the student with a code snippet and
ask what gets printed. For example:

> Question:
>
> What is printed by the following code?
```
class C:
    def __init__(self, x):
        self.x = x

a = C(3)
b = a
c = b
del a
b.x += 1
print(c.x)
```
> Answer:
>
> `4`

You want to be able to generate many of these problems, but with slight 
variations to prevent cheating or for makeup tests etc. For example, here's
a variation:

> Question:
>
> What is printed by the following code?
```
class C:
    def __init__(self, x):
        self.x = x

a = C(5)
b = a
c = b
del a
b.x += 1
print(c.x)
```
> Answer:
>
> `6`

You are to write a program to generate these problem variations. The program
should take the correct answer as input and output the problem. In other 
words, take the string that should be printed as input, and output the code
that prints that string. Here's an example of that program running:

```
<stderr> Input an integer: <stdin> 4
<stdout> 
<stdout> 
<stdout> class C:
<stdout>     def __init__(self, x):
<stdout>         self.x = x
<stdout> 
<stdout> a = C(3)
<stdout> b = a
<stdout> c = b
<stdout> del a
<stdout> b.x += 1
<stdout> print(c.x)
<stdout> 

```

Note that the input (4) is what is printed by the output (the program).

Please get creative with your problems! The problem should be at least a 
little tricky, but still solvable by hand. You're encouraged to make the 
problem about some metaprogramming topic.

Also note that there is no `runner.py` with this assignment. See Part 2.


## Part 2: Validator

A very common application of metaprogramming is the testing or validation 
of code.

For this assignment, you are to write a `runner.py` to test your solution to 
the Part 1. Your runner should try running your program from part 1 on several 
different inputs and validate that the code outputted does in fact print the 
original input. 

Feel free to look at the supplied `runner.py` files for the other assignments
for inspiration.

Also note that this task might become painfully meta. You are 
1. writing code that 
2. executes code, and 
3. takes the output of that code and executes it.

This may be easier depending on how you implemented you solution to Part 1.
Feel free to modify your solution to Part 1. For example, it might be 
convenient to put the logic of converting the input to the outputted code
in a function with simple parameters and a return value. Then your script
for Part 1 might simply be:
```
import sys

def gen(answer):
    # ...
    pass # return question as string

if __name__ == "__main__":
    sys.stderr.write("Input the answer: ")
    answer = input()
    question = gen(answer)
    print(question)
```
Then you could only validate that `gen` function.
