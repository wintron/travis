import unittest

import travis


class Test1(unittest.TestCase):
    def test_string_converted_to_upper_case(self):
        self.assertEqual("HELLO", travis.upper("hello"))
        
    def test_string_converted_to_lower_case(self):
        self.assertEqual("hello", travis.lower("HELLO"))
