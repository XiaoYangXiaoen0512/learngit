import requests
import json
import datetime
import hashlib


def get_work():
    url = "https://api.smec-cn.com/EliteGenericScriptMainService/GeneralService/getworkorderlist"
    time1 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    appsecret = 'appidsldtappappsecretrBKeBbIMLSLa2dhsfqplmrcdesxuytbcalltime'
    signature = hashlib.md5(str(appsecret + time1).encode()).hexdigest()
    print(time1, signature)
    header = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6Ill1TXBNaWk0OUgzYzB3NmdDOWZYeU1fWGk3MCIsImtpZCI6Ill1TXBNaWk0OUgzYzB3NmdDOWZYeU1fWGk3MCJ9.eyJhdWQiOiI5ZjM4ZTFlNC0yN2YzLTQxODYtYTBmMS1jYjdmOGY5ODE4OTUiLCJpc3MiOiJodHRwczovL2FkZnMuc21lYy1jbi5jb20vYWRmcyIsImlhdCI6MTY2MDI4NzQ1OSwibmJmIjoxNjYwMjg3NDU5LCJleHAiOjE2NjAyOTEwNTksImF1dGhfdGltZSI6MTY2MDI3NTAzOSwibm9uY2UiOiJjNGZhODYyMy03OGY0LTQzNzQtOTQ5Yi04ODk2MzQwN2FmNDkiLCJzdWIiOiJRSk95YkIzT1VKQ2FoRDhxdkYzUmdVbmhZY0NvVmRLdXNHUUtNTVJ6UnBRPSIsInVwbiI6ImY2MTAwMjdAc21lYy1jbi5jb20iLCJ1bmlxdWVfbmFtZSI6IlNNRUMtQ05cXGY2MTAwMjciLCJwd2RfdXJsIjoiaHR0cHM6Ly9hZGZzLnNtZWMtY24uY29tL2FkZnMvcG9ydGFsL3VwZGF0ZXBhc3N3b3JkLyIsInNpZCI6IlMtMS01LTIxLTIxNzc3ODI4NzctMzA5MjE2MTQwNC0zOTU2MzgzNDU0LTEyMDY1In0.O4kAmquWyQadHTGsUaKleZdYEuIOM8wVwg3ckfJthLfRSGAUzbTiVdTjUyh0FW6ybTNJzWbvHGZ21x3_7yqLWbwjqeQd0QvzwDX0lCz3a8AxA_YsTAGIGFWx5KGCzbtclPK-yRrXWCRq0OKHDCJ3eGNwX0lidkTlX4nQRPy5U2qrfpScOSvlvCLMKi1VPj5h7zvZPuKwgmPyG4QnIficcaKpv1ynfhW4-7JkL1gbFjugxlQE-D6Z0-DsktEAdpR1jcsXxjcc-q4WKW0q8eozFmix_k00qknk4SxSGlOwZXWN0-8bkCKBSFmr_QmTpYCr9aOuNG_EhqN_8x6PBiGjzg',
        'appid': 'sldtapp',
        'appsecret': 'rBKeBbIMLSLa2dhsfqplmrcdesxuytb',
        'calltime': '{}'.format(time1),
        'signature': '{}'.format(signature)
    }

    payload = json.dumps({
        'cur_rolegroupid': 'BCOM05',
        'caseid': 'SL202007310010'
    })

    response = requests.request("POST", url, headers=header, data=payload)
    json_music = response.json()
    dict1 = dict(json_music)
    print(response, dict1)


if __name__ == "__main__":
    get_work()