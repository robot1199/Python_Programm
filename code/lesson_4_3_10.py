class StringDigit(str):
    def __init__(self, st):
        super().__init__()
        self._veryfi_num(st)
        self.st = st

    @staticmethod
    def _veryfi_num(st):
        if all(x.isdigit() for x in st):
            return
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self._veryfi_num(other)
        return StringDigit(self.st + other)

    def __radd__(self, other):
        self._veryfi_num(other)
        return StringDigit(other + self.st)


sd = StringDigit("123")
print(sd)
sd = sd + "456"
print(sd)
sd = "789" + sd
print(sd)
sd = sd + "12f"
print(sd)
