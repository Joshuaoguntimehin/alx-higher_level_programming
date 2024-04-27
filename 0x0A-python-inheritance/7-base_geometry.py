class BaseGeometry:
    """
    Ensures that the given value is an integer. If not, raises a TypeError with a specific error message.

    Parameters:
    - value: The value to check.
    - name: The name of the variable (assumed to always be a string).

    Raises:
    - TypeError: If 'value' is not an integer.
    """
    def area(self):
       raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
