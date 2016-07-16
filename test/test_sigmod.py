import unittest
from lesson1.sigmoid import sigmoid


class MyTestCase(unittest.TestCase):
    def test_sigmoid(self):
        self.assertEqual(sigmoid(37), 1.0, 'method sigmod failed');
        self.assertEqual(sigmoid(-37), 0, 'method sigmod failed');

        self.assertEqual(sigmoid(38), 1.0, 'method sigmod failed');
        self.assertEqual(sigmoid(-38), 0, 'method sigmod failed');

        self.assertEqual(sigmoid(1e-16), 0.5, 'method sigmod failed');
        self.assertEqual(sigmoid(-1e-16), 0.5, 'method sigmod failed');

        self.assertEqual(sigmoid(1e-17), 0.5, 'method sigmod failed');
        self.assertEqual(sigmoid(-1e-17), 0.5, 'method sigmod failed');


if __name__ == '__main__':
    unittest.main()
