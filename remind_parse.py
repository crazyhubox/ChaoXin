from deadline.tasks import get_works
from deadline import get_score_from_time
from sign import get_params
from Login import refresh_cookies, login_cookies
from redis import Redis
from datetime import datetime
from time import sleep
from Logger import Logger

COURSES = [
    ('/visit/stucoursemiddle?courseid=218148267&clazzid=40920416&vc=1&cpi=134538886', '教育学'),
    ('/visit/stucoursemiddle?courseid=218144539&clazzid=40910648&vc=1&cpi=136486695', '设置基础学'),
    ('/visit/stucoursemiddle?courseid=217817986&clazzid=40052686&vc=1&cpi=137312605', '小学数学'),
]

rdb = Redis(host='your host of redis serer',db=2,password='your password',decode_responses=True)

logger = Logger()

def Parse(cookies, s_t):
    logger.warning('登录....')
    for url, course_name in COURSES:
        # 每一节课
        courseId, jclassId, cpi = get_params(url=url)
        logger.info(f'{url},{course_name}')
        for each_work in get_works(cookies, courseId, jclassId, cpi):
            '写入redis'
            # 时间每一分钟都在刷新
            name, status, rest_time = each_work
            res_str = '{},{}'.format(name, status)
            logger.info(each_work)
            rdb.zadd(course_name, {res_str: get_score_from_time(rest_time)})
        sleep(s_t)


def main():
    cookies = login_cookies()
    count = 0
    while True:
        sleep_time = 1.5
        cookies, count = refresh_cookies(cookies, count)

        now = datetime.now()
        
        if now.hour > 6 and now.hour < 23:
            Parse(cookies, sleep_time)

        sleep(120)
        count += 1


if __name__ == '__main__':
    main()
