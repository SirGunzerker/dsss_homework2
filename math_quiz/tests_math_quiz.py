import unittest
from math_quiz import Random_max_min_selector, Random_return_operator, perform_math_operation


class TestMathGame(unittest.TestCase):

    def test_Random_max_min_selector(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = Random_max_min_selector(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_Random_return_operator(self):
        # Test if the operator generated is either of the three options
        operators = {'+', '-', '*'}
         # Use the choice function from the random module to randomly select an operator from the list
        selected_operator = Random_return_operator()
        self.assertTrue(selected_operator in operators)
    def test_perform_math_operation(self):
        test_cases = [
        (5, 2, '+', '5 + 2', 7), 
        (9, 3, '-', '9 - 3', 6), 
        (4, 2, '*', '4 * 2', 8)
            ]
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            result = perform_math_operation(num1, num2, operator)
            expected_result= (expected_problem, expected_answer)
            self.assertEqual(result, expected_result)
if __name__ == "__main__":
    unittest.main()
