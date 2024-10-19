from random import randint

class RN:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return randint(1, 10)
        else:
            raise StopIteration


rn = RN(3)

# print(next(rn))
# print(next(rn))
# print(next(rn))
# print(next(rn))

for item in RN(5):
    print(item)