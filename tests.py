import unittest

import manipulatron


class Test1(unittest.TestCase):
    def test_string_converted_to_upper_case(self):
        self.assertEqual("HELLO", manipulatron.upper("hello"))

    def test_string_converted_to_lower_case(self):
        self.assertEqual("hello", manipulatron.lower("HELLO"))
