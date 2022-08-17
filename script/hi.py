import numpy as np

def print_hi(name):

    np.array([1])

    if not isinstance(name, str):
        raise TypeError("name must be a string, got {}".format(type(name)))

    print(f'Hi, {name}')