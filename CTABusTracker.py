import urllib.request
import json


from cbp_enums import APIRequest

class API(object):
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
    
    
    def _RequestUrl(self, url):
        """
        sends the request to the API over HTTP
        """
        
        # rURL = '%s/%s/?key=%s&format=%s' % (self.request_base, url, self.api_key, self.response_format)
        rURL = '{}/{}/?key={}&format={}'.format(self.request_base, url, self.api_key, self.response_format)

        return json.loads(urllib.request.urlopen(rURL).read().decode())['bustime-response']
         
       
