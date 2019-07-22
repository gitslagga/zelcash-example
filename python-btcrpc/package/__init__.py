
import json
import requests
from .setting import *
 
url = DINGDING_URL


def WriteLogByDing(content):
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
        response = requests.post(url= url, headers= headers, data= sendData)
        content = response.content.decode()
        print(content)
    except Exception as ex:
        print('Dingding send message error: {}'.format(ex))
 
if __name__ == '__main__':
    content = input('please input message')
    
    WriteLogByDing(content)
