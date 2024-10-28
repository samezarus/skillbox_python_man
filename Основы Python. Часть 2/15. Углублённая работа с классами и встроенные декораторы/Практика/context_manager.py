from time import time


class Timer:
    def __init__(self) -> None:
        print("Время работы кода")
        self.start = None

    def __enter__(self) -> 'Timer':
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time() - self.start)

        # Пропуск конкретного типа ошибок
        # if exc_type is TypeError:
        #     return True

        # Пропуск любых ошибок
        return True


if __name__ == '__main__':
    with Timer() as t1:
        x = 1000 * 1000 ** 1000000
        x += 'qwerty'