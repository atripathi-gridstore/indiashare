'''
Created on May 20, 2016

@author: kdesai
'''

import json
import time 
import urllib

import requests

from ApiError import ApiError
from GSAPI_Base import GSAPI_Base

class GSAPI_Systemcheck(GSAPI_Base):
    '''
    classdocs
    '''
    
    def __init__(self, host, port):
        '''
        Constructor
        '''
        GSAPI_Base.__init__(self, host, port)
        
    def storagenode_get (self):
        api = 'grid/storagenode/get'
        auth_api = self._initurl(api)
        print 'getting storage node ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
         # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def host_get (self):
        api = 'grid/host/get'
        auth_api = self._initurl(api)
        print 'getting host ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
         # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def configuration_profile_get (self):
        api = 'grid/profile/configuration/get'
        auth_api = self._initurl(api)
        print 'getting configuration profile ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
         # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def maskingset_get (self):
        api = 'grid/maskingset/get'
        auth_api = self._initurl(api)
        print 'getting maskingsets ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
         # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    
if __name__ == '__main__':
    api = GSAPI_Systemcheck('10.100.37.153', '12309')
    print 'GS API Login - ', api.login()
    nodes = api.maskingset_get()
   
       
    print 'GS API Logout - ', api.logout()