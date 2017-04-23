import functools
import sys


def memoize(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        args_ = (args, tuple(kwargs.items()))
        if not hasattr(func, "dic"):
            func.dic = dict()
        if args_ not in func.dic:
            func.dic[args_] = func(*args, **kwargs)
        return func.dic[args_]

    return decorator


exec(sys.stdin.read())

'''
print(fib(3))
print(fib(200))'''
