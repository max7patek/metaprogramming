

# imports:

import inspect



# decorators:

def debug(func):
    print('decorating', func.__name__)
    def wrapper(*args, **kwargs):
        print( func.__name__, 'being called on', args, kwargs)
        return func(*args, **kwargs)
    return wrapper


def debug_prefix(prefix):
    print('receiving prefix:', prefix)
    def debug(func):
        print('decorating', func.__name__)
        def wrapper(*args, **kwargs):
            print(prefix, func.__name__, 'being called on', args, kwargs)
            return func(*args, **kwargs)
        return wrapper
    return debug


def debug_class(cls):
    print('decorating', cls.__name__)
    class wrapper(*cls.__bases__):
        pass
    for key, val in inspect.getmembers(cls, predicate=inspect.isfunction):
        setattr(wrapper, key, debug(val))
    return wrapper




# tests:

@debug_prefix('***')
def foo(a, b):
    print(a + b)
    
@debug_class
class bar(object):
    def foo(self, a , b):
        print(a + b)
