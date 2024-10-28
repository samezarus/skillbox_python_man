def fibo(num):
    cur_val, new_val = 0, 1

    for _ in range(num):
        yield cur_val
        cur_val, new_val = new_val, cur_val + new_val

        # Прерывание по условию
        if cur_val > 10 ** 5:
            return


def square(nums):
    """
    Генератор квадрата каждого элемента последовательности

    :param nums:
    :return:
    """

    for num in nums:
        yield num ** 2


for item in fibo(10000000):
    print(item, end=' ')

print("\n")

print(sum(square(fibo(10000000))))

