from sign import *
from Login import *
from time import sleep
from Logger import Logger,Handler
from datetime import datetime
import sys
import traceback

COURSES = [
    ('/visit/stucoursemiddle?courseid=218148267&clazzid=40920416&vc=1&cpi=134538886','教育学'),
    ('/visit/stucoursemiddle?courseid=218144539&clazzid=40910648&vc=1&cpi=136486695','设置基础学'),
    ('/visit/stucoursemiddle?courseid=217817986&clazzid=40052686&vc=1&cpi=137312605','小学数学'),
]

def get_sign_logname():
    today = datetime.now().date()
    sign_log_filename = f'{today}-sign.log'
    return f'./Logger/logs/{sign_log_filename}'

log_name = get_sign_logname()
print(log_name)
logger = Logger('file',log_name)

def Sign(cookies):
    logger.warning('登录....')

    for url,title in COURSES:
        # 每一节课
        courseId,jclassId,_ = get_params(url=url)
        selector = view_task_page(cookies,courseId,jclassId)
        tasks = get_tasks(selector)
      
        if not tasks:
            logger.info(f'{title} 没有签到')
            continue

        for task_id,task_name in tasks:
            # 每一个任务
            if task_name.find('签到') == -1:
                logger.info(f"{title} 其他任务:{task_name}")
                continue

            if task_name == '位置签到':
                res = location_sign(cookies,task_id,courseId,jclassId)
                if res:
                    logger.info(f'{title} 位置签到成功')
                else:
                    logger.error(f'{title} 位置签到失败')
            
            elif task_name[:2] == '签到':
                res = genal_sign(cookies,activeId=task_id,courseId=courseId,classId=jclassId)
                logger.info(f"{title} {res}")
            
            else:
                logger.info(f'{title} 其他签到,发送通知 {task_name}')


def change_log_path():
    log_name = get_sign_logname()
    if logger.handlers:
        logger.removeHandler(logger.handlers[0])
    print(log_name)
    new_handler = Handler('file',log_name)
    logger.addHandler(new_handler)
    


def main():
    cookies = login_cookies()
    count = 0

    yesterday = datetime.now().day
    while True:
        sleep_time = 1.5
        cookies,count = refresh_cookies(cookies,count)
        now = datetime.now()

        if now.day > yesterday:
            # 切换日志文件
            change_log_path()
            yesterday = now.day

        week = now.weekday()
        if week == 5 or week == 6:
            # 睡眠时间加为一个小时
            sleep_time = 3600
            sleep(sleep_time)
        
        if now.hour > 7 and now.hour < 20:
            Sign(cookies)
        
        sleep(10)
        count += 1

if __name__ == '__main__':
    try:
        main()
    except:
        logger.error(traceback.format_exc(limit=1, file=sys.stdout))
        

