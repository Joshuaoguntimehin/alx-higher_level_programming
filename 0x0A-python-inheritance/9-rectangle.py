class BaseGeometry:
    pass
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self._width = width
        self._height = height
        if  type(width) != int:
            raise TypeError(f"{width} must be greater than 0")
    def area(self):
        """Return the area of the rectangle."""
        return self._width * self._height
    def __str__(self):
        """Return the rectangle description in the specified format."""
        return f"[Rectangle] {self._width}/{self._height}"

