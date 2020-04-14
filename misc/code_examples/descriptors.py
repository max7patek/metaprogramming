
from types import SimpleNamespace
from typing import Optional


class InfiniAttr:

    def __getattr__(self, name):
        setattr(self, name, InfiniAttr())
        return getattr(self, name)


foo = InfiniAttr()

print(foo.a)
print(foo.bar.a.x)



class Immutable:
    def __init__(self, x):
        self.x = x
    def __setattr__(self, name, val):
        if hasattr(self, name):
            raise AttributeError(f"{type(self).__name__} is immutable")
        else:
            self.__dict__[name] = val


if __name__ == "__main__":
    im = Immutable(2)

if __name__ == "__main__":
    print(im.x)
    im.y = 4
    print(im.y)
    try:
        im.y = 3
        print("COULD RESET Y")
    except AttributeError:
        print("Could not reset y")


class Person:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


if __name__ == "__main__":
    p = Person(name="Max", age=22)

    p.talk = lambda self: print(f"I'm {self.name}")

    try:
        p.talk()
        print("self was bound!?")
    except TypeError:
        print("TypeError: <lambda>() missing 1 required positional argument: 'self'")

    del p.talk
    Person.talk = lambda self: print(f"I'm {self.name}")

    p.talk()



class MyDesc:
    def __get__(self, obj, type=None):
        print(f"binding {self} to {obj}, {type=}")
        return "Hello Descriptors"


class Test:
    x = MyDesc()

if __name__ == "__main__":
    t = Test()

    print(t.x)


def naive_static(function):
    def func(self, *args, **kwargs):
        return function(*args, **kwargs)
    return func 


class good_static:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, obj, type=None):
        return self.func

class ClsWithStatic:

    @naive_static
    def foo(a, b):
        return a + b
    
    @good_static
    def bar(a, b):
        return a + b


class Setter:
    def __set__(self, obj, value):
        print(f"setting {self} on {obj} to {value}")
        obj.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name


class TestSetter:
    x = Setter()
    def __init__(self, x):
        self.x = x


class TypeChecked:
    def __init__(self, type, optional=False):
        self.type = type
    def __set__(self, obj, value):
        if not isinstance(value, self.type):
            raise TypeError(f"{self.name} must be of type {self.type}")
        obj.__dict__[self.name] = value
    def __set_name__(self, owner, name):
        self.name = name


class AutoInit(type):
    def __new__(meta, name, bases, attrs):
        fields = [
            key for key, value in attrs.items() 
            if isinstance(value, TypeChecked)
        ]
        args = ", ".join(f for f in fields)
        sets = "".join(f"\n    self.{f} = {f}" for f in fields)
        code = f"def __init__(self, {args}):{sets}"
        print(code)
        exec(code, globals(), attrs)
        return super().__new__(meta, name, bases, attrs)



# class DescriptPerson():
class DescriptPerson(metaclass=AutoInit):
    name = TypeChecked(str)
    age = TypeChecked(int)



if __name__ == "__main__":
    p = DescriptPerson("Max", 22)
