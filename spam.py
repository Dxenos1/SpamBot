import yaml
from requests import request, exceptions

def readConfig(configPath: str):
    with open(configPath, "r") as configContents:
        try:
            config = yaml.safe_load(configContents)
            return config
        except yaml.YAMLError as error:
            print(error)

def spam(url: str, method: str, body: dict ={}, headers: dict={}):
    res = request(method, url, json=body, headers=headers)
    try:
        res.raise_for_status()
    except exceptions.HTTPError as err:
        print(err)
    else:
        print(f"Payload delivered successfully, code {res.status_code}.")

# main     
configPath = "config.yaml"

config = readConfig(configPath)

api = config["api"]
url = api["url"]
data = api["data"]
method = api["method"]
headers = api["headers"]

for i in range(config["loopCount"]):
    spam(method=method, url=url, body=data, headers=headers)

