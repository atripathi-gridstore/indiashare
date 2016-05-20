'''
Created on May 4, 2016

@author: atripathi
'''

class ApiError(RuntimeError):
    '''
    Holder class for API Erro
    '''
    msg = 'success'
    code = 200
    
    def __init__(self, http_error, message):
        '''
        Constructor
        '''
        self.msg = message
        self.code = http_error