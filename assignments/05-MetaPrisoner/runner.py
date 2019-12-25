

from metaprisoner import prisoners, MetaPrisoner
from os import listdir
from os.path import isfile, join
from collections import defaultdict
from pprint import pprint


def is_prisoner_file(filename):
    f = filename
    return all([
        isfile(join('./', f)), 
        'prisoner' in f,
        f.endswith('.py'),
        '~' not in f,
        'metaprisoner' not in f,
    ])

files = list(filter(is_prisoner_file, listdir('./')))

print(files)
for f in files:
    __import__(f[:-3]) # runs the file

# In assignment 00, runner.py had to scan the modules for prisoners
# Now, MetaPrisoner keeps track of the prisoners for us!

print(prisoners)


scoreboard = defaultdict(int)
runs = 100
sentences = (5, 2, 0, 6) # temporary, may change
score_map = {
    (True, True) : (sentences[0], sentences[0]),
    (False, False) : (sentences[1], sentences[1]),
    (True, False) : (sentences[2], sentences[3]),
    (False, True) : (sentences[3], sentences[2]),
}


def play(p1, p2):
    i1, i2 = p1(*sentences), p2(*sentences)
    for _ in range(runs):
        s1, s2 = score_map[(i1.decide(), i2.decide())]
        i1.sentence(s1)
        i2.sentence(s2)
        scoreboard[p1] += s1
        scoreboard[p2] += s2

for i in range(len(prisoners)):
    for j in range(i+1, len(prisoners)):
        play(prisoners[i], prisoners[j])

for p, s in scoreboard.items():
    print(f"{p} scored {s}")
# score indicates years sentenced (low score is better)

try:
    class IncompletePrisoner(metaclass=MetaPrisoner):
        def __init__(self, *args):
            pass
        def sentence(self, *args):
            pass
    print("Error: was allowed to create a prisoner class without a decide method")
    exit(1)
except TypeError:
    pass

class NamedPrisoner(metaclass=MetaPrisoner):
    def __init__(self, *args):
        pass
    def decide(self):
        pass
    def sentence(self, *args):
        pass
result = str(NamedPrisoner)
if result != "NamedPrisoner":
    print(f"Error: calling str(NamedPrisoner) returned \"{result}\", not \"NamedPrisoner\".") 
    exit(1)

print("All Tests Passed!!")

