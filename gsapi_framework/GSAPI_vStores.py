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


class GSAPI_vSstores(GSAPI_Base):
    '''
    classdocs
    '''
    
    def vstore_get (self):
        api = 'grid/vstore/get'
        auth_api = self._initurl(api)
        print 'getting vstores ', auth_api
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
    
    
    def hosts_per_vstore_get (self,vstoreid ):
        api = 'grid/vstore/host/get'
        auth_api = self._initurl(api, {'vstoreid': vstoreid })
        print 'Get Hosts per vStore API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def start_vstore_post (self,vstoreid ):
        api = 'grid/vstore/start'
        auth_api = self._initurl(api, {'vstoreid': vstoreid })
        print 'Start vStore API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    
    def stop_vstore_post (self,vstoreid ):
        api = 'grid/vstore/stop'
        auth_api = self._initurl(api, {'vstoreid': vstoreid })
        print 'Stop vStore API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def remove_vstore_post (self,vstoreid ):
        api = 'grid/vstore/remove'
        auth_api = self._initurl(api, {'vstoreid': vstoreid })
        print 'Stop vStore API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def expand_vstore_post (self,vstoreid,newsize,maxsize ):
        api = 'grid/vstore/expand'
        auth_api = self._initurl(api, {'vstoreid': vstoreid,'newsize':newsize, 'maxsize':maxsize  })
        print 'Expand vStore API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    
    def create_vstore_post(self,vStoreName, vPoolID,sizeGB):
        api = 'grid/vstore/create'
        auth_api = self._initurl(api, {'vStoreName' : vStoreName, 'vpoolid': vPoolID, 'sizegb':sizeGB })
        print 'Create vPool API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def rename_vstore_post(self,vStoreName, vStoreID):
        api = 'grid/vstore/rename'
        auth_api = self._initurl(api, {'vStoreName' : vStoreName, 'vstoreid': vStoreID})
        print 'Rename vPool API ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.post(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code,'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def __init__(self, host, port):
        '''
        Constructor
        '''
        GSAPI_Base.__init__(self, host, port)

if __name__ == '__main__':
    api = GSAPI_vSstores('10.100.37.153', '12309')
    print 'GS API Login - ', api.login()
    #"VStoreID": "6cf69b6c-a1aa-4c71-b091-62219ccbd083"
    nodes = api.expand_vstore_post('1214f492-ab80-4cf7-b7c2-823a734b09e0', 2048, 0)
    """
    for item in nodes :
        api.hosts_per_vstore_get(item['VStoreID'])
    """
    print 'GS API Logout - ', api.logout()