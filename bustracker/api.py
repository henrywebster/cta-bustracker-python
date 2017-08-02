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
        self._verifyGetTime(url)
        return self._sendRequest(url)
   
    def getVehiclesById(self, vids, tmres='m'):


        url = self._buildUrl('getvehicles', {'vid': vids, 'tmres': tmres})
        self._verifyGetVehicles(url)
        return self._sendRequest(url)

    def getVehiclesByRoute(self, rts, tmres='m'):
        """
        Returns the most-recent status for each vehicle
        """

        url = self._buildUrl('getvehicles', {'rt': rts, 'tmres': tmres})
        self._verifyGetVehicles(url)
        return self._sendRequest(url)
    
    def _sendRequest(self, url):
        return self._RequestUrl('getvehicles', {param: vals})
    
    def _RequestUrl(self, page, params=None):
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

    def _verifyGetTime(self, url):
        """
        Make sure the get time url is valid for the API call
        """

        parsedUrl = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)

        #   TODO fix
        return True

    def _verifyGetVehicles(self, url):
        

        parsedUrl = urllib.parse.parse_qs(urllib.parse.urlsplit(url).query)

        if 'vid' and 'rt' in parsedUrl:
            return False

        return True

    def _error(self, error):

        print('cta-bustracker-python: error: {}'.format(error[0]['msg']))
        sys.exit(1)
       
