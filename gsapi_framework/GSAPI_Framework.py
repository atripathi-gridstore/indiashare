'''
Created on May 5, 2016

@author: atripathi
'''

import requests
import json
import urllib
from ApiError import ApiError
from GSAPI_Base import GSAPI_Base
from GSAPI_Storage import GSAPI_Storage

class GSAPI_Framework(GSAPI_Storage):
    '''
    classdocs
    '''


    def __init__(self, host, port):
        '''
        Constructor
        '''
        GSAPI_Base.__init__(self, host, port)

if __name__ == "__main__":
    api = GSAPI_Framework('10.100.37.153', '12309')
    print 'GS API Login - ', api.login()
    nodes = api.storagenode_get()