from models.rectangle import Rectangle
"""import statement"""

class Square(Rectangle):
    """documetation"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    def __str__(self):
        """returning the values"""
        return f"[Square] ({self.id}) {self.x}/{self.y}, {self.height}"
