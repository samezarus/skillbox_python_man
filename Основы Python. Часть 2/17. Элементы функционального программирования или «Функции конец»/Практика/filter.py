from typing import List

if __name__ == '__main__':
    list1 = [15, 7, 13, 19, 52, 64]

    # Фильтрация список на чётные числа
    result = filter(lambda x: x%2==0, list1)
    print(result)

    for item in result: print(item)

    # Или можно результат завернуть сразу в список
    print()

    result: List[int] = list(filter(lambda x: x % 2 == 0, list1))
    print(result)


