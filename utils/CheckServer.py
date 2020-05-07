#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import socket
import subprocess

# 判断网络是否正常
server = '192.168.88.128'


# 检测服务器是否能ping通，在程序运行时，会在标准输出中显示命令的运行信息
def pingServer(server):
    result = os.system('ping ' + server + ' -n 2')
    if result:
        print('service %s ping fail' % server)
    else:
        print('service %s ping ok' % server)
    return result


# 把程序输出定位到/dev/null,否则会在程序运行时会在标准输出中显示命令的运行信息
def pingServerCall(server):
    fnull = open(os.devnull, 'w')
    # result = subprocess.call('ping ' + server, shell=True, stdout=fnull, stderr=fnull)
    result = subprocess.call('ping ' + server + ' -n 2', shell=True, stdout=fnull, stderr=fnull)
    if result:
        print('service %s ping fail' % server)
    else:
        print('service %s ping ok' % server)

    fnull.close()
    return result


# 可用于检测程序是否正常，如检测redis是否正常，即检测redis的6379端口是否正常
# 检测ssh是否正常，即检测ssh的22端口是否正常
def check_aliveness(ip, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(1)
    try:
        sk.connect((ip, port))
        print('server %s %d service is OK!' % (ip, port))
        return True
    except Exception:
        print('server %s %d service is NOT OK!' % (ip, port))
        return False
    finally:
        sk.close()
    return False


if __name__ == '__main__':
    result1 = pingServerCall(server)
    print(result1)
    # print(pingServer(server))
    result = check_aliveness('192.168.88.128', 6379)
    print(result)
