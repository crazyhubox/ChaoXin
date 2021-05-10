import requests
from parsel import Selector
import re

param_find = re.compile(r'.+?courseid=([0-9]+?)&clazzid=([0-9]+?)&vc=1&cpi=([0-9]+)')
act_id = re.compile(r'activeDetail\((\d+?),')

def view_task_page(cookies: dict, courseId: str, jclassId: str):
    params = (
            ('courseId', courseId),
            ('jclassId', jclassId),
    )
    response = requests.get('http://mobilelearn.elearning.shu.edu.cn/widget/pcpick/stu/index',
                            params=params, cookies=cookies)
    html = response.text
    return Selector(text=html)

def get_tasks(select: Selector) -> list:
    # TODO 得到任务的编号以及任务的类型,普通还是位置签到
    tasks = []
    acts = select.css('#startList div.Mct')
    for each_act in acts:
        # each_act.css('.Mct::attr(onclick)')
        atc_val = each_act.css('.Mct::attr(onclick)').get()
        atc_name = each_act.css('.Mct div a[shape=rect]::text').get()
        if atc_val:
            res = act_id.search(atc_val)
            if res:
                atc_val = res.group(1)
            tasks.append((atc_val, atc_name))
    return tasks

def get_params(url: str):
    # 从课程连接得到班级号和课程号
    res = param_find.search(url)
    if res:
        return (res.group(1), res.group(2),res.group(3))
    return None



if __name__ == '__main__':
    pass
    # main()
    # get_urls_each_course()
