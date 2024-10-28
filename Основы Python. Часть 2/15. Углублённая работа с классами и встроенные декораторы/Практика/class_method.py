"""
cls - это непосредственно сам класс !
"""


class Main:
    COUNT_HELLOW = 0

    def __init__(self):
        self.x = 0

class Simple(Main):
    def __init__(self):
        super().__init__()

    @classmethod
    def func(cls):
        cls.COUNT_HELLOW += 1

        print("Hellow")

if __name__ == '__main__':
    simple = Simple()
