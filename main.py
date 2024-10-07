def counter(*objects):
    sum_ = 0
    for i in list(*objects):
        if isinstance(i, list):  # если i список суммируем i и полученное число прибавляем к sum_
            sum_ += (counter(i))
        elif isinstance(i, dict):  # если i словарь суммируем
            sum_ += counter(list(i.items()))
        elif isinstance(i, tuple):  # если i кортеж суммируем
            sum_ += counter(list(i))
        elif isinstance(i, set):  # если i множество суммируем
            sum_ += counter(list(i))
        elif isinstance(i, int):  # если i число суммируем
            sum_ += i
        else:  # суммируем длину i
            sum_ += len(i)
    return sum_


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(counter(data_structure))