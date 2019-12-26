
_counts = {}

def verify_called_count(key, count):
    actual = _counts[key]
    if actual != count:
        print(f"""
Warning: expected {key} to be called {count} times 
    but was actually called {actual} times.
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