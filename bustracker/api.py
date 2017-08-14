__author__ = 'Henry Webster <hwebster@mail.depaul.edu>'
__date__ = '2 August 2017'

import urllib.request
import urllib.parse
import json
import sys

class Api(object):
    """
    CTABusTracker API
    """

    def __init__(self, api_key=None):
        """
        Construct with api key and build the skeleton of a request URL
        """

        self.api_key = api_key
        self.request_template = 'http://www.ctabustracker.com/bustime/api/v2/{}/?key={}{}&format=json'

    def getTime(self):
        """
        Returns the current system time
        """

        url = self._buildUrl('gettime')
        return self._sendRequest(url)
   
    def getVehiclesById(self, vids, tmres='m'):


        if tmres not in ('m','s'):
            raise RuntimeError('\'tmres\' parameter can only be \'m\' or \'s\'.')
	
        url = self._buildUrl('getvehicles', {'vid': vids, 'tmres': tmres})
        return self._sendRequest(url)

    def getVehiclesByRoute(self, rts, tmres='m'):
        """
        Returns the most-recent status for each vehicle
        """

        if tmres not in ('m','s'):
            raise RuntimeError('\'tmres\' parameter can only be \'m\' or \'s\'.')
		
        url = self._buildUrl('getvehicles', {'rt': rts, 'tmres': tmres})
        return self._sendRequest(url)
   
    def getRoutes(self):
        """
        Returns the entire list of bus routes serviced by the CTA by number and name designation
        """

        return self._sendRequest(self._buildUrl('getroutes'))

    def _sendRequest(self, url):
        """
        sends the request to the API over HTTP
        """
        
        return json.loads(urllib.request.urlopen(url).read().decode())

    def _buildUrl(self, page, parameters=None):
        """
        create the full URL for the API request
        """

        p = str()
        
        if parameters is not None:
        
            for param in parameters:
                p = p + '&{}={}'.format(param, ','.join(map(str, parameters[param])))
            

        return self.request_template.format(page, self.api_key, p)



    def _error(self, error):

        print('cta-bustracker-python: error: {}'.format(error[0]['msg']))
        sys.exit(1)
       
