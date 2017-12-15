#图片爬虫，3个循环（目前还少一个）
#先爬取分页
#在爬取每一个里面的文字列表
#在爬取列表中的图片
import re
from urllib import request
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
url='http://www.acfun.cn/u/350475.aspx#page=1'
req = request.Request(url=url, headers=headers, method='POST')
r=str(request.urlopen(req).read())
# print(r)
url = 'http://www.acfun.cn/u/350475.aspx#page=1'
page=re.findall(r'href="/a/ac(.*?) title',r)
for i in page:
    page_url=str('http://www.acfun.cn/a/ac'+str(i))
    newpage_url=page_url.strip('"')
    # print(newpage_url)
    img_req=str(request.urlopen(newpage_url).read())
    # print(img_req)
    imglist=re.findall(r'src="http://imgs.aixifan.com/live/(.*?)" style',img_req)

    for i in imglist:
        res='http://imgs.aixifan.com/live/'+i
        print(res)