class Fibo:
    def __init__(self, num):
        self.__num = num
        # self.__cur_val = 0
        # self.__new_val = 1
        # self.__counter = 0
        self.reinit()

    def reinit(self):
        self.__cur_val = 0
        self.__new_val = 1
        self.__counter = 0

    def __iter__(self):
        self.reinit()
        return self

    def __next__(self):
        self.__counter += 1

        if self.__counter > 1:
            if self.__counter > self.__num: raise StopIteration

            self.__cur_val, self.__new_val = self.__new_val, self.__cur_val + self.__new_val

            # tmp = self.__cur_val
            # self.__cur_val = self.__new_val
            # self.__new_val = tmp + self.__new_val

        return self.__cur_val


fibo_cl = Fibo(100000)

# for item in fibo_cl:
#     print(item)

print(10 in fibo_cl)