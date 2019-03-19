import .....backend.helpers.SimilarityMeasures 
import unittest

class TestSimilarityMeasures(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print 'called once before any tests in class'

    @classmethod
    def tearDownClass(cls):
        print '\ncalled once after all tests in class'

    def setUp(self):
        pass
   
    def tearDown(self):
        pass

    def test1(self):
        """One"""
        self.assertTrue(True)
   
    def test2(self):
        """Two"""
        self.assertTrue(False)
      
if __name__ == '__main__':
    unittest.main()