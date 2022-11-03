x, y = input().split()

try:
    c = int(x) + int(y)
except:
    try:
        c = float(x) + float(y)
    except:
        c = x + y
finally:
    print(c)