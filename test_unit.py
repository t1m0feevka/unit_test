import unittest
import unit


class TestUnit(unittest.TestCase):
    def setUp(self):
        """Set Up for test"""
        print('homework-test', self.shortDescription())

    def test_check(self):
        """test check doc"""
        self.assertTrue(unit.check(2, 1))

    def test_div(self):
        """test div doc"""
        self.assertEqual(unit.div(6, 2), 3)

    def test_check_upper(self):
        """test check upper doc"""
        self.assertEqual(unit.check_upper('Привіт'), 'ПРИВІТ')


if __name__ == '__main__':
    unittest.main()
