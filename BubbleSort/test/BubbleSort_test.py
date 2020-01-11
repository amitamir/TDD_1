import unittest

from src.BubbleSort import BubbleSort

class BubbleSortTest(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_BubbleSortReturnValue(self):
        arr = [1, 3, 2, 5]
        expected = [1, 2, 3, 5]
        result = BubbleSort.BubbleSort(arr)
        self.assertEqual(expected, result)

    def test_BubbleSortWithOutValues(self):
        arr = []
        expected = []
        result = BubbleSort.BubbleSort(arr)
        self.assertEqual(expected, result)

    def test_BubbleSortNotLost(self):
        arr = [8, 10, 5,  3, 4]
        expected = [3, 4, 5, 8, 10]
        result = BubbleSort.BubbleSort(arr)
        self.assertEqual(expected, result)

    def test_BubbleSortValid(self):
        arr = [2, 2, 3, 6, 0, 1]
        expected = [0, 1, 2, 2, 3, 6]
        result = BubbleSort.BubbleSort(arr)
        self.assertEqual(expected, result)


