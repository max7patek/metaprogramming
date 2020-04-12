
"""
Quines:
_='_=%r;print (_%%_)';print (_%_)
s='s=%r;print(s%%s)';print(s%s)
NOT _="_=%r;print (_%%_)";print (_%_)

NOT self = 'self = {}; print(self.format(self))'; print(self.format(self))
self = 'self = {!r}; print(self.format(self))'; print(self.format(self))
s='s={!r};print(s.format(s))';print(s.format(s))

NOT self = 'print("self = " + self + "; eval(self)")'; eval(self)
self = 'print("self = " + repr(self) + "; eval(self)")'; eval(self)

s = 's = f"{!r}"

"""



from contextlib import redirect_stdout
import io
import traceback





def check_quine(string):
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            exec(string, {}, {})
        except:
            traceback.print_exc()
            return False
    result = f.getvalue().strip()
    # print(f"{result=}, {string=}")
    if result != string:
        print(f"inputted\t{string}\noutputted\t{result}")
        return False
    print(f"{string} is a quine")
    return True


if __name__ == "__main__":
    while True:
        check_quine(input("Input a quine: "))

