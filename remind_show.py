#!/usr/local/python3/bin/python3
from deadline.show import Show
import argparse

def main():
    # 创建解析步骤
    parser = argparse.ArgumentParser(description='Show the reminds.')
    # 添加参数步骤
    parser.add_argument('type',type=str,default="None",help='give the show type.')
    parser.add_argument('view_mode',type=str,default="order",help='give the show mode group? order?.')
    # 解析参数步骤  
    args = parser.parse_args()
    Show(args.type,args.view_mode)
    
if __name__ == '__main__':
    main()