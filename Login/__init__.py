import requests
import re

cookies = re.compile(r'HttpOnly, ?(.+?);|Path=/, (.+?);')

def login_cookies():
    headers = {
        'Origin': 'http://passport2.chaoxing.com',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://passport2.chaoxing.com/login?refer=http%3A%2F%2Fmooc1-1.chaoxing.com%2Fvisit%2Finteraction%3Fs%3D3d390bb2f73d2fb2566e8b3354649e66&fid=0&newversion=true&_blank=0',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    data = {
        'fid': '-1',
        'uname': '你的电话或者学号',
        'password': '这个是加密之后的密码,可以在浏览器中抓到,不会动态变化',
        'refer': 'http%3A%2F%2Fmooc1-1.chaoxing.com%2Fvisit%2Finteraction%3Fs%3D3d390bb2f73d2fb2566e8b3354649e66',
        't': 'true',
        'forbidotherlogin': '0'
    }

    response = requests.post(
        'http://passport2.chaoxing.com/fanyalogin', headers=headers, data=data)
    cookie_str = response.headers['Set-Cookie']
    cookie_dict = clean_cookies(cookie_str)
    # print(cookie_dict)
    return cookie_dict


def clean_cookies(raw_cookie) -> dict:
    cookies_res = {}
    res = cookies.findall(raw_cookie)
    for each in res:
        c = each[0] if each[0] != '' else each[1]
        temp = c.split('=')
        cookies_res[temp[0]] = temp[1]
    return cookies_res


def refresh_cookies(cookies,count:int):
    if count/10 == 1:
        count = 0
        cookies = login_cookies()
        return cookies,count

    return cookies,count

__all__ = [
    'refresh_cookies',
    'login_cookies'
]