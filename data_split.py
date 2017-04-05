#!/usr/bin/python2.7
import sys
import random


def str_getuser(s):
    return s.split(';')[0].replace('"','')

def str_gettime(s):
    return int(s.split(';')[2].replace('"',''))

def str_getitem(s):
    return int(s.split(';')[1].replace('"',''))

if __name__ == '__main__':
    print sys.argv[1]
    print sys.argv[2]
    print sys.argv[3]


    f1 = file(sys.argv[1] , 'r')
    f2 = file(sys.argv[2] , 'w')
    f3 = file(sys.argv[3] , 'w')

    s = f1.readlines()

    Records = dict()

    for line in s:
        user = str_getuser(line)
        if user in Records:
            Records[user].append(line)
        else:
            Records[user] = [line]

    Userlist = sorted(Records.keys() , key = lambda x : int(x))
    for user_index , user in enumerate(Userlist):
        raw = Records[user]
        raw = sorted(raw , key = lambda x : str_gettime(x))
        lasttime = str_gettime(raw[-1])
        for line in raw:
            if str_gettime(line) < lasttime:
                f2.write(line)
            else:
                f3.write(line)

    f2.close()
    f3.close()
