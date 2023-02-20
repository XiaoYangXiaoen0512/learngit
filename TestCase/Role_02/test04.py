import requests
import json
import time


# 同步平台类型人员信息
def get_platform_user():
    xdaptoken = get_token()
    print(xdaptoken)
    url = "http://10.20.13.13:30607/xdap-admin/platform/synchronization/user"
    datatime = int(round(time.time() * 1000))
    header = {
        "xdaptimestamp": "{}".format(datatime),
        "Content-Type": "application/json",
        "xdaptoken": "{}".format(xdaptoken)
    }

    payload = json.dumps([
        {
            "account": "Durant002",
            "username": "杜兰特2号",
            "password": "welcome1",
            "phone": "17752825637",
            "email": "Durant002@qq.com"
        },
        {
            "password": "welcome1",
            "account": "Durant003",
            "username": "杜兰特3号",
            "phone": "17752827637",
            "email": "Durant003@qq.com"
        }
    ])

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    print(datatime, response, dict1)


# 同步租户类型人员信息
def get_tenant_user():
    xdaptoken = get_token()
    url = "http://10.20.13.13:30607/xdap-app/department/api/create/user"
    datatime = int(round(time.time() * 1000))
    header = {
        "xdaptenantid": "353575397822038017",
        "xdaptimestamp": "{}".format(datatime),
        "Content-Type": "application/json",
        "xdaptoken": "{}".format(xdaptoken)
    }

    payload = json.dumps(
        {
            "apiAddUsrDtoList": [
                {
                    "account": "Durant002",
                    "username": "杜兰特2号",
                    "password": "welcome1",
                    "phone": "16652825637",
                    "email": "Durant002@qq.com",
                    "userNumber": "A02"
                },
                {
                    "password": "welcome1",
                    "account": "Durant003",
                    "username": "杜兰特3号",
                    "phone": "16652827637",
                    "email": "Durant003@qq.com",
                    "userNumber": "A03"
                },
                {
                    "password": "welcome1",
                    "account": "Durant004",
                    "username": "杜兰特4号",
                    "departmentCode": "TEST02",
                    "commonDeptCodeList": [
                        "TEST4"
                    ],
                    "phone": "16652900909",
                    "manageerAccount": "Durant003",
                    "email": "Durant.004@qq.com",
                    "userNumber": "B00005",
                    "workStatus": "离职"
                }
            ]
        }
    )

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    print(datatime, response, dict1)


# 获取应用access_token
def get_access_token():
    client_id = '9234d7c2-7dc8-41c5-a386-ecddc209f897'
    client_secret = '53b2fb99-31b0-4d08-bd95-8a088d3b9ec8'
    url = 'http://10.20.13.13:30613/xdap-open/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        client_id, client_secret)
    header = {
        "Content-Type": "application/json",
    }

    payload = {
        "client_id": "{}".format(client_id),
        "client_secret": "{}".format(client_secret),
        "grant_type": "client_credentials"
    }

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    actoken = dict1["access_token"]
    print(response, dict1)
    return actoken


# 获取用户token
def get_token():
    actoken = get_access_token()
    userId = "100169876816012509184"
    url = 'http://10.20.13.13:30613/xdap-open/token/userToken?token={}&userId={}'.format(actoken, userId)
    header = {
        "Content-Type": "application/json",
    }

    payload = {
        "token": "{}".format(actoken),
        "userId": "".format(userId)
    }

    response = requests.request("GET", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    token = dict1["access_token"]
    print(response, dict1)
    return token


if __name__ == "__main__":
    get_tenant_user()
