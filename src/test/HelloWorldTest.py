'''
Created on May 2, 2015

@author: lamd
'''
import unittest
import random
from main.HelloWorld import *


class Test(unittest.TestCase):

    def testHelloWorld(self):
        self.assertEqual("Hello World", helloWorld(), "helloWorld failed")

    def testSum2(self):
        self.assertEqual(5, sum2(2, 3), "Sum Failed")
        self.assertEqual(4, sum2(2, 2), "Sum Failed")
        self.assertEqual(10, sum2(7, 3), "Sum Failed")
        self.assertEqual(90, sum2(40, 50), "Sum Failed")
        self.assertEqual(15, sum2(7, 8), "Sum Failed")
        self.assertEqual(0, sum2(1, -1), "Sum Failed")
        self.assertEqual(0, sum2(0, 0), "Sum Failed")

    def testDistance(self):
        self.assertEqual(0, distance(0, 0, 0, 0), "Distance Failed")
        self.assertEqual(6, distance(3, 3, 9, 3), "Distance Failed")
        self.assertEqual(31, distance(30, 2, -1, 8), "Distance Failed")
        self.assertEqual(2, distance(1, 1, 2, 3), "Distance Failed")

    def testSummation(self):
        listOfInts = []
        for k in range(3):
            listOfInts.append(random.randint(1, 100))

        self.assertEqual(sum(listOfInts), summation(listOfInts), "Summation Failed")

    def testCombineStrint(self):
        self.assertEqual("HelloWorld", combineString("Hello", "World"), "combineString Failed")
        self.assertEqual("RainFall", combineString("Rain", "Fall"), "combineString Failed")
        self.assertEqual(":-)", combineString(":-", ")"), "combineString Failed")

    def testDivisibleByTwo(self):
        self.assertEqual(True, divisibleByTwo(2), "divisibleByTwo failed")
        self.assertEqual(True, divisibleByTwo(4), "divisibleByTwo failed")
        self.assertEqual(True, divisibleByTwo(108), "divisibleByTwo failed")
        self.assertEqual(True, divisibleByTwo(10008), "divisibleByTwo failed")
        self.assertEqual(False, divisibleByTwo(3), "divisibleByTwo failed")
        self.assertEqual(False, divisibleByTwo(7), "divisibleByTwo failed")
        self.assertEqual(False, divisibleByTwo(901), "divisibleByTwo failed")
        self.assertEqual(False, divisibleByTwo(90000001), "divisibleByTwo failed")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testHelloWorld']
    unittest.main()
