import unittest
import script.hi
import numpy as np
import os

class Test(unittest.TestCase):
    def test1(self):

        self.assertGreater(len(os.environ.get('NAME')), 0)

        x = script.hi.say_hi(os.environ.get('NAME'))
        self.assertEqual(x, np.array([1]))