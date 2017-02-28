qqzone
===========

## secret.py
爬取qq空间小秘密的python脚本
爬取原理的说明[传送门](http://mp.weixin.qq.com/s?__biz=MzIxMTY4MDQ2OQ==&mid=2247484612&idx=1&sn=98f5104d4cbe008503f552bc458eefa7&chksm=9750e97ea02760682a40827f7679aaf0896ae9a9cdd60cb35318de5f6e62c3c9282698738d39&mpshare=1&scene=22&srcid=0216NbBqNDQHqkvyg7mDuJMU#rd)，by [charleYang](https://mryang.minelandcn.com)

本脚本改进自[charleYang的初版](https://mryang.minelandcn.com/py-qzone-secret/):

1. 用requests包替换了urllib  
2. 去掉了一些不必要的参数  
3. 添加了说明，更易于使用
4. 自动计算g_tk
5. 默认爬取从当前时间到2017年2月
6. 如果不指定输出文件，默认保存的文件名为开始日期_结束日期，如20170201_20170228.txt



### Usage

1.电脑上，使用浏览器（chrome/firefox），点下F12打开开发者工具，访问http://h5.qzone.qq.com  
2.获取cookie，按下图方式即可获取。（网络 - XHR）  
[![cookie.png](https://github.com/VegetableCat/qqzone/blob/master/img/cookie.png?raw=true)]()

将请求头信息中的cookie，复制到同目录下的cookie.txt中，一行就好，不要换行。  



note:

推荐使用手机端的cookie和g_tk，因为电脑上每次登录空间，g_tk都会变化，而手机端的更加持久。

脚本运行说明
-g 为必要参数

```bash
➜  qqzone git:(master) ✗ ./secret.py       
usage: secret.py [-h] [-s START_TIME] [-e END_TIME] [-g G_TK] [-o OUTFILE]

optional arguments:
  -h, --help     show this help message and exit
  -s START_TIME  the start date you want to spider,(e.g. 2017-01-01)
  -e END_TIME    the end date you want to spider,default is now
  -g G_TK        auth to qq zone
  -o OUTFILE     output to a file,default is data.txt

```

### Example

```bash
➜  qqzone ./secret.py -g 1423284xxx -e 2017-02-25 -s 2017-02-20           
[*] results save to 20170220_20170225.txt!
[*] cookie load success!
[*] payload sending ...
[*] payload sent
spider to : 2017-02-25 00:00:00
[*] payload sending ...
[*] payload sent
spider to : 2017-02-23 22:37:17
[*] payload sending ...
[*] payload sent
spider to : 2017-02-23 11:24:25
[*] payload sending ...
[*] payload sent
spider to : 2017-02-22 02:55:18
[*] payload sending ...
[*] payload sent
spider to : 2017-02-21 00:55:09


```
