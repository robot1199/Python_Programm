class Test:
    def __init__(self, descr):
        if not 10 <= len(descr) <= 10_000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super(TestAnsDigit, self).__init__(descr)
        if type(ans_digit) not in (float, int) or \
                type(max_error_digit) not in (float, int) or\
                max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')

        self.ans_digit = ans_digit
        self.max_error_digit = max_error_digit

    def run(self):
        ans = float(input())
        return self.ans_digit - self.max_error_digit <= ans <= self.ans_digit + self.max_error_digit


descr, ans = map(str.strip, input().split('|'))

ans = float(ans)

try:
    test = TestAnsDigit(descr, ans)
    res = test.run()
    print(res)
except ValueError as e:
    print(e)
