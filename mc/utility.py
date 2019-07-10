
from mc import Dict, List, Set


def chain(*callables):
    def f(arg):
        result = arg
        for c in callables:
            result = c(result)
        return result

    return f


def mux(*callables, **kwcallables):
    if len(callables) == 0 and len(kwcallables) != 0:

        def f(arg):
            result = Dict({})
            for c in kwcallables:
                result[c] = kwcallables[c](arg)
            return result

        return f
    if len(callables) != 0 and len(kwcallables) == 0:

        def f(arg):
            result = []
            for c in callables:
                result.append(c(arg))
            return tuple(result)

        return f
    if len(callables) == 0 and len(kwcallables) == 0:

        def f(args):
            return f

    raise AssertionError(
        "You should either pass all named or all not-named arguments")


def add(a, b): return a + b


def subtr(a, b): return a - b


def multiply(a, b): return a * b


def mcify(obj):
    if isinstance(obj,dict):
        return Dict({k: mcify(obj[k]) for k in obj})
    if isinstance(obj, set):
        
        return Set({mcify(k) for k in obj})
    if isinstance(obj, list):
        
        return List([mcify(k) for k in obj])
    return obj

def choose(i):
    def func(x):
        return x[i]
    return func

