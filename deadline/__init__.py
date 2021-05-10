import re

h_m = re.compile(r'剩余(\d{1,3})小时(\d{1,2})分钟')
m = re.compile(r'剩余(\d{1,2})分钟')
h = re.compile(r'剩余(\d{1,3})小时')

def get_score_from_time(time: str):
    # 剩余275小时38分钟 => 275.38
    # 剩余8分钟 => 0.8
    if time == '' or not time:
        return 0.001

    def f(time):
        if time.find('小时') != -1 and time.find('分钟') != -1:
            # 有小时又有分钟
            res = h_m.search(time)
            if not res:
                raise ValueError(time)
            if res.group(1) and res.group(2):
                return '{}.{}'.format(res.group(1), res.group(2))

        if time.find('小时') != -1:
            #有小时没有分钟
            res = h.search(time)
            return '{}.0'.format(res.group(1))

        # 只有分钟
        res = m.search(time)
        return '0.{}'.format(res.group(1))
    res = f(time)
    return res
