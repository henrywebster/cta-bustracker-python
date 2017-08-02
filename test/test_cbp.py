import sys
import os

import json
import urllib.request
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bustracker



class CBPTest(unittest.TestCase):
    
    def setUp(self):
        
        self.api_key = ''  #   add secret API key
        self.request_base = 'http://ctabustracker.com/bustime/api/v2/'

        self.api = bustracker.Api(self.api_key)

    def test_getTime(self):
        
        response = self.api.getTime()
        self.assertIn('tm', response)



if __name__ == '__main__':
    unittest.main()

