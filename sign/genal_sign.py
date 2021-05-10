import requests
from parsel import Selector

def genal_sign(cookies,courseId,classId,activeId):
    
    headers = {
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://mobilelearn.elearning.shu.edu.cn/widget/pcpick/stu/index?courseId=217817986&jclassId=40052686',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }

    params = (
        ('activeId', activeId),#这个参数对应签到的图标在DOM中可获得
        ('classId', classId),
        ('fid', '209'), #这个参数是固定的,并且唯一标识用户身份
        ('courseId', courseId),
    )
    response = requests.get('http://mobilelearn.elearning.shu.edu.cn/widget/sign/pcStuSignController/preSign', headers=headers, params=params, cookies=cookies, verify=False)
    html = response.text 
    find = Selector(text=html)
    res = find.css('title::text').get()
    if res.find('签到成功') != -1:
        stime = find.css('#st::text').get()
        return f"{res},{stime}"
    
