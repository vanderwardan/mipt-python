import functools
import sys
import time


def profiler(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        if sys._getframe().f_back.f_code.co_name != func.__name__:
            decorator.calls = 0
        decorator.calls += 1

        begin = time.time()
        result = func(*args, **kwargs)
        decorator.last_time_taken = time.time() - begin

        return result

    decorator.calls = 0
    return decorator


'''
task()
print(task.calls)'''
