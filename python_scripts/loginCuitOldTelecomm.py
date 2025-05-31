# 开发时间：2023/6/18  20:43
# @authored by Jam，改进 by ChatGPT 五百二版

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# === 基本信息 ===
url = "https://10.254.241.3/webauth.do?&wlanacname=SC-CD-XXGCDX-SR8810-X"
student_id = "2022051121"   # 👈 修改为你的账号
password = ""     # 👈 修改为你的密码

# === POST 表单参数 ===
data = {
    "loginType": "",
    "auth_type": "0",
    "isBindMac1": "0",
    "pageid": "1",
    "templatetype": "1",
    "listbindmac": "0",
    "recordmac": "0",
    "isRemind": "1",
    "loginTimes": "",
    "groupId": "",
    "distoken": "",
    "echostr": "",
    "url": "",
    "isautoauth": "",
    "notice_pic_loop2": "/portal/uploads/pc/demo2/images/bj.png",
    "notice_pic_loop1": "/portal/uploads/pc/demo2/images/logo.png",
    "userId": student_id,
    "passwd": password,
    "remInfo": "on"
}

# === 请求头 ===
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    # "Cookie": "...",  # 如无特殊需要可省略，或用 requests.Session() 自动管理
    "Host": "10.254.241.3",
    "Origin": "https://10.254.241.3",
    "Referer": url,
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}

# === 发送请求 ===
try:
    response = requests.post(url, data=data, headers=headers, verify=False)
    print(f"回应代码: {response.status_code}")
    print(f"响应内容预览:\n{response.text[:30000]}...")  # 只预览前300字符
except requests.exceptions.RequestException as e:
    print("请求失败：", e)
