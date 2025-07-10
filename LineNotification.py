import requests
import json

def sendMessage(text,access_token,user_id):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    content = {
        'to': user_id,
        'messages': [
            {
                'type': 'text',
                'text': text
            }
        ]
    }
    requests.post(url,headers = headers,data = json.dumps(content))
