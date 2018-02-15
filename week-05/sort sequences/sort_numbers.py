from datastubs import NUMBER_LIST


def reverse_numerical_order():
    """
    Sort the list of numbers but in reverse order
    """
    return sorted(NUMBER_LIST, reverse=True)


def numerical_order():

    return sorted (NUMBER_LIST)
    """
    Sort the list of numbers in numerical order
    """
    # fill it out

def as_absolute_value(): 
    """
    The absolute value of a number `n` is its value
    regardless of positive or negative sign
    """
    # fill it out
    return sorted(NUMBER_LIST, key = abs)


def as_inverse_number():
    """
    An inverse of a number `n` is defined as: `1/n`
    The bigger the number, the smaller its inverse, and vice versa
    """
    def foo(x):
        return 1/x
    inverselist = []
    return sorted(NUMBER_LIST, key = foo)




