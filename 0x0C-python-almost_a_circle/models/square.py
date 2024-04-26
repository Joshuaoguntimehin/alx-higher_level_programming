from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(x=x, y=y, width=size, height=size, id=id)

    def __str__(self):
        return f"[Square] (<id>) <x>/<y> - <size>"
