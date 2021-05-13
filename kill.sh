#!/bin/bash
#encoding=utf-8

function killAll () {
    sign=$(ps aux | grep sign_main  | grep -v grep | awk {'print $2'})
    remind=$(ps aux | grep remind_parse | grep -v grep | awk {'print $2'})

    for item in {$sign,$remind}; do
        printf '%s %s\n' $item "kill -9 $item"
        kill -9 $item
    done
}

killAll
