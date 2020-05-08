#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pexpect


def remote_ssh(remote_ip, user, passwd, cmd):
    ret = -1
    ssh = pexpect.spawn('ssh %s@%s "%s"' % (user, remote_ip, cmd))
    try:
        i = ssh.expect(['password:', 'continue connect (yes/no)?'], timeout=5)
        if i == 0:
            ssh.sendline(passwd)
        elif i == 1:
            ssh.sendline('yes\n')
            ssh.expect('password:')
            ssh.sendline(passwd)
        r = ssh.read()
        print(r)
        ret = 0
    except pexpect.EOF:
        print("EOF")
        ssh.close()
        ret = -1
    except pexpect.TIMEOUT:
        print("TIMEOUT")
        ssh.close()
        ret = -2
    return ret, r


if __name__ == '__main__':
    ip = "192.168.88.128"
    user = "root"
    password = "taoweidong"
    cmd = "df -h"
    ret, msg = remote_ssh(ip, user, password, cmd)
    print ret
    print msg
