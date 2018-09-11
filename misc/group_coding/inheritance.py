#izzy shehan
#Arthur Browne
# Josh Santana
#Will Clark
#Matthew Bacon
#Caeley Santos
# Marika Gutzman
# Diego Hernandez
#Jason Ashley
#G.Michael Fitzgerald
#Harun Feraidon
# James Garcia-Otero :P aka the bitch no you are
#Ze Wang
#clara kim
#Andrew Walsh
#ganmon witt
#Brad Knaysi
#Spencer Martin
#Tyler Macaluso
# Dylan Cao
#Alex Johnson
# Megan Marshall
#Jimmy Chiou
#Bradley Lund
# Jake Rodal (jr6ff)
#David Alves
#Carolyn Wong
#Erin Barrett
# Devon Yi
# Penn Bauman
# Michael Benos
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

class Patrick(Animal):
    def greet(self, other):
        return "Does Mayonnaise count as an instrument"

class Mitochondria(Animal):
    def greet(self, other):
        return "I am the powerhouse of the cell!"
    def interact(self, other):
        print(self, 'punches you in the face with science and says', self.greet(other), 'to', other)

class Zooter(Animal):
    def greet(self, other):
        return "ZOOOP"

    def interact(self, other):
        print(self.__class__.__name__, ' says: go away ', other.__class__.__name__)

class Hyena(Dog):
    def greet(self, other):
        return "cackle"

class Tiger(Animal):
    def greet(self, other):
        return "Roar, I will eat you!"

    def interact(self, other):
        print(self.__class__.__name__, ' eats ', other.__class__.__name__)

class Elephant(Animal):
    def greet(self, other):
        return "I love Max ;)"

class Mouse(Animal):
    def greet(self,other):
        return '42'

class shark(Animal):
    def greet(self, other):
        return 'wajs'

class Dolphin(Animal):
    def greet(self, other):
        return 'whaddup'

class Fish(Animal):
    def greet(self, other):
        return "I'm a fish, moo"

class Alexa(Animal):
    def greet(self, other):
        return 'playing Despacito 2'

class something(Animal):
    def greet(self, other):
        return "who knows what I am?"

class Giraffe(Animal):
    def greet(self,other):
        return "*long stare while slowly chewing*"

class Chimera(Animal):
    def greet(self,other):
        return "Bleet-Roar-Hiss"



class Liger(Animal):
    def greet(self,other):
        return "All-knowing stare"

class polarBear(Animal):
    def greet(self, other):
        return 'I will eat you now'

class Snek(Animal):
    def greet(self, other):
        return "hissssss"

class Flamingo(Animal):
    def greet(self, other):
        return 'Did you ever hear the tragedy of Darth Plagueis The Wise?'
    def interact(self, other):
        return 'I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.'
# flamingo end
#
class turtle(Animal):
    def greet(self, other):
        return "Hides in shell if scared."

class pig(Animal):

    def greet(self, other):
        return greet(other)

class tiger(Animal):
    def greet(self, other):
        return "ROAR"

class camel(Animal):
    def greet(self,other):
        return "spit is on your face now"

class rhino(Animal):
    def greet(self, other):
        return "Sup, wimp"

class kangaroo(Animal):
    def greet(self, other):
        return "I will kick you"

class Banana(Animal):
    def greet(self, other):
        return "If you believe, you can achieve."
    def interact(self, other):
        print("")

class Adc(Animal):
    def greet(self, other):
        return "flame"

class Pig(Animal):
    def greet(self, other):
        return "Oink"

class Bear(Animal):
    def greet(self, other):
        return "Hello 🐻 " + id(other)

class Human(Animal):
	def greet(self, other):
		return "Hello " + str(other) + "! What a cute little animal!"

class Bigfoot(Animal):
    def greet(self,other):
        [print(" ́ ͂ ̓ ̈́ ͅ ͆ ͇ ͈ ͉ ͊ ͋ ͌ ͍ ͎ ͏ ͐ ͑ ͒ ͓ ͔ ͕ ͖ ͗ ͘ ͙ ͚ ͛ ͜ ͝ ͞ ͟"*1000) for _ in range(1)]


############################# DONT TOUCH THIS ##################################

animals = []
for A in Animal.__subclasses__():
    animals.append(A())

for c in itertools.permutations(animals, r=2):
    c[0].interact(c[1])
