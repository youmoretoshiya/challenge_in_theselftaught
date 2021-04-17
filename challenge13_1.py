class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def what_am_i(self):
        print("I am a shape")
        
class Rectangle(Shape):
    def calculate_perimeter(self):
        return (self.width + self.len) * 2

class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, diff):
        self.len += diff

a_rectangle = Rectangle(10, 15)
print(a_rectangle.calculate_perimeter())
a_rectangle.what_am_i()

a_square = Square(10)
print(a_square.calculate_perimeter())
a_square.what_am_i()
a_square.change_size(3)
print(a_square.calculate_perimeter())
