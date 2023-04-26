import requests
import json
import datetime
import hashlib


def get_accesstoken():
    client_id = 'd1b50b03-5418-49f7-bbcb-6a1987f1250b'
    client_secret = 'b677e34c-8615-4b8e-97e7-ba71147e75be'
    url = 'https://zcode.zeekrlife-test.com/quality-zeekr-tqmp/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
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
    #userId = "100390501107509493760"  # 范玉涛id
    userId = "100434185964848414720"
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
    url = 'https://zcode.zeekrlife-test.com/quality-zeekr-tqmp/xdap-open/token/accountToken?token={}&account={}'.format(actoken, accout)
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

def get_accesstoken_gongshi():
    client_id = 'dad3f081-987a-4aec-8481-f32ce8d52234'
    client_secret = 'cd07d7a0-112e-4962-aeb4-c0f0b2cf9920'
    url = 'https://zcode.zeekrlife-test.com/quality-gongshi-test/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
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

def get_tokenbyaccout_gongshi(accout):
    actoken = get_accesstoken()
    url = 'https://zcode.zeekrlife-test.com/quality-gongshi-test/xdap-open/token/accountToken?token={}&account={}'.format(actoken, accout)
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
    accout = "e-xuepei.zhang"
    get_tokenbyaccout_gongshi(accout)
