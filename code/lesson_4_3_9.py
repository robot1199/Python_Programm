class SoftList(list):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __getitem__(self, item):
        if item > len(self.__class__.__dict__):
            return False
        return self.value[item]

sl = SoftList("python")
sl[0] # 'p'
sl[-1] # 'n'
sl[6] # False
sl[-7] # False