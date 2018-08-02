# tests.py

import os
import sys

# so code in the test dir can see the code in the src dir
testdir = os.path.dirname(__file__)
srcdir = '../src'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest                                                                  
from mock import patch, MagicMock    
import classB #necessary to import classB                                  
from classB import B #convenient to import B                                            


class TestAlib(classB.Alib):

    def _get_a(self):
         return 4
    def _get_b(self):
        return 5
    def _get_c(self):
        return 6


class TestClassB(unittest.TestCase):                                       
    
    @patch('classB.Alib')                                            
    def test_execute(self, mock_alib):
        # Create a new MagickMock instance which will be the
        # `return_value` of our patched object
        mock_alib.return_value = MagicMock(side_effect=TestAlib)()   

        my_b = B()
        self.assertEqual( my_b.dowork(), 15 )



if __name__ == '__main__':
    unittest.main()