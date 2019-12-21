
_counts = {}

def verify_called_count(key, count):
    actual = _counts[key]
    if actual != count:
        print(f"""
Warning: expected {key} to be called {count} times 
    but was actually called {actual} times.
    This may not be a problem, depending on implementation details,
    but if the actual number of calls is 0, then please make sure that
    your decorator is actually calling the the function it's decorating.
            """)
        exit(1)

def assert_called(key):
    def decorator(func):
        _counts[key] = 0
        def wrapper(*args, **kwargs):
            _counts[key] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator