
class Man:
    def __init__(self, name):
        # self.name - это сеттер
        self.name = name

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


if __name__ == '__main__':
    man = Man('XMan')
    print(man)

    # через сеттер назначаем новое имя
    man.name = "123"
    print(man)


