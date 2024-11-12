import re


if __name__ == '__main__':
    s = "AUE - Hello world"

    print("-" * 20)

    # Поиск в начале строки по шаблону (r - сырая строка)
    r = re.match(r"AUE", s)
    print(r)
    print(r.group())
    print(r.start())
    print(r.end())

    print("-" * 20)

    # Поиск в строке по шаблону
    r = re.search(r"Hello", s)
    print(r)

    print("-" * 20)

    # Поиск в строке всех вхождений шаблона
    r = re.findall(r"l", s)
    print(r)

    print("-" * 20)

    # Поиск всего найденного на шабон
    r = re.sub(r"l", "L", s)
    print(r)

    print("-" * 20)

    # Сбор регулярных выражений в объект
    s2 = "London is a capital of"

    pattern = re.compile("l")

    r = pattern.findall(s)
    print(r)

    r2 = pattern.findall(s2)
    print(r2)
