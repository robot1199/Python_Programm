class Validator:
    def __init__(self):
        pass

    def _is_valid(self, data):
        raise NotImplementedError('в классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value


    def __call__(self, data):
        return self._is_valid(data)

    def _is_valid(self, data):
        if type(data) != float or not (self.min_value <= data < self.max_value):
            return False
        return True
