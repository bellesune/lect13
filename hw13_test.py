# TODO get 100% test coverage for hw13.py

import unittest
import hw13
from hw13 import my_func

KEY_ITERATION = "iteration"
KEY_INITIAL = "initial"
KEY_SECOND = "second"
KEY_EXPECTED = "expected"
KEY_OUTPUT = "length"

class SplitTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_ITERATION: 0,
                KEY_INITIAL: 1,
                KEY_SECOND: 2,
                KEY_EXPECTED: {
                    KEY_OUTPUT: "Don't iterate",
                }
            },
            {
                KEY_ITERATION: 3,
                KEY_INITIAL: 1,
                KEY_SECOND: 2,
                KEY_EXPECTED: {
                    KEY_OUTPUT: "counter is 10",
                }
            },
            {
                KEY_ITERATION: 3,
                KEY_INITIAL: 0,
                KEY_SECOND: 2,
                KEY_EXPECTED: {
                    KEY_OUTPUT: "initial is 0",
                }
            },
        ]
         
        self.failure_test_params = [
            {
                KEY_ITERATION: "",
                KEY_INITIAL: 0,
                KEY_SECOND: 2,
                KEY_EXPECTED: {
                    KEY_OUTPUT: "Don't iterate",
                }
            },
        ]

    def test_split_success(self):
        for test in self.success_test_params:
            response = hw13.my_func(test[KEY_ITERATION], test[KEY_INITIAL], test[KEY_SECOND])
            expected = test[KEY_EXPECTED]
             
            self.assertEqual(response, expected[KEY_OUTPUT])
            
    def est_split_failure(self):
        for test in self.failure_test_params:
            response = hw13.my_func(test[KEY_ITERATION], test[KEY_INITIAL], test[KEY_SECOND])
            expected = test[KEY_EXPECTED]
        
            self.assertNotEqual(response, expected)
            

if __name__ == '__main__':
    unittest.main()