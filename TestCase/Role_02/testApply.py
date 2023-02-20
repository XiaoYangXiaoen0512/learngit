import requests
import json


# 获取应用access_token
def get_access_token():
    url = 'http://10.20.12.64:30612/xdap-app/event/trigger/external?eventId=6333b7ae87b7e21912f74d80&tenantId=362554500273143809'
    header = {

    }

    payload = {

    }

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    print(response, dict1)


if __name__ == "__main__":
    get_access_token()