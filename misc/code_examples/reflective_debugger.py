
# imports

import inspect
import sys
from pprint import pprint
import functools



# tracer code

def _get_source(obj):
    try:
        return inspect.getsourcelines(obj)
    except OSError:
        return None


def upon_call(frame, event, arg):
    return print_everything


def print_line(line, is_current):
    prefix = ' '
    if is_current:
        prefix = '>'
    print(prefix, line, end='')

def is_dunder(string):
    return len(string) >= 2 and string[:2] == '__' and string[-2:] == '__'

def set_vars(string, globals, locals):
    arr = string.split('=')
    arr = list(map(str.strip, arr))
    if len(arr) == 2:
        value = eval(arr[1], globals, locals)
        if arr[0] in locals:
            print(type(locals))
            locals[arr[0]] = value
        else:
            globals[arr[0]] = value



def print_everything(frame, event, arg):
    source = _get_source(frame.f_code)
    if source is not None:
        if event == 'return':
            print('returning')
            return
        print('code:')
        for index, line in enumerate(source[0]):
            print_line(line, index == frame.f_lineno - frame.f_code.co_firstlineno)
        print('globals:')
        for i in frame.f_globals:
            if not is_dunder(i):
                print('   ', i, '=', frame.f_globals[i])
        print('locals:')
        for i in frame.f_locals:
            print('   ', i, '=', frame.f_locals[i])
        print('callstack:')
        for i in reversed(inspect.getouterframes(frame)):
            print('   ',i.function + ':',
                  i.code_context[0] if i.code_context is not None else '\n',
                  end='')
        string = input('set an already declared variable or just hit enter: ')
        set_vars(string, frame.f_globals, frame.f_locals)


# interface

def start():
    sys.settrace(upon_call)


def nop(frame, event, arg):
    return None

end = functools.partial(sys.settrace, nop)


def debug(callme):
    def func(*args, **kwargs):
        start()
        callme(*args, **kwargs)
        end()
    return func

# testing and demo

if __name__ == '__main__':
    global foo, bar, printer, exec_test, assign_test, inspect_test
    import itertools

    def foo(a, b):
        c = a + b
        print(c)

    def bar(*args):
        for i in itertools.combinations(args, 2):
            foo(*i)

    def printer(*args):
        print(args)
        return printer

    def exec_test():
        a = 1
        exec('a = 2')
        print(a)

    def assign_test():
        a = 1
        locals()['a'] = 2
        print(a)

    def inspect_test():
        a = 1
        f = inspect.currentframe()
        f.f_locals['a'] = 1
        print(type(f.f_locals))
        print(a)
