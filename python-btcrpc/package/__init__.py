# from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

import json
import requests
from .setting import *

# def getConnection():
#     return AuthServiceProxy('http://%s:%s@%s:%s'%(RPC_HOST, RPC_PASSWORD, RPC_HOST, RPC_PORT))

def SendDingDing(content):
    headers = {
        'Content-Type': 'application/json',
        'Charset': 'utf-8'
    }
    request_data = {
        'msgtype': 'text',
        'text': {
            'content': content
        },
        'at': {
            'atMobiles': [],
            'isAtAll': True
        }
    }

    try:
        sendData = json.dumps(request_data)
        response = requests.post(url= DINGDING_URL, headers= headers, data= sendData)
        content = response.content.decode()
        print(content)
    except Exception as ex:
        print('Dingding send message error: {}'.format(ex))
 
