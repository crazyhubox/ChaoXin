#/usr/bin/bash

function check_reminds_parse_server() {
    res=$(ps aux | grep remind | grep -v grep)
    if [[ -n "$res" ]]; then
        echo "爬取服务运行正常,请记得清理日志"
    else
        echo "爬取服务异常"
    fi
}

function check_sign_server() {
    res=$(ps aux | grep sign | grep -v grep)
    if [[ -n "$res" ]]; then
        echo "签到服务运行正常,请记得清理日志"
    else
        echo "签到服务异常"
    fi
}

check_reminds_parse_server
check_sign_server