import requests
from parsel import Selector

def location_sign(cookies,activeId,courseId,classId):
    headers = {
        'Host': 'mobilelearn.chaoxing.com',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (device:iPhone12,5) com.ssreader.ChaoXingStudy/ChaoXingStudy_3_4.8.3_ios_phone_202103121830_59 (@Kalimdor)_6470657592511539728',
        'Referer': 'https://mobilelearn.chaoxing.com/newsign/preSign?courseId={}&classId={}&activePrimaryId={}&general=1&sys=1&ls=1&appType=15&isTeacherViewOpen=0'.format(courseId,classId,activeId),
        'Accept-Language': 'zh-cn',
        'X-Requested-With': 'XMLHttpRequest',
    }
    # activeDetail(4000003120160,2,null)
    params = (
        ('name', '16123113胡志宏'),
        ('address', '上海大学宝山校区'),
        ('activeId', activeId),
        ('uid', cookies['_uid']),
        ('clientip', ''),
        ('latitude', '31.318863995721365'),
        ('longitude', '121.40224211824975'),
        ('fid', '209'),
        ('appType', '15'),
        ('ifTiJiao', '1'),
    )
    response = requests.get('https://mobilelearn.chaoxing.com/pptSign/stuSignajax', headers=headers, params=params, cookies=cookies)
    res = response.text
    if res == 'success' or res == '您已签到过了':
        return 1
    return 0
