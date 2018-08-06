

# imports:

import inspect



# decorators:

def debug(func):
    print('decorating', func.__qualname__)
    def wrapper(*args, **kwargs):
        print( func.__qualname__, 'being called on', args, kwargs)
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
    print('decorating', cls.__qualname__)
    class wrapper(*cls.__bases__):
        pass
    for key, val in inspect.getmembers(cls, predicate=inspect.isfunction):
        setattr(wrapper, key, debug(val))
#    wrapper.__name__ = cls.__name__
    wrapper.__qualname__ = cls.__qualname__
    return wrapper




# tests:
def main():
    @debug_prefix('***')
    def foo(a, b):
        print(a + b)
    
        @debug_class
        class bar(object):
            def foo(self, a , b):
                print(a + b)

if __name__ == '__main__':
    main()
