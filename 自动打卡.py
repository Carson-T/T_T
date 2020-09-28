import requests,json
from bs4 import BeautifulSoup
session = requests.session()
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    "Content-Type":"application/json"
}
data={
    "password": "Tan123456789..",
    "username": "2019051402"
}
url="https://stuhealth.jnu.edu.cn/api/user/login"
response = session.post(url,headers=headers,data=json.dumps(data))
print(response)
url_l="https://stuhealth.jnu.edu.cn/api/write/main"


data_l = {
    "jnuid": "2019051402",
        "mainTable":{
            "assistantName": "张磊",
            "assistantNo": "0005875*",
            "className": "2019级",
            "collegeName": "信息科学技术学院",
            "currentArea": "3",
            "declareTime": "2020-09-14",
            "isPass14C1": "0",
            "isPass14C2": "0",
            "isPass14C3": "2",
            "language": "cn",
            "linkman": "吴义娇",
            "linkmanPhone": "13346514467",
            "linkmanPhoneArea": "+86",
            "otherC4": "无",
            "personC4": "t3 626",
            "personHealth": "1",
            "personHealth2": "0",
            "personName": "谭建韬",
            "personNo": "2019051402",
            "phone": "19860076127",
            "phoneArea": "+86",
            "professionName": "智能科学与技术",
            "schoolC1": "2",
            "sex": "男",
            "temperature": "37",
            "way2Start": "",
        }
}

session.post (url_l,headers=headers,data=json.dumps(data_l))
print(session.post (url_l,headers=headers,data=json.dumps(data_l)))