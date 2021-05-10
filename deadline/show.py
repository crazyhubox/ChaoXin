from redis import Redis
rdb = Redis(host='your host of redis-server',password='your password.',db=2,decode_responses=True)

COURSES = [
    ('/visit/stucoursemiddle?courseid=218148267&clazzid=40920416&vc=1&cpi=134538886','教育学'),
    ('/visit/stucoursemiddle?courseid=218144539&clazzid=40910648&vc=1&cpi=136486695','设置基础学'),
    ('/visit/stucoursemiddle?courseid=217817986&clazzid=40052686&vc=1&cpi=137312605','小学数学'),
]

def get_restime_from_score(score:float):
    if score == 0.001:
        return None
    sc = str(score)
    h,m = sc.split('.')
    return f'剩余{h}小时{m}分钟'

def get_reminds(tp):
    reminds = []
    for course in COURSES:
        res = rdb.zscan_iter(course[1])
        for course_info in res:
            info,score = course_info
            task, status = info.split(',')
            
            if score == 0.001 and tp != 'all':
                continue
            reminds.append((f'[{status}]: {course[1]}',score,task))
    return reminds


def Show(tp=None,mode:str='order'):

    def show_reminds(reminds:list,tp,mode):
        reminds = sorted(reminds,key=lambda s:s[1])
        if mode == 'group'and tp != 'all':
            group_show(reminds=reminds)
            return
        
        if mode == 'group' and tp == 'all':
            group_show_all(reminds=reminds)
            return
        
        temp = []
        for course,score,task in reminds:
            t = get_restime_from_score(score)
            if not t:
                t = '无截止时间'
                # print(t)
                temp.append((course,task,t))
                continue
            print(course,task,t)

        if tp == 'all':
            # print(temp)
            for course,task,t in temp:
                print(course,task,t)

    def group_show(reminds):
        res = {}
        for course,score,task in reminds:
            t = get_restime_from_score(score)
            if not t:
                t = '无截止时间'

            status,course = course.split(': ')
            if course in res:
                res[course].append(f'{status}: {task} {t}')
                continue

            res[course] = []
            res[course].append(f'{status}: {task} {t}')
            
        for k,v in res.items():
            print(f'{k}:')
            for each in v:
                print(each)
            print()

    def group_show_all(reminds):
        res = {}
        for course,score,task in reminds:
            t = get_restime_from_score(score)
            if not t:
                t = '无截止时间'

            status,course = course.split(': ')
            if course in res:
                res[course].append(f'{status}: {task} {t}')
                continue

            res[course] = []
            res[course].append(f'{status}: {task} {t}')
            
        for k,v in res.items():
            print(f'{k}:')
            temp = []
            for each in v:
                if each.find('无截止') != -1:
                    temp.append(each)
                    continue
                print(each)
            for each in temp:
                print(each)
            print()

    reminds = get_reminds(tp)
    show_reminds(reminds,tp,mode)

if __name__ == '__main__':
    Show()




