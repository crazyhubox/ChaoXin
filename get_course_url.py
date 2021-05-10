from Login import requests,login_cookies
from parsel import Selector

def get_urls_each_course():
    cookies = login_cookies()
    url = 'http://mooc1-1.chaoxing.com/visit/interaction?s=3d390bb2f73d2fb2566e8b3354649e66'

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.51',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://passport2.chaoxing.com/',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    }
    resp = requests.get(url, cookies=cookies, headers=headers)
    html = resp.text
    finder = Selector(text=html)
    courses = finder.xpath('/html/body/div/div[2]/div[3]/ul/li')

    for each_course in courses[1:11]:
        url = each_course.css(
            'div.Mconright.httpsClass > h3 > a::attr(href)').get()
        title = each_course.css(
            'div.Mconright.httpsClass > h3 > a::attr(title)').get()
        print(url, title)

if __name__ == '__main__':
    get_urls_each_course()