from abc import ABC, abstractmethod


class Model:
    @abstractmethod
    def get_pk(self):
        raise TypeError

    def get_info(self):
        return f'Базовый класс Model'


class ModelForm(Model):
    __ID = 0

    def __init__(self, login, password):
        self._login = login
        self._password = password
        self._id = self.__ID
        ModelForm.__ID += 1

    def get_pk(self):
        return self._id

form = ModelForm("Логин", "Пароль")
print(form.get_pk())
print(form.get_info())
