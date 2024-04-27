class Rectangle:
    pass

class Square(Rectangle):
    def __init__(self, size):
        self._size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        def area(self):
            return self.size ** 2
        def __str__(self):
            return f"[Square] {self._size}/{self._size}"

