#-*-coding:utf8 -*-
#一个比较初级的爬取蜻蜓fm的做法。
import re
from urllib import request

for i in range(1,12):
    url='http://i.qingting.fm/wapi/channels/84344/programs/page/'+str(i)+'/pagesize/10'  #从网页中找到json文件url，得到真实地址，循环页码
    # print(url)
    with request.urlopen(url) as f:  #把内容读出来
        dd=str(f.read())
        # print(dd)
        res=re.findall(r'"program_ondemand","file_path":"(.*?)"',dd)  #用正则表达式获取文件的真是path
        for ii in res:
            a=str(ii).replace('\\','/')
            # print(a)
            downlist='http://upod.qingting.fm/'+str(a)         #拼接出真是网址。
            print(downlist)                                    #打印
            # urllib.request.urlretrieve(downlist,'/Users/lifujie/test/')  #下载文件，未实现。