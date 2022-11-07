class ValidatorString:
    def __init__(self, min_length, max_length, chars):
        self.min_length = min_length
        self.max_length = max_length
        self.chars = chars

    def is_valid(self, string):
        if not (self.min_length <= len(string) <= self.max_length) or\
                self.chars and not any(x in self.chars for x in string):
            raise ValueError('недопустимая строка')
        return string




class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.login_validator = login_validator
        self.password_validator = password_validator
        self._login = None
        self._password = None

    def form(self, request):
        if not request.get('login') or not request.get('password'):
            raise TypeError('в запросе отсутствует логин или пароль')
        self._login = self.login_validator.is_valid(request.get('login'))
        self._password = self.password_validator.is_valid(request.get('password'))

login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = input().split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)