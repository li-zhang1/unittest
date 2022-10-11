import unittest
from my_calculator import calculator
class test_cal(unittest.TestCase):
    
    def test_calculator(self):
        num1 = 8
        num2 = 4
        cal = calculator(num1, num2)
        result_add = cal.add()
        result_sub = cal.sub()
        result_mul = cal.mul()
        result_div = cal.div()
        self.assertEqual(result_add, 12)
        self.assertEqual(result_sub, 4)
        self.assertEqual(result_mul, 32)
        self.assertEqual(result_div, 2)
    
    def test_add(self):
        num1, num2 = 1, 2
        cal = calculator(num1, num2)
        result = cal.add()
        self.assertEqual(result,3)
    def test_sub(self):
        num1 = 5
        num2 = 3
        cal = calculator(num1, num2)
        result=cal.sub()
        self.assertEqual(result,2)
    def test_mul(self):
        num1 = 3
        num2 = 5
        cal = calculator(num1, num2)
        result=cal.mul()
        self.assertEqual(result,15)
    def test_div(self):
        num1 = 8
        num2 = 2
        cal = calculator(num1, num2)
        result = cal.div()
        self.assertEqual(result,4)


    
if __name__ == "__main__":
    unittest.main()
    