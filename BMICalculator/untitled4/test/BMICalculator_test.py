import unittest
from src.BMICalculator import BMICalculator

class BMICalculatorTest(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription



    def test_calculateBMI_forHealthy(self):
        # Capture the results of the function
        weight = 78
        height = 190
        result = BMICalculator.CalculateBMI(weight, height)
        BMICalculator.choose(result)
        # Check for expected output
        self.assertEqual(21.61, result)

    def test_calculateBMI_forUnderweight(self):
        # Capture the results of the function
        weight = 58
        height = 180
        result = BMICalculator.CalculateBMI(weight, height)
        BMICalculator.choose(result)
        # Check for expected output
        self.assertEqual(17.90, result)

    def test_calculateBMI_forSeverelyUnderweight(self):
        # Capture the results of the function
        weight = 47
        height = 173
        result = BMICalculator.CalculateBMI(weight, height)
        BMICalculator.choose(result)
        # Check for expected output
        self.assertEqual(15.70, result)

    def test_calculateBMI_forOverweight(self):
        # Capture the results of the function
        weight = 89
        height = 181
        result = BMICalculator.CalculateBMI(weight, height)
        BMICalculator.choose(result)
        # Check for expected output
        self.assertEqual(27.17, result)

    def test_calculateBMI_forSeverelyOverweight(self):
        # Capture the results of the function
        weight = 98
        height = 179
        result = BMICalculator.CalculateBMI(weight, height)
        BMICalculator.choose(result)
        # Check for expected output
        self.assertEqual(30.59, result)



if __name__ == '__main__':
    unittest.main()
