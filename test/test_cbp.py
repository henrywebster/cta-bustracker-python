import sys
import os

import json
import urllib.request
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import bustracker



class CBPTest(unittest.TestCase):
    
    def setUp(self):
        

        self.api_key = ''   #   secret api key added via command line
        self.request_base = 'http://ctabustracker.com/bustime/api/v2/'

        self.api = bustracker.Api(self.api_key)

    def test_getTime(self):
        
        response = self.api.getTime()
        self.assertIn('tm', response['bustime-response'])

    def test_getVehiclesByIdSeconds(self):
	
        response = self.api.getVehiclesById(['1103','1192'], tmres='s')
        self.assertIn('vehicle', response['bustime-response'])
	
    def test_getVehiclesByIdMinutes(self):

		
        response = self.api.getVehiclesById(['1103','1192'], tmres='m')
        self.assertIn('vehicle', response['bustime-response'])
	
    def test_getVehiclesByIdExceptionRaised(self):

        #	check invalid tmres parameter raises runtime exception
        self.assertRaises(RuntimeError, self.api.getVehiclesById, ['2000'], tmres='x')
		
	# add a test for list of numbers	

    def test_getVehiclesByRoute(self):

        response = self.api.getVehiclesByRoute(['66','70'])
        self.assertIn('vehicle', response['bustime-response'])
		
    def test_getRoutes(self):

        response = self.api.getRoutes()
        self.assertIn('routes', response['bustime-response'])

    def test_getDirectionsByInt(self):

        response = self.api.getDirections(8)
        self.assertIn('directions', response['bustime-response'])

    def test_getDirectionsByString(self):

        response = self.api.getDirections('9')
        self.assertIn('directions', response['bustime-response'])

    def test_getDirectionsExceptionRaised(self):

        self.assertRaises(RuntimeError, self.api.getDirections, ['9', 22])
    

if __name__ == '__main__':
    unittest.main()

