import functools

from typing import Callable, Any

from time import time


def timer(func: Callable) -> Callable:

    @functools.wraps(func)  # Для проксирования документации из 'func'
    def wrapped_func(*args, **kwargs) -> Any:
        start_t = time()

        ##############################
        result = func(*args, **kwargs)
        ##############################

        stop_t = time()

        work_t = stop_t - start_t

        print(f"Функция '{func.__name__}' работала {work_t} сек.")

        return result

    return wrapped_func


@timer
def myfunc():
    mylist = [i*3 for i in range(100000)]


if __name__ == '__main__':
    myfunc()