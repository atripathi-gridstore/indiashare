'''
Created on May 4, 2016

@author: atripathi
'''

import requests
import json
import urllib
from ApiError import ApiError

class GSAPI_Base():
    '''
    classdocs
    '''
    _host = ''
    _port = 0
    _access_token = None
    _refresh_token = None
    
    def __init__(self, host, port):
        print "test data"
        self._host = host
        self._port = port
    
    def _initurl(self, api_cat, urlparams=None):
        http_params = ''
        if urlparams is not None:
            print urlparams
            http_params = '?' + urllib.urlencode(urlparams)
            
        return 'http://{}:{}/{}{}'.format(self._host, self._port, api_cat,http_params);
    
    def _get_authheader (self):
        headers = { 'Content-Type':'application/x-www-form-urlencoded'};
        if self._access_token is not None:
            headers['Authorization'] = 'Bearer {}'.format(self._access_token);
            
        return headers
    
    
    
    
    def login (self):
        api = 'authorize'
        auth_api = self._initurl(api)
        print 'Log in to GS system ', auth_api
        print 'Headers -- ', self._get_authheader()
        user_data = 'username=hercules&password=gridstore&grant_type=password'
        resp = requests.post(auth_api, data=user_data, headers=self._get_authheader(),)
        if resp.status_code != 200:
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        resp_obj = resp.json()
        #print resp_obj['access_token']
        self._access_token = resp_obj['access_token']
        self._refresh_token = resp_obj['refresh_token']
        
        return resp_obj['access_token']

    def logout (self):
        api = 'grid/user/logout'
        auth_api = self._initurl('grid/user/logout', {'refreshtoken':str(self._refresh_token)})
        print 'Logout of GS system ', auth_api
        headers = self._get_authheader()
        print 'headers -- ', headers
        resp = requests.post(auth_api, headers=headers)
        if resp.status_code != 200:
            print resp.status_code
            #     This means something went wrong.
            raise ApiError(resp.status_code, 'POST {} / {}'.format(api, resp.status_code))
        
        #print resp_obj
        return 'success'
        
if __name__ == "__main__":
    api = GSAPI_Base('172.16.47.10', '12309')
    print 'GS API Login - ', api.login()
    print 'GS API Logout - ', api.logout()
    
    