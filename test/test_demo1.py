import unittest
from lesson1.demo1 import add
from lesson1.demo1 import multiply


class MyTestCase(unittest.TestCase):

    def test_add(self):
        x = 3
        y = 4
        z = add(x, y)
        self.assertEqual(z, 7, 'method add failed')

    def test_multiply(self):
        x = 3
        y = 4
        z = multiply(x, y)
        self.assertEqual(z, 12, 'method multiply failed')

if __name__ == '__main__':
    unittest.main()
