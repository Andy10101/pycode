#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-04 09:46:52
# @Author  : nwcrazysword (nwcrazysword@gmail.com)
# @Link    : https://github.com/nwcrazysword
# @Version : $Id$

import json
import sys
import os
import pickle

def GetTheJson(jsontype):
    '''
    jsontype:
    low 小写字母
    up  大写字母
    num 数字
    '''
    dict_temp = {}
    if jsontype == 'low':
        templist = xrange(26)
        char_min = 'a'
        char_pre='_'
    if jsontype == 'up':
        templist = xrange(26)
        char_min = 'A'
        char_pre=''
    if jsontype == 'num':
        templist = xrange(1, 10)
        char_min = 'A'
        char_pre=''

    path_json_pre='../json_zhuhai/'+char_pre

    for i in templist:
        try:
            if jsontype == 'num':
                c = i
            # elif jsontype == 'up':
            #     c = chr(ord(char_min) + i)
            else:
                c = chr(ord(char_min) + i)
            fpath = '%s%s.json' % (path_json_pre,c)
            f = open(fpath)
            d = json.loads(f.read())
            dict_temp[c] = d
            f.close()
        except IOError:
            dict_temp[c] = {}

    for char in dict_temp:
        char=str(char)
        print '====== %s ======' % char
        show(char_pre+char)

    return dict_temp


def GetAllJson():
    result = {}
    typelist = ['low', 'up', 'num']
    for item in typelist:
        dict_temp = GetTheJson(item)
        result.update(dict_temp)
    for key in result:
        result[key].pop('x_min')
        result[key].pop('y_min')
        result[key].pop('x_max')
        result[key].pop('y_max')
    # print result
    with open('data.json', 'wb') as f:
        f.write(json.dumps(result))

def show(char):
    fpath='../json_zhuhai/%s.json'%char
    if not os.path.exists(fpath):
        print 'The json file is not exist!'
        return
    with open(fpath) as f:
        dic = json.loads(f.read())
        # print dic
        for j in xrange(dic['height']):
            for i in xrange(dic['width']):
                if [i,j] in dic['points']:
                    print 'O',
                else:
                    print ' ',
            print '\n'


def main():
    GetAllJson()

if __name__ == '__main__':
    main()