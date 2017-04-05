#!/usr/bin/python2.7
import sys
import datetime
import time

input_range_min = 0
input_range_max = 500000
split_dot = '\t'
origin_list = ['user','tags','resource','timestamp']
target_list = ['user','resource','timestamp','tags']
output_format = '"%s";"%s";"%s";"%s";""\n'

def string2timestamp(strValue):
    try:
        d = datetime.datetime.strptime(strValue, "%Y/%m/%d %H:%M:%S")
        t = d.timetuple()
        timeStamp = int(time.mktime(t))
        return timeStamp
    except ValueError as e:
        print e
        print 'format error?'


if __name__ == '__main__':
    print sys.argv[1]
    print sys.argv[2]

    f1 = file(sys.argv[1] , 'r')
    f2 = file(sys.argv[2] , 'w')

    for f_index , line in enumerate(f1):
        if input_range_min <= f_index and f_index <= input_range_max:
            try:
                line = line.strip().replace('"','').split(split_dot)
                #bibsonomy
                line[3] = string2timestamp(line[3])
                #movielens
                '''
                if len(line) > 4:
                    line = [ line[0] , line[1] , ','.join(line[2:-1]) , line[-1] ]
                '''
                raw = [''] * len(target_list)
                for l_index , temp_str in enumerate(line):
                    raw[ target_list.index(origin_list[l_index]) ] = temp_str
                f2.write( output_format % tuple(raw) )
            except:
                print "error at %i" % (f_index + 1)
                print line
                break

    f1.close()
    f2.close()
