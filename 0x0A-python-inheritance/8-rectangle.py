class BaseGeometry:
    pass
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        if type(height) !=int:
            raise TypeError("height must be an integer")

