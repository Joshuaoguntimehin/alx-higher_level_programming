class square:
    def __init__(self, size):
        self.size = self
        @property
    def size(self):
            return self._size
        @size.setter
    def size(self, value):
            self._size = value
            try:
                if not isinstance(value, int):
                    raise TypeError("size must be an integer")
                if size < 0:
                    raise ValueError("size must be >= 0")
            self._size = value
    def __init__(self, size=0):
            self.size = 0
    def area(self):
            return self._size ** 2
    def my_print(self):
            for _ in range(self._size):
                print("#" * self._size)
                try:
                    if size = 0:
                        print()
