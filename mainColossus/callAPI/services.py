import os
import requests
import json
from . import sdk

# try:
#   from sdk import VRClient
# except ImportError, e:
#   import sys
#   print 'Import error:', e
#   print 'sys.path:', sys.path
#   blah = __import__('sdk')
#   print 'sdk is %r' % sdk
#   try:
#     print 'sdk is at %s (%s)' % (sdk.__file__, sdk.__path__)
#   except Exception, e:
#     print 'Cannot give details on sdk (%s)' % e



userID='606116'
apiKey='522a9427e6872ecc6464b25d7af6c948'

def callAPI():
    # make some dummy data in order to call vedic rishi api
    data = {
        'date': 10,
        'month': 12,
        'year': 1993,
        'hour': 1,
        'minute': 25,
        'latitude': 25,
        'longitude': 82,
        'timezone': 5.5
    }

    # api name which is to be called
    resource = "general_ascendant_report"

    # instantiate VedicRishiClient class
    client = sdk.VRClient(userID, apiKey)
    # client.matchMakingCall()

    # call horoscope apis
    responseData = client.call(resource, data['date'], data['month'], data['year'], data['hour'], data['minute'], data['latitude'], data['longitude'], data['timezone'])

    loaded_json = json.loads(responseData.text)

    # print(loaded_json)  # <== prints json response.

    # print(loaded_json['ascendant'])  # <== prints single key
    return loaded_json['asc_report']['ascendant']