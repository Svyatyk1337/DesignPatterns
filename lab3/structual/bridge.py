class Color:
    def apply_color(self):
        pass

class RedColor(Color):
    def apply_color(self):
        return "Applying red color"

class BlueColor(Color):
    def apply_color(self):
        return "Applying blue color"

class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return f"Drawing circle. {self.color.apply_color()}"

class Square(Shape):
    def draw(self):
        return f"Drawing square. {self.color.apply_color()}"