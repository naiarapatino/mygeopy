import numbers

def hypot(a,b):
    '''
    Compute the hypotenuse of a right triangle.

    args:
        a: length of one side (must be a non-negative real number)
        b: length of the other side (must be a non-negative real number)
    returns:
        The length of the hypotenuse (a non-negative real number)

    examples:
        >>> hypot(3, 4)
        5.0
        >>> hypot(5, 12)
        13.0

    '''


    if not (isinstance(a, numbers.Real) and isinstance(b, numbers.Real)):
        raise TypeError("Arguments must be real numbers")
    if a < 0 or b < 0:
        raise ValueError("Arguments must be non-negative")
    return (a**2 + b**2)**0.5
