

class singleton(type):
    
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls in singleton._instances:
            return singleton._instances[cls]
        singleton._instances[cls] = super().__call__(*args, **kwargs)
        return singleton._instances[cls]



