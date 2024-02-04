import unittest
import requests
import importlib
import json

# TODO figure out the output problems here


# dynamically run test cases 
class TestAPI(unittest.TestCase):
    base_url = "http://localhost:5000"

    # Dynamically generate test methods
    def run_parametrized_test(self, JSON_test_cases ):
        test_cases = json.loads(JSON_test_cases)
        # Iterate over test cases and dynamically generate test methods
        for test_case in test_cases['tests']:
            endpoint = test_case['endpoint']
            params = test_case['params']
            expected_result = test_case['expected_result']

            # Make HTTP POST request to the API endpoint
            response = requests.post(f"{self.base_url}/functions/{endpoint}", json={"params": params})
            data = response.json()

            # Assert the response matches the expected result
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data["result"], expected_result)
           
if __name__ == '__main__':
    unittest.main()