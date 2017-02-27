#!/usr/bin/env python
# coding:utf-8

import json
import requests
import os
import time
import sys
import argparse

reload(sys)
sys.setdefaultencoding('utf-8')

start_text="""

"""

def loadCookie():
    cwd = os.getcwd()
    filename='cookie.txt'
    cookiefile = os.path.join(cwd,filename)


    with open(cookiefile,'r') as f:
        cookies={}
        for line in f.read().split(';'):
            name,value = line.strip().split('=',1)
            cookies[name]=value

    print "[*] cookie load success!"
    return cookies

def secretSpider(t,g,outfile,cookies):


    s = requests.Session()
    p = {}
    p['g_tk'] = g
    #1423284339



    secretUrl = 'https://h5.qzone.qq.com/webapp/json/secretList/getSecretActFeeds'


    payload = {
        'refresh_type':'2',
        'relation_type':'8',
        'attach_info':'endtime='+str(t)+'&offset=0&tlistsec=0&tlistusec=0&recomfeed=',
        'uin':cookies['p_uin'].replace("o0",""),
        'format':'json'
    }


    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13E238 Safari/601.1'
    headers['Content-Type'] = 'application/x-www-form-urlencoded'




    if True:

        print '[*] payload sending ...'
        r2= s.post(secretUrl, params=p, headers=headers,data=payload,cookies=cookies)
        #气死 不是data=json.dumps(payload)
        #如果是表单形式 直接data=payload TAT
        if r2.status_code == 200:
            print '[*] payload sent'
            content = json.loads(r2.text)

            lastnode = content['data']['all_feeds_data'][-1]
            laststamp = lastnode['singlefeed']['0']['time']

            for node in content['data']['all_feeds_data']:
                orglikekey = node['singlefeed']['0']['orglikekey']
                stamp = node['singlefeed']['0']['time']
                curlikekey = node['singlefeed']['0']['curlikekey']
                relation = node['singlefeed']['3']['relation_type']
                uid = node['singlefeed']['1']['user']['uid']
                text = node['singlefeed']['4']['summary']
                text = text.replace("\n", "<br>")
                datatime = stamp2time(stamp)

                try:
                    img = node['singlefeed']['5']['picdata'][0]['photourl']['11']['url']
                    qq = img.split('/')[4]

                except KeyError,e:
                    qq = 'unknown'

                with open(outfile,'a') as f:
                    f.write("time:%s,uid:%s,qq:%s,relation:%s,text:%s\n" % (datatime,uid,qq,relation,text))
            print "spider to : " + stamp2time(t)
            return laststamp
        else:
            print r2.status_code,'post',r2.reason,r2
            print "[!] check your cookies!"
            sys.exit(0)


def stamp2time(stamp):
    timeArray = time.localtime(stamp)
    datatime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return datatime




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s',help='the start time you want to spider,(e.g. 2017-01-01)' ,dest='start_time',default=None)
    parser.add_argument('-e',help='the end time you want to spider,default is now',dest='end_time',default=None)
    parser.add_argument('-g',help='auth to qq zone',dest='g_tk',type=str,default=None)
    parser.add_argument('-o',help='output to a file,default is data.txt',dest='outfile',default=None)

    args = parser.parse_args()

    start_time = args.start_time
    end_time   = args.end_time
    g_tk = args.g_tk
    outfile = args.outfile

    if g_tk == None:
        parser.print_help()
        sys.exit(-1)
    else:
        g = g_tk

    #起始时间
    if start_time == None:
        start_time = '2017-01-01'
        t1=int(time.mktime(time.strptime(start_time,'%Y-%m-%d')))

    else:
        t1=int(time.mktime(time.strptime(start_time,'%Y-%m-%d')))

    #结束时间
    if end_time == None:
        t2=int(time.time())
    else:
        end=end_time
        t2=time.mktime(time.strptime(end,'%Y-%m-%d'))

    if outfile == None:
        f = 'data.txt'
        print "[*] results save to data.txt!"
    else:
        f = outfile
        print "[*] results save to %s!" % f



    cookies = loadCookie()


    t=t2
    t2=t2+1
    while (t < t2) and (t > t1):
        try:
            t = secretSpider(t,g,f,cookies)
        except IndexError,e:
            print "all is ok"
            sys.exit(1)
        t = t-1


if __name__ == '__main__':
    main()
