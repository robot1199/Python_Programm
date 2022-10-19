def privet_2(func):
    def wraper(value):
        return func(value) * value
    return wraper

@privet_2
def privet(value):
    return value ** 2

print(privet(5))