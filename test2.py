import unittest
from cal import addNumbers, subNumbers 

class unoTest2(unittest.TestCase):
    def testPositiveNumbers(self):
        self.assertEqual(addNumbers(5,5), 10)



if __name__ == '__main__':
    unittest.main()