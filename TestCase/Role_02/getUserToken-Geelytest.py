import requests
import json
import datetime
import hashlib


def get_accesstoken():
    client_id = '38823f6e-cf7f-4bc5-95e4-52cb41b762df'
    client_secret = '9e6728fc-eec2-4737-8425-ba508489552d'
    url = 'https://geely-ams.test.geely.com/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        client_id, client_secret)
    header = {
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "client_id": "{}".format(client_id),
        "client_secret": "{}".format(client_secret),
        "grant_type": "client_credentials"
    })

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    actoken = dict1["access_token"]
    print(response, dict1)
    return actoken


def get_token():
    actoken = get_accesstoken()
    userId = "100259163972685529088"  # 金梦恩id
    url = 'https://gams.geely.com/xdap-open/token/userToken?token={}&userId={}'.format(actoken, userId)
    header = {
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "token": "{}".format(actoken),
        "userId": "".format(userId)
    })

    response = requests.request("GET", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    token = dict1["access_token"]
    print(response, dict1)
    return token


def get_tokenbyaccout(accout):
    actoken = get_accesstoken()
    url = 'https://geely-ams.test.geely.com/xdap-open/token/accountToken?token={}&account={}'.format(actoken, accout)
    header = {
        "Content-Type": "application/json",
    }

    payload = json.dumps({
        "token": "{}".format(actoken),
        "userId": "".format(accout)
    })

    response = requests.request("GET", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    token = dict1["access_token"]
    print(response, dict1)
    return token


if __name__ == "__main__":
    accout = "0310721"  # 金梦恩账号
    get_tokenbyaccout(accout)
