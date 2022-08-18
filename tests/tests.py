import unittest
from unittest import mock
import script.hi
import numpy as np
import os


# @mock.patch.dict(os.environ, {"NAME": "Sial"})
class Test(unittest.TestCase):
    def test1(self):

        x = script.hi.say_hi(os.environ.get('NAME'))
        self.assertEqual(x, np.array([1]))