import unittest

# To run the python test file directly, we will need to add base folder
# to the path, else it will not be able to import test subject properly
# Will also allow for auto discovery from inside the tests folder
import sys
sys.path.insert(0, '..\\..\\..\\')

from _22_UnitTesting._01_CmdlnAndFixtures.src.simpleCalculator import Calculator

from parameterized import parameterized, parameterized_class

class TestSimpleCalc_1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass()")
        cls.calc = Calculator(0, 0)

    def setUp(self):
        print("In setUp()")
        self.calc.a = 8
        self.calc.b = 4

    def tearDown(self):
        print("In tearDown()")
        self.calc.a = 0
        self.calc.b = 0

    @ classmethod
    def tearDownCzlass(cls):
        print("In tearDownClass()")
        del cls.calc


    @parameterized.expand([
        (8, 4, 12),
        (1, 2, 3),
        (5, 3, 8)
    ])
    def test_simpleadd(self, num1, num2, sum):
        self.calc.a = num1
        self.calc.b = num2
        self.assertEqual(sum, self.calc.add())

    def test_simplesub(self):
        self.calc = Calculator(8, 4)
        self.assertEqual(4, self.calc.sub())

    def test_simplesubFail(self):
        self.calc = Calculator(8, 4)
        self.assertEqual(4, self.calc.sub())


@unittest.skip
class TestSimpleCalc_2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass() method")
        cls.calc = Calculator(1, 2)

    @classmethod
    def tearDownClass(cls):
        del cls.calc
        print("In tearDownClass() method")

    def setUp(self):
        print("In setUp() method")
        self.calc.a = 8
        self.calc.b = 4

    def tearDown(self):
        self.calc.a = 0
        self.calc.b = 0
        print("In tearDown() method")

    '''[(a, b, res), (a, b, res), (a, b, res), (a, b, res)]
    def test_simpleadd(self):
        self.assertEqual(12, self.calc.add())

        #sub-test
        for i in range(10):
            with self.subTest(i=i):
                # Test code
                pass
    '''

    def test_simpleadd_5_3(self):
        self.calc.a = 5
        self.calc.b = 3
        self.assertEqual(8, self.calc.add())

    def test_simplesub(self):
        self.assertEqual(4, self.calc.sub())

    def test_simplesubFail(self):
        self.assertNotEqual(5, self.calc.sub())


if __name__ == '__main__':
    unittest.main()
