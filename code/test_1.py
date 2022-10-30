c = {'_id': 1, '_title': 'Python ООП', '_author': 'Балакирев', '_year': 2022}


lst = [f'{i[0]}: {i[1]}' for i in c.items()]
print('\n'.join(lst))

# [print(f'{i[0]}: {i[1]}') for i in c.items()]