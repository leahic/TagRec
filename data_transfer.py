#!/usr/bin/python2.7
import sys


input_range_min = 1
input_range_max = 500000
split_dot = ','
origin_list = ['user','resource','tags','timestamp']
target_list = ['user','resource','timestamp','tags']
output_format = '"%s";"%s";"%s";"%s";""\n'

if __name__ == '__main__':
    print sys.argv[1]
    print sys.argv[2]

    f1 = file(sys.argv[1] , 'r')
    f2 = file(sys.argv[2] , 'w')

    for f_index , line in enumerate(f1):
        if input_range_min <= f_index and f_index <= input_range_max:
            try:
                line = line.strip().replace('"','').split(split_dot)
                if len(line) > 4:
                    line = [ line[0] , line[1] , ','.join(line[2:-1]) , line[-1] ]
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
