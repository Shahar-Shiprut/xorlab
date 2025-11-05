from typing import Callable

def retry(func: Callable):
    def inner():
        while True: 
            res = func()
            if res is not None:
                return res

    return inner
