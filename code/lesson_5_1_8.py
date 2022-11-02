lst = [8, 11, 'abcd', -7.5, 2.0, -5]
# lst_in = input().split()
print(sum(map(int, filter(lambda x: x.strip('-').isdigit(), input().split()))))

