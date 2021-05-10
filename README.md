# 自动签到以及作业DDL的获取

![avatar](https://img.shields.io/badge/license-MIT-blue)
![avatar](https://img.shields.io/badge/Redis-%203.2.12-orange)
![avatar](https://img.shields.io/badge/requests-2.25.0-grenn)
![avatar](https://img.shields.io/badge/parsel-1.6.0-9cf)

签到:

每次都一不小心错过发布的签到, 这次直接写脚本在server上一直刷吧, 终于不会漏了.

作业DDL:

这个必须要吐槽一下, 超星既然是帮助老师和同学更好地管理和安排学习任务, 那么再当今大学生都是靠DDL激发生活斗志的形势之下, 学生端居然没有DDL的统一管理页面, 要查看一个课程的作业还剩多少时日,居然还要一个课程一个课程去找. 截止时间到了24小时以内也不发送通知, 因此错过好几次作业的提交.

- [自动签到以及作业DDL的获取](#%E8%87%AA%E5%8A%A8%E7%AD%BE%E5%88%B0%E4%BB%A5%E5%8F%8A%E4%BD%9C%E4%B8%9Addl%E7%9A%84%E8%8E%B7%E5%8F%96)
  - [解决方案](#%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88)
  - [实现逻辑](#%E5%AE%9E%E7%8E%B0%E9%80%BB%E8%BE%91)
  - [目录文件说明](#%E7%9B%AE%E5%BD%95%E6%96%87%E4%BB%B6%E8%AF%B4%E6%98%8E)
  - [最后](#%E6%9C%80%E5%90%8E)


## 解决方案

![image](https://github.com/crazyhubox/ChaoXin/blob/main/static/sign.gif)

![image](https://github.com/crazyhubox/ChaoXin/blob/main/static/DDL.gif)

## 实现逻辑

![image](https://github.com/crazyhubox/ChaoXin/blob/main/static/logic.png)

只是很粗略地表示整个逻辑,内部还有许多细节,比如如何根据剩余时间进行排序的问题, 如何友好的显示这种字符串格式化的问题.

可以使用redis提供的排序集合这个数据结构来实现根据时间排序.

## 目录文件说明

```bash
.
├── LICENSE
├── Logger
│   └── __init__.py         这个就是负责日志记录的封装
│
├── Login
│   └── __init__.py         登录获取cookie的方法
│
├── deadline                DDL需要的工具函数
│   ├── __init__.py
│   ├── show.py
│   └── tasks.py
│
├── sign                    签到需要的工具函数
│   ├── __init__.py
│   ├── genal_sign.py       普通签到
│   ├── getTasks.py
│   └── location_sign.py    位置签到
│
├── remind_parse.py         DDL的爬取
├── remind_show.py          DDL的显示
├── get_course_url.py       获取自己所有的课程链接
├── sign_main.py            签到的实现
├── makefile                makefile脚本不用也行
└── check.sh                检查进程的脚本
```

先通过get_course_url.py这个文件获取所有的课程信息

然后放入到remind_parse.py和deadline/show.py这两个文件中使用

## 最后

其他详细的说明有兴趣同学见代码注释吧. 项目仅仅作为同学们参考和讨论交流, 并不属于拿来即用类型的项目,如果需要实际使用还需要根据自身情况进行修改.

这个项目就用这个最后一个学期了, 所以之后并没有考虑更大的功能的拓展, 也就没有使用面向对象, 都是函数式编程.

最后推荐一个解析库就是parsel, scrapy框架内部封装的selector就是对这个库的封装, 里面有支持css选择器和xpath语法以及正则表达式, 个人感觉比beautifulsoup好用.

这个项目公开的就更新到这里吧,没有那么多时间来更新了.