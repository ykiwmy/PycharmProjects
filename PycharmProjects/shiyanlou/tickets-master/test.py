
import requests

def cli():
    # 添加verify=False参数不验证证书
    r = requests.get(url, verify=False)
    print(r.json())

