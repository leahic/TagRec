#!/usr/bin/python2.7
import os

algorithms_list = ['3layers','3LT','bll_c','bll_c_ac','lda','cf','cfr','fr','girptm','mp','mp_u_r',
                   'item_sustain','item_cirtt','item_mp','item_cbt','item_cft','item_cfb','item_zheng','item_huang',
                   'hashtag_analysis','hashtag_socialmp','hashtag_socialrecency','hashtag_socialbll','hashtag_hybrid','hashtag_cb_res','hashtag_cb_gen']

if __name__ == '__main__':
    commander = 'java -jar tagrec3_0.jar %s ml ml_tags >> error_log 2>&1 \n'
    for algorithm in algorithms_list:
        print commander % algorithm
        os.system(  commander % algorithm )
        print algorithm + ' over'
