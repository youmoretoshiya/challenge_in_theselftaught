class Square:
    square_list = []
    def __init__(self, l):
        self.len = l
        self.square_list.append((self.len))

    def print(self):
        print("{} by {} by {} by {}".format(self.len, self.len, self.len, self.len))

square1 = Square(8)
square1.print()
