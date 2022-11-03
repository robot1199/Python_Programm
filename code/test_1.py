def get_div(x, y):
    try:
        res = x / y
        return res
    except ZeroDivisionError:
        res = 100
        return res
    finally:
        res = -1
        print(f"finally: {res}")

print(get_div(1, 0))