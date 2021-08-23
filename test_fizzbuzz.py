import unittest  # This is the default Python testing library, unittest

from fizzbuzz import generate 
from fizzbuzz import fizzbuzz #importing method (generate) from file (fizbuzz)

class TestFizzBuzz(unittest.TestCase): # Sets up a new test case
    def test_lists_values_upto_one(self):   # This is a test, don't forget `self`!
        self.assertEqual(generate(1), 1) # And an assertion

    def test_lists_values_up_to_two(self):
        self.assertEqual(generate(2), 1, 2)

    def test_fizz(self):
         for num in [3, 6, 9]:
           print("testing if fizz replaces", num)
           assert fizzbuzz(num) == "fizz"

    def test_buzz(self):
         for num in [5, 10, 20]:
           print("testing if buzz replaces", num)
           assert fizzbuzz(num) == "buzz"             

    def test_fizzbuzz(self):
         for num in [15, 30, 45]:
           print("testing if fizzbuzz replaces", num)
           assert fizzbuzz(num) == "fizzbuzz"               

 