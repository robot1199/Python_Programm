def input_int_numbers():
    try:
        return list(map(int, input().split()))
    except TypeError:
        raise TypeError('все числа должны быть целыми')


while True:
    try:
        print(*input_int_numbers())
        break
    except TypeError:
        pass
