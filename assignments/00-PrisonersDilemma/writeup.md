# Prisoner's Dilemma Exploration

Your task is to continue our group-coding activity from the first lecture.
Implement a Prisoner class that has the following methods:

 - `__init__(self, both_confess_sentence, none_confess_sentence, self_confess_sentence, other_confess_sentence)`
 - `decide(self)`
 - `sentence(self, years)`

It doesn't matter what you call your prisoner class (funny names are acceptable).
However, call your file `"<computing id>_prisoner.py"`

Your submissions will compete at the beginning of next class. Extra credit for the winner *and* the looser.

 ### __init__

`__init__` takes in the sentence (penalty in years) for each of the four scenarios as parameters in the following order:

 - Both prisoners confess and rat on eachother
 - Both prisoners keep their mouths shut and don't confess
 - `self` confesses but the other prisoner doesn't
 - The other prisoner rats `self` out, but `self` didn't confess!

You may assume that the sentences are unique.
That way, upon your sentencing, you can determine what your accomplice decided, which will
help your prisoner make more informed decisions for future interrogations.

### decide

The `decide` method takes in no parameters other than `self`. It should decide whether to confess or to remain silent.
It should return `True` to confess and `False` to keep quiet.

### sentence

When testing the prisoners, I will pair up instances and call `decide` on each one.
The two decisions will yield a sentence, which I will pass back to your prisoner through the `sentence` method.
You may assume that this sentence is associated with the previous decision.
The prisoner will probably want to remember this sentence somehow so that he/she can make a more informed decision next time.
The sentence you receive will be one of the four possibilities that were passed in through `__init__`.
You should be able to deduce what your partner did by looking your sentence up in those possibilities.

### Testing

There is a [tester file](tester.py) that I will use to make your prisoners compete.
It collects all the prisoners that are in the same directory as it and runs them together.
I recommend that you copy and paste your prisoner so that you can run the tester to verify that your code works.
