def inherits_from(obj, a_class):
    """
    Check if the object 'obj' is an instance of a class that inherited (either directly or
    indirectly) from 'parent_class'.

    Parameters:
        obj (object): The object to check.
        parent_class (type): The parent class to check against.

    Returns:
        bool: True if 'obj' is an instance of a class that inherited from 'parent_class',
              otherwise False.
    """
    if  isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    else:
        return False
