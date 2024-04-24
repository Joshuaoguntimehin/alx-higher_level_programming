class Base:
     def __init__(self, width, height, x=0, y=0):
         self.width = width
         self.height = height
         self.x = x
         self.y = x
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0,):
        super().__init__(width, height, x, y)
    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, width):
        if width >= 0:
            raise TypeError("width must be an integer")
        elif not isinstance(width, int):
            raise ValueError("width must be > 0")
        self.__width = width
 
    """ Getter and setter for height"""
    @property
    def height(self):
        return self.__height
      
    @height.setter
    def set_height(self, height):
        if height >= 0:
            raise TypeError("height must be an integer")
        elif not isinstance(height, int):
            raise ValueError("height must be > 0")
        self.__height = height

    """ Getter and setter for x"""
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <0:
            raise ValueError("x must be >= 0")
        self.__x = value
     
    """ Getter and setter for y"""
    @property
    def y(self):
        return self.__y
        
    
    @y.setter
    def y(self, y):
        if value <0:
            raise ValueError(" must be >= 0")
        self.__y = y
