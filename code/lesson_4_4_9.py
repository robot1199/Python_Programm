class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._verify_line(model)
        for i in (mass, speed, top):
            self._verify_num(i)
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def _verify_line(self, value):
        if type(value) != str:
            raise TypeError('неверный тип аргумента')

    def _verify_num(self, value):
        if not type(value) in (int, float):
            raise TypeError('неверный тип аргумента')
        if value <= 0:
            raise TypeError('неверный тип аргумента')

    def _veryfi_int(self, value):
        if type(value) != int:
            raise TypeError('неверный тип аргумента')





class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super(PassengerAircraft, self).__init__(model, mass, speed, top)
        self._verify_num(chairs)
        self._veryfi_int(chairs)
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super(WarPlane, self).__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons



planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]