import requests
import json
import datetime
import hashlib


def get_accesstoken():
    client_id = '6ab22ae9-4531-43d9-ba1e-b514b0c40ff2'
    client_secret = '020f8c2b-d4a8-4822-84a9-898e8a95f486'
    url = 'https://gams.geely.com/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
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
    # userId = "100293710681222414336"  # 黄丽梅id
    # userId = "100293738068861517824"  # qinyi
    # userId = "100293713534607425536"  # cailiyuan
    # userId = '100293709793963540480'  # liuxinghong
    userId = '100386856690823200768'  #gaojunchao
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
    url = 'https://gams.geely.com/xdap-open/token/accountToken?token={}&account={}'.format(actoken, accout)
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
    accout = "0125194"  # 黄丽梅账号
    # accout = "0222697"  # qinyi
    # accout = "0052698"  # cailiyuan
    # accout = '0000297'  # liuxinghong
    accout = '0379638'
    get_tokenbyaccout(accout)
