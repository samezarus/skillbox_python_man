def fibo(num):
    cur_val, new_val = 0, 1

    for _ in range(num):
        yield cur_val
        cur_val, new_val = new_val, cur_val + new_val




for item in fibo(10):
    print(item)

