# Dependancy Injection Bomb Puzzle

In this assignment you are to diffuse the bomb!

In [bomb.py](bomb.py), you will see an `explosives` superclass and a `bomb`
subclass. The `explosives` class handles the actual explosion, which you are
to prevent, and the `bomb` class handles outputting the *code* which provides
confirmation to the bomber that the bomb went off. Your goal is to print the
*code* without setting off the explosives.

You should write your code in `"diffuser.py"`. You
may import anything from [bomb.py](bomb.py), but note that I will test your
diffuser with a different *code*, so you can't just print out the code provided.
Also, note that the runner.py deletes many builtin python things, so
you're operating in a very restricted environment. The only way to solve the
puzzle should be to use multiple inheritance. (You're welcome to try other methods though)

Running your file should cause the *code* to be printed. You can use
[runner.py](runner.py) to test your solution.

Good Luck, Have Fun!


Side Note: If you're wondering why this assignment is called "Dependancy Injection", 
I recommend this 
[great article](https://medium.com/@suneandreasdybrodebel/pythonic-dependency-injection-a-practical-guide-83a1b1299280) 
about this pattern.
