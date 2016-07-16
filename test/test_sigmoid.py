import unittest
from lesson1.sigmoid import sigmoid
from math import e


class MyTestCase(unittest.TestCase):
    def test_sigmoid(self):
        msg = 'method sigmoid failed'
        self.assertEqual(sigmoid(37), 1.0, msg);
        self.assertEqual(sigmoid(-37), 0, msg);

        self.assertEqual(sigmoid(38), 1.0, msg);
        self.assertEqual(sigmoid(-38), 0, msg);

        self.assertEqual(sigmoid(1e-16), 0.5, msg);
        self.assertEqual(sigmoid(-1e-16), 0.5, msg);

        self.assertEqual(sigmoid(1e-17), 0.5, msg);
        self.assertEqual(sigmoid(-1e-17), 0.5, msg);

        self.assertEqual(sigmoid(0), 0.5, msg);

        self.assertEqual(sigmoid(1), e/(1+e), msg);
        self.assertEqual(sigmoid(-1), 1/(1+e), msg);


if __name__ == '__main__':
    unittest.main()
