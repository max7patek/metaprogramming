

from debug_decorator import debug


class debug_type(type):
    def __new__(cls, name, bases, defs):
        print(defs)
        return type(name, bases, {key:debug(val) if callable(val) else val for (key, val) in defs.items()})


class Person(metaclass=debug_type):
    def __init__(self, first, last):
        self.name = first + ' ' + last
    def talk(self):
        print("I'm " + self.name)

p = Person('Max', 'Patek')

p.talk()
