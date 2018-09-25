
from mc import Dict, List

def chain(*callables):
    def f(arg):
        result = arg
        for c in callables:
            result = c(result)
        return result

    return f


def mux(*callables,**kwcallables):
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

    raise AssertionError("You should either pass all named or all not-named arguments")

add = lambda a,b: a + b

subtr = lambda a,b: a - b

multiply = lambda a,b: a * b

