
from shrinkme import image as ref
from shrinked import image
from random import randrange

def random_array(x, y):
    out = []
    for i in range(x):
        out.append([])
        for j in range(y):
            out[i].append(randrange(256))
    return out

a = random_array(100, 100)
b = random_array(100, 100)
num = randrange(100)

a_ref = ref(a)
a_img = image(a)
b_ref = ref(b)
b_img = image(b)

assert not ref in image.mro(), 'You may not inherit from the unshrinked image class'

passed_all = True

for key in ref.__dict__:
    if len(key) > 3 and not key[0:2] == '__':
        passed = False
        try:
            passed = ref.__dict__[key](a_ref, num) == image.__dict__[key](a_img, num)
        except BaseException:
            passed = ref.__dict__[key](a_ref, b_ref) == image.__dict__[key](a_img, b_img)
        print(key, 'passed' if passed else 'failed')
        if not passed:
            passed_all = False

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

length = file_len('shrinked.py')
print('length is ' + str(length) + ' lines.' )

score = 0 if not passed_all else remap(length, 22, 54, 100, 0)

print('score is ' + str(score) + '%')
