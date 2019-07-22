
import json
import requests
import sys
 
url = 'https://oapi.dingtalk.com/robot/send?access_token=a25324cafc5b0f2bb239b5e56c71e7f378f570a3d281160dbec9e4f8c4a7e493'


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
    content = input('please input message\n')
    content = sys.argv[1]
    WriteLogByDing(content)
