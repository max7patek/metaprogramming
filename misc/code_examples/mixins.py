

from collections import namedtuple

Ingredient = namedtuple("Ingredient", ["name", "cost"])

dough = Ingredient("dough", 1)
sauce = Ingredient("sauce", 1)
cheese = Ingredient("cheese", 1)
pepperoni = Ingredient("pepperoni", 2)
sausage = Ingredient("sausage", 2)
ham = Ingredient("sausage", 2)
pineapple = Ingredient("pineapple", 1)

class Pizza:
    def __init__(self):
        self.ingredients = {dough, sauce, cheese}
        self.markup = 2
    
    def cost(self):
        raw = sum(x.cost for x in self.ingredients)
        return raw * self.markup


class Hawaiian(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients.add(ham)
        self.ingredients.add(pineapple)

class MeatLover(Pizza):
    def __init__(self):
        super().__init__()
        self.ingredients.add(pepperoni)
        self.ingredients.add(sausage)
        self.ingredients.add(ham)

class Gourmet(Pizza):
    def __init__(self):
        super().__init__()
        self.markup += 1

class Special(Gourmet, MeatLover, Hawaiian, Pizza):
    pass

za = Special()

print(za.cost())
