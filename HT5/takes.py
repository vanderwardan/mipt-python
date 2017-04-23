import functools
import sys


def takes(*types):
    def decorator(function):
        @functools.wraps(function)
        def decorated(*args, **kwargs):
            tuple_ = args + tuple(kwargs)
            len1 = len(types)
            len2 = len(tuple_)
            for i in range(min(len1, len2)):
                if type(tuple_[i]) != types[i]:
                    raise TypeError
            result = function(*args, **kwargs)
            return result

        return decorated

    return decorator


exec(sys.stdin.read())

'''
print(sum(1, 1))
print(sum(1))'''
