class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reflect_about_X(self):
        self.y *= -1

    def reflect_about_Y(self):
        self.x *= -1

    def scale(self, s):
        self.x, self.y = s * self.x, s * self.y

    def add(self, V):
        v = Vector(0, 0)
        v.x = self.x + V.x
        v.y = self.y + V.y
        return v

    def print_info(self):
        print(f'({self.x},{self.y})')
