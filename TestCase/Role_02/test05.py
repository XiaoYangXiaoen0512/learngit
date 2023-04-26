import requests
import json


def get_access_token():
    client_id = 'd1b50b03-5418-49f7-bbcb-6a1987f1250b'
    client_secret = 'b677e34c-8615-4b8e-97e7-ba71147e75be'
    url = 'https://zcode.zeekrlife-test.com/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(client_id, client_secret)
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
    actoken = get_access_token()
    userId = "100169876816012509184"
    url = 'http://zcode.zeekrlife-test.com/xdap-open/token/userToken?token={}&userId={}'.format(actoken, userId)
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


def get_process():
    url = 'https://zcode.zeekrlife-test.com/quality-zeekr-tqmp/xdap-open/open/process/v1/singleSuspend'
    header = {
        "Content-Type": "application/json",
        "Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ4ZGFwYXBwaWQiOiI0MDAzMTAzMDQ3MzIzNDg0MTYiLCJleHAiOjE2ODExODUwMjAsImlhdCI6MTY3OTk3NTQyMCwieGRhcHRlbmFudGlkIjoiMzg4NjQ0NTA4MTM4NDcxNDI1IiwieGRhcHVzZXJpZCI6IjEwMDM5MDA4MTk5ODYwNzA4OTY2NCJ9._GG1aAH6rlRM24ApDtyYdtMrHejt_fNGLTPqpuy5sdUA9QtdfKUwG-5LS4lxFq_z6WdNFg4QKiKVSFdXWYkSeA"
    }

    payload = json.dumps({
        "documentId": "428518196975372544",
        "formId": "64216625fe82be5c00308e93",
        "instanceId":"3015064",
        "nodeId": "BPMN_fe48bc67c90f6fd2"
})

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    # dict1 = dict(json_music)
    # actoken = dict1["access_token"]
    # print(response, dict1)
    # return actoken
    return json_music


if "__main__" == __name__:
    token = get_process()
    print(token)