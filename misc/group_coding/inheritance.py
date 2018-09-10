

############################# DONT TOUCH THIS ##################################

from abc import ABCMeta, abstractmethod
import itertools
import sys
sys.modules['os'] = None

class Animal(metaclass=ABCMeta): # Extend this!!

    def interact(self, other):
        print(self, 'says', self.greet(other), 'to', other)

    @abstractmethod
    def greet(self, other) -> str:
        raise NotImplementedError

    def __str__(self):
        return self.__class__.__name__


class Cat(Animal):
    def greet(self, other):
        return 'meow'

class Dog(Animal):
    def greet(self, other):
        return 'woof'


############################# Add your animal here #############################


























############################# DONT TOUCH THIS ##################################

animals = []
for A in Animal.__subclasses__():
    animals.append(A())

for c in itertools.permutations(animals, r=2):
    c[0].interact(c[1])
