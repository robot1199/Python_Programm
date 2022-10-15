def veryfi_num(st):
    if not all(x.isdigit() for x in st):
        raise ValueError("в строке должны быть только цифры")
    print('yes')


veryfi_num('123456789r')
