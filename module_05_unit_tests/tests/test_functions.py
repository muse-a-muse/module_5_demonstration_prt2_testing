"""
Description: Module 05 demonstration: Functions with Unit Testing
Author: ACE Faculty
Date: {current date}
Usage: To execute the unit tests: 
        From the unit_testing directory in the Terminal:
        python -m unittest -v tests/test_functions.py
    To execute the python src program:
        From the unit_testing directory in the Terminal:
        python src/functions.py
"""

import unittest
from unittest.mock import patch

from src.functions import greet_name_age

class TestFunctions(unittest.TestCase):
    def test_greet_name_with_all_parameters(self):
        # Arrange
        # [define my variables]
        name = "Joe"
        age = 25
        expected = "Hello Joi, you are 25 years old!"
        # note: spelled Joe incorrectly to show failed test.

        # Act
        # [run the code you're testing]
        # Act
        actual = greet_name_age(name, age)
        # Assert
        # [compare expected output with output from the act phase]
        self.assertEqual(expected, actual)
