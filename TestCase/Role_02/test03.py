import requests
import json
import datetime
import hashlib
def get_work():
    url = "http://10.20.13.13:30613/xdap-app/event/trigger/external?eventId=63212df853dc304dca644c5b&tenantId=353575397822038017"
    header = {
    }

    payload = json.dumps({
            "a": [
                {
                    "CheckProject": "AWBbefore",
                    "CheckTask": "R",
                    "Remark": "Redaverage"
                },
                {
                    "CheckProject": "AWBbefore",
                    "CheckTask": "B",
                    "Remark": "Blueaverage"
                }]})

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    print(response, dict1)


if __name__ == "__main__":
    get_work()