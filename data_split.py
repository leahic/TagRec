#!/usr/bin/python2.7
import sys
import random

if __name__ == '__main__':
    print sys.argv[1]
    print sys.argv[2]
    print sys.argv[3]


    f1 = file(sys.argv[1] , 'r')
    f2 = file(sys.argv[2] , 'w')
    f3 = file(sys.argv[3] , 'w')

    s = f1.readlines()
    tot = len(s)
    print 'tot' , tot , ' lines'
    train_num = int(0.8 * tot)
    test_num = tot - train_num
    print 'train' , train_num , ' samples'
    print 'test' , test_num , ' samples'

    train_sample_list = set(random.sample(range(tot) , train_num))

    f = file('sample.log','w')
    f.write( 'tot ' + str(tot) + '  lines\n' )
    f.write( 'train ' + str(train_num) + '  samples\n' )
    f.write( 'test ' + str(test_num) + '  samples\n' )
    for x in train_sample_list: f.write( str(x) + '\n')
    f.close()

    for s_index , line in enumerate(s):
        if s_index in train_sample_list:
            f2.write(line)
        else:
            f3.write(line)
    f2.close()
    f3.close()
