import sys
import functools
import traceback


def retry_method(n=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            num = 0
            while num <= n:
                try:
                    num += 1
                    func(*args, **kwargs)
                    return
                except AssertionError:
                    if num <= n:
                        trace = sys.exc_info()
                        traceback_info = ""
                        for trace_line in traceback.format_exception(trace[0], trace[1], trace[2], 3):
                            traceback_info += trace_line
                        print(traceback_info)
                        args[0].tearDown()
                        args[0].setUp()
                    else:
                        raise
        return wrapper
    return decorator


def retry_class(n=0, prefix="Test"):
    def retry(cls):
        for name, func in list(cls.__dict__.items()):
            if hasattr(func, "__call__") and name.startswith(prefix):
                setattr(cls, name, retry_method(n)(func))

        return cls

    return retry
