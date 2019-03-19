import unittest
from unitTests.backend.helpers import TestSimilarityMeasures
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSimilarityMEasures))
    return suite
   
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run (test_suite)