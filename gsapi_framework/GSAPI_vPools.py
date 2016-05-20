'''
Created on May 19, 2016

@author: kdesai
'''

import json
import time 
import urllib

import requests

from ApiError import ApiError
from GSAPI_Base import GSAPI_Base


class GSAPI_vPools(GSAPI_Base):
    '''
    classdocs
    '''
    
    def __init__(self, host, port):
        '''
        Constructor
        '''
        GSAPI_Base.__init__(self, host, port)
        
    def vpool_count (self):
        api = 'grid/vpool/count'
        auth_api = self._initurl(api)
        print 'getting vpool count ', auth_api
        #print 'headers -- ', self._get_authheader()
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        print resp_obj
        
        return resp_obj
        
    def vpool_get (self):
        api = 'grid/vpool/get'
        auth_api = self._initurl(api)
        print 'getting vPools ', auth_api
        resp = requests.get(auth_api,  headers=self._get_authheader())
        if resp.status_code != 200:
            print resp
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        # pretty printing of json-formatted string
        print json.dumps(resp_obj, sort_keys=True, indent=4)
        
        return resp_obj
    
    def storagenode_vpool_get (self,vPoolID):
        api = 'grid/vpool/storagenode/get'
        auth_api = self._initurl(api, {'VPoolID': vPoolID})
        print 'Get Storage Nodes of a vPool ', auth_api
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
    
    def create_vpool_post(self,physicalpoolid ,name,optimizationsetting , qossetting, protectionsetting , grouptype ):
        api = 'grid/vpool/create'
        auth_api = self._initurl(api, {'name': name,'physicalpoolid ': physicalpoolid , 'optimizationsetting':optimizationsetting,'qossetting':qossetting,'protectionsetting':protectionsetting,'grouptype':grouptype })
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
    
    
    def update_vpool_post(self,vPoolID,name,optimizationsetting , qossetting, protectionsetting , grouptype ):
        api = 'grid/vpool/update'
        auth_api = self._initurl(api, {'VPoolID': vPoolID, 'name': name,'optimizationsetting':optimizationsetting,
                                       'qossetting':qossetting,'protectionsetting':protectionsetting,'grouptype':grouptype })
        print 'Update vPool API ', auth_api
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
    
    
    
    def rebalance_vpool_post(self,vPoolID):
        api = 'grid/vpool/rebalance'
        auth_api = self._initurl(api, {'vpoolid': vPoolID })
        print 'Rebalance vPool API ', auth_api
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
    
    
    def storagenode_vpool_get (self,vPoolID):
        api = 'grid/vpool/storagenode/get'
        auth_api = self._initurl(api, {'VPoolID': vPoolID})
        print 'Get Storage Nodes of a vPool ', auth_api
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
    
   
    
if __name__ == "__main__":
    api = GSAPI_vPools('10.100.37.153', '12309')
    print 'GS API Login - ', api.login()
    #count = api.vpool_count()
    nodes = api.vpool_get()
    #create_vpool_post(self,physicalpoolid ,name,optimizationsetting , qossetting, protectionsetting , grouptype )
    api.create_vpool_post('86b10100-31c3-4d18-9b3e-f51fcce053d0','vPool-new',0,0,0,0)
    """
    for item in nodes :
        api.storagenode_vpool_get(item['VPoolID'])
    """
       
    print 'GS API Logout - ', api.logout()