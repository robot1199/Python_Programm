lst_in = input().split()

def f(x):
    try:
        int(x)
        return True
    except:
        return False

print(sum(list(map(int, (filter(f, lst_in))))))