# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, state, speed=1):
        self.x = 0
        self.y = 0
        self.state = state
        self.speed = speed

    def set_unit(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'UP':
            self.set_unit(y=self.y + self.speed, x=self.x)
        elif direction == 'DOWN':
            self.set_unit(y=self.y - self.speed, x=self.x)
        elif direction == 'LEFT':
            self.set_unit(y=self.y, x=self.x - self.speed)
        elif direction == 'RIGTH':
            self.set_unit(y=self.y, x=self.x + self.speed)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'crawl':
            return self.speed * 0.5
