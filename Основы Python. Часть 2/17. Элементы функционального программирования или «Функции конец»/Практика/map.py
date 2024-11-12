from typing import List

if __name__ == '__main__':
    list1: List[int] = [12, 2, 6, 8, 15, 22]
    list2: List[int] = [3, 5, 7, 11, 37, 42]

    result = map(lambda x, y: x + y, list1, list2)
    print(result)

    for item in result: print(item)

    # Или можно результат завернуть сразу в список
    print()

    list_result: List[int] = list(map(lambda x, y: x + y, list1, list2))
    print(list_result)