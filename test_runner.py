import unittest

# Import the test class containing test cases
from Test.test_comments import TestCollection

# Load the test cases
test_loader = unittest.TestLoader()
test_suite = test_loader.loadTestsFromTestCase(TestCollection)

# Run the tests
test_runner = unittest.TextTestRunner()
test_result = test_runner.run(test_suite)


# Check if the tests ran successfully
if test_result.wasSuccessful():
    print("All tests passed successfully!")
else:
    print("Some tests failed or encountered errors.")
