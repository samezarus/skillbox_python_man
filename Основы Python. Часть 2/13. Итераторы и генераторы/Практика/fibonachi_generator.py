def fibo(num):
    result = list()

    cur_val, new_val = 0, 1

    for _ in range(num):
        result.append(cur_val)
        cur_val, new_val = new_val, cur_val + new_val

    return result


print(fibo(100))
print(8 in fibo(100))
