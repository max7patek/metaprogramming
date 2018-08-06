

class Person(object):
    
    def __init__(self, first_name, last_name):
        self.name = first_name + ' ' + last_name
    
    def talk(self):
        print("I'm", self.name)
    
    @classmethod
    def make_family(cls, last_name):
        def init(self, first_name, last_name=last_name):
            cls.__init__(self, first_name, last_name)
        return type(
            last_name,
            (cls,),
            {'__init__': init})



