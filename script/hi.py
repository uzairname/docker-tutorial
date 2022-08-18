import numpy as np

def say_hi(name):

    if not isinstance(name, str):
        raise TypeError("name must be a string, got {}".format(type(name)))

    print(f'Hi, {name}')

    return np.array([1])
