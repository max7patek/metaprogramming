_print = print
def print(array):
    _print(''.join(map(str,(map(int, array)))))

def lex_successor(array, i=0):
    if i == len(array):
        yield array
    else:
        if array[i] is not True:
            array[i] = False
            yield from lex_successor(array, i+1)
            array[i] = True
            for j in range(i+1, len(array)):
                array[j] = None
            yield from lex_successor(array, i+1)
        else:
            yield from lex_successor(array, i+1)

import sys
arr = []
for i in sys.argv[1]:
    arr.append(bool(int(i)))
for i in lex_successor(arr):
    print(i)
