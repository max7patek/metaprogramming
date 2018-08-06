

#from families import Person as family_person
from debug_decorator import debug_class


@debug_class
class MetaClass(type):

    def __new__(meta, name, bases, attrs):
        #print('metaclass __new__ called on', meta, name, bases, attrs)
        return type.__new__(meta, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        #print('metaclass __init__ called on', cls, name, bases, attrs)
        type.__init__(cls, name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        #print('metaclass __call__ called on', cls, *args)
        return type.__call__(cls, *args, **kwargs)

def main():
    debugged_regular_person = debug_class(family_person)


    Person1 = MetaClass('Person1', debugged_regular_person.__bases__, dict(debugged_regular_person.__dict__))

    p1 = Person1('Max', 'Patek')

    p1.talk()

    class Person2(metaclass=MetaClass):
        def __init__(self, name):
            self.name = name
        def talk(self):
            print("I'm", self.name)


        p2 = Person2('Leah')

        p2.talk()
