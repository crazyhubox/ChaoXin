import requests
from parsel import Selector
    
def get_works(cookies:dict,courseId:str,classId:str,cpi:str):
    headers = {
        'Host': 'mooc1-api.chaoxing.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 (device:iPhone12,5) com.ssreader.ChaoXingStudy/ChaoXingStudy_3_4.8.3_ios_phone_202103121830_59 (@Kalimdor)_6470657592511539728',
        'Accept-Language': 'zh-cn',
    }

    params = (
        ('courseId', courseId),
        ('classId', classId),
        ('cpi', cpi),
    )
    response = requests.get('https://mooc1-api.chaoxing.com/work/task-list', headers=headers, params=params, cookies=cookies)

    # print(response.text)
    find = Selector(text=response.text)
    contents = find.css('#content li')
    for each in contents:
        name = each.css('p::text').get()
        status = each.css('span::text').get()
        rest_time = each.css('span.fr::text').get()
        if not rest_time:
            rest_time = ''
        yield (name,status,rest_time)


if __name__ == '__main__':
    # main()
    pass