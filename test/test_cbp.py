import sys
import os

import json
import urllib.request
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bustracker



class CBPTest(unittest.TestCase):
    
    def setUp(self):
        
        self.api_key = '9s9kctLMdftQ4UB2sdPjG26g8'  #   add secret API key
        self.request_base = 'http://ctabustracker.com/bustime/api/v2/'

        self.api = bustracker.Api(self.api_key)

    def test_getTime(self):
        
        response = self.api.getTime()
        self.assertIn('tm', response['bustime-response'])

    def test_getVehicleById(self):

        response = self.api.getVehiclesById(['1147','1192'])
        self.assertIn('vehicle', response['bustime-response'])

    def test_getVehiclesByRoute(self):

        response = self.api.getVehiclesByRoute(['66','70'])
        self.assertIn('vehicle', response['bustime-response'])


if __name__ == '__main__':
    unittest.main()

