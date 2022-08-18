import unittest
import script.hi
import numpy as np
import os

class Test(unittest.TestCase):
    def test1(self):

        x = script.hi.say_hi(os.environ.get('NAME'))
        self.assertEqual(x, np.array([1]))