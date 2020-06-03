

from os import listdir
from os.path import isfile, join
from collections import defaultdict


def is_prisoner_file(filename):
    f = filename
    return f == "submission.py" or all([
        isfile(join('./', f)), 
        'prisoner' in f,
        f.endswith('.py'),
        '~' not in f,
    ])

files = list(filter(is_prisoner_file, listdir('./')))

print(files)

prisoners = []

for f in files:
    module = __import__(f[:-3])
    for key, val in module.__dict__.items():
        if isinstance(val, type):
            prisoners.append(val)

print(prisoners)
if len(prisoners) <= 3:
    print("Only found example prisoners.")
    exit(1)

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
