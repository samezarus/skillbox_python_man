from typing import List


users: List[str] = ["user5", "user3", "user20", "user9", "user10", "user6", "user2"]


def str_to_int(item: str) -> int:
    return int(item[4:])


if __name__ == '__main__':
    # Сортировка по коду символа
    print(sorted(users))

    # Сортировка по ключу в виде функции
    print(sorted(users, key=str_to_int))

    # Сортировка по ключу в виде лямбда-функции
    print(sorted(users, key=lambda item: int(item[4:])))