import time

import requests
import json
import datetime


def email_send():
    url = "http://osb.smec-cn.com/CommonService/MessageService/DFStageMessageService"

    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = json.dumps({
        "key": "9304",
        "sendContent": "管梯APP测试情况",
        "title": "上海中心项目管梯APP{}测试情况".format(time),
        "toUsers": "yingkai.zhao@definesys.com",
        "toCopyEmails": "",
        "toSecretEmails": "",
        "token": "hovaqbtvuyOpFmqUVZVGYpEERtLCXHGJ",
        "type": "EMAIL"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
def etext_send():
    url = "http://osb.smec-cn.com/CommonService/MessageService/DFStageMessageService"

    payload = json.dumps({
        "token": "hovaqbtvuyOpFmqUVZVGYpEERtLCXHGJ",
        "type": "SMS",
        "toUsers": "17752821932",
        "sendContent": "",
        "key": "kerry1",
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

if __name__ == "__main__":
    etext_send()
