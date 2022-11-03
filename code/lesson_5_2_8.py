def get_loss(w1, w2, w3, w4):
    try:
        return 10 * w1 // w2 - 5 * w2 * w3 + w4
    except:
        return 'деление на ноль'
    else:
        return 10 - 5 * w2 * w3 + w4

print(get_loss(4, 0, 6, 8))