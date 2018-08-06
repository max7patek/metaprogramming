



class registrar(type):

    def _add_subclass(cls, c):
        cls.subclasses.append(c)

    def __init__(cls, name, bases, attrs):
        cls.subclasses = []
        for c in cls.mro()[1:]:
            if hasattr(c, '_add_subclass') and callable(c._add_subclass):
                c._add_subclass(cls)
        
