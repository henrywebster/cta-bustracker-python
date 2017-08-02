import urllib.request
import json
import sys

class Api(object):
    """
    CTABusTracker API
    """

    def __init__(self, api_key=None, response_format='json'):

        self.api_key = api_key
        self.response_format = response_format.lower()
        self.request_base = 'http://www.ctabustracker.com/bustime/api/v2/'

    def getTime(self):
        """
        Returns the current system time
        """

        return self._RequestUrl('gettime')
   
    def getVehicles(self, param, vals, tmres='m'):
        """
        Returns the most-recent status for each vehicle
        """

        return self._RequestUrl('getvehicles', {param: vals})

    
    def _RequestUrl(self, page, params=None):
        """
        sends the request to the API over HTTP
        """
        
        p = str()
        for param in params:
            p = p + '&{}={}'.format(param, ','.join(map(str, params[param])))


        url = '{}/{}/?key={}{}&format={}'.format(self.request_base, page, self.api_key, p, self.response_format)
        print(url)

        
        response = json.loads(urllib.request.urlopen(url).read().decode())['bustime-response']
        
        if 'error' not in response:
            return response
        else:
            self._error(response['error'])


    def _error(self, error):

        print('cta-bustracker-python: error: {}'.format(error[0]['msg']))
        sys.exit(1)
       
