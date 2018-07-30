
def debug(func):
    print('decorating', func.__name__)
    def wrapper(*args, **kwargs):
        print( func.__name__, 'being called on', args, kwargs)
        func(*args, **kwargs)
    return wrapper

