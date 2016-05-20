'''
Created on May 4, 2016

@author: atripathi
'''
import requests
import json
import urllib
from ApiError import ApiError
from GSAPI_Base import GSAPI_Base
import time 

class GSAPI_Storage(GSAPI_Base):
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
    
    def storagenode_count (self):
        api = 'grid/storagenode/count'
        auth_api = self._initurl(api)
        print 'getting storage node ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        #print resp_obj['access_token']
        
        return resp_obj
    
    def storagenode_shutdown (self, node, reboot=False):
        api = 'grid/storagenode/shutdown'
        auth_api = self._initurl(api, {'nodeid': node, "reboot": reboot})
        print 'shutdown storage node ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        #print resp_obj['access_token']
        
        return resp_obj

if __name__ == "__main__":
    api = GSAPI_Storage('10.100.37.153', '12309')
    print 'GS API Login - ', api.login()
    nodes = api.storagenode_get()
    for item in nodes :
        print 'node - ', item['NodeID'], ' IsSyncOrchestrator -- ', item['IsSyncOrchestrator']
        if item['IsSyncOrchestrator'] is False:
            print 'shutting down node', item['NodeID']
            api.storagenode_shutdown(item['NodeID'], True)
            print 'sleeping for 60 seconds'
            time.sleep(30);

    print 'GS API grid/storagenode/get ', api.storagenode_get()
    print 'GS API grid/storagenode/count ', api.storagenode_count() 
       
    print 'GS API Logout - ', api.logout()
    
    