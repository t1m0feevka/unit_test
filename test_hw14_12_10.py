import unittest
import hw14_12_10


class TestUnit(unittest.TestCase):

    def test_func1(self):
        a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        list = []
        result = [1, 2, 3, 5, 8, 13]
        self.assertEqual(hw14_12_10.func1(a, b, list), result)

    def test_func2(self):
        text = 'I am a good developer. I am also a writer'
        result1 = 5
        self.assertEqual(hw14_12_10.func2(text), result1)

    def test_func3(self):
        g = 9
        self.assertTrue(hw14_12_10.func3(g))
        self.assertFalse(hw14_12_10.func3(12))


if __name__ == '__main__':
    unittest.main()

