#coding=utf-8

import FuckTheDouyu
import FuckThePanda
import FuckTheQuanmin
import FuckTheHuya
import os
from bs4 import BeautifulSoup #引入 BeautifulSoup  
import urllib
import urllib2
import cookielib
import HTMLParser
import cgi
import sys 



def main():

	reload(sys) 
	sys.setdefaultencoding('utf-8')

	liveList  = []
	douyuList = FuckTheDouyu.getLiveList('http://www.douyu.com/directory/game/How')
	liveList += douyuList
	print "斗鱼 %d" % len(douyuList)
	pandaList = FuckThePanda.getLiveList('http://www.panda.tv/cate/hearthstone')
	liveList += pandaList
	print "熊猫 %d" % len(pandaList)
	quanList  = FuckTheQuanmin.getLiveList('http://www.quanmin.tv/json/categories/heartstone/list.json')
	liveList += quanList
	print "全民 %d" % len(quanList)
	huyaList  = FuckTheHuya.getLiveList('http://www.huya.com/g/hearthstone')
	liveList += huyaList
	print "YY %d" % len(huyaList)

	liveList.sort(key = lambda x:x.fans,reverse = True)
	for liveBean in liveList:
		print liveBean.desc()
		print '--'*10


	url 		=	'http://www.douyu.com/directory/game/How'
	userAgent	= 	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
	headers		=	{
						'User-Agent':userAgent,
						'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
					}
	data		=	urllib.urlencode({})
	request 	=	urllib2.Request(url+'?'+data,headers=headers)

	try:
		response 	= 	urllib2.urlopen(request)
		body = response.read().decode('utf-8');
		soup = BeautifulSoup(body,'lxml')
		div = soup.find(id='live-list-content')

		liveli = (div.ul.li)
		# 修改li属性
		ulStr = ""
		for liveBean in liveList:
			liveli.a['href'] 						= ""+liveBean.href
			liveli.a['title'] 						= liveBean.name.encode('utf-8')
			liveli.a.span.img['data-original']		= liveBean.pic
			liveli.a.div.div.h3.string 				= liveBean.name.encode('utf-8')
			liveli.a.div.div.span.string 			= liveBean.platform.encode('utf-8')
			liveli.find(class_='dy-name').string 	= liveBean.title.encode('utf-8') 
			if liveBean.fans < 10000 :
				liveli.find(class_='dy-num').string = str(liveBean.fans).encode('utf-8') 
			else:
				liveli.find(class_='dy-num').string = "%.1f万" % (liveBean.fans/10000.0)


			ulStr += HTMLParser.HTMLParser().unescape(liveli.prettify().encode('utf-8'))


		div.ul.string = ulStr

		soup.title.string ='死鱼TV'

		# print "\n"*3
		# print HTMLParser.HTMLParser().unescape(soup.prettify())

	except Exception, e:
		raise e

	fp = open("siyu.html",'w')  
	# soup = BeautifulSoup(fp)#根据文件内容新建一个 BeautifulSoup 对象  
	# print soup
	# name = soup.find(class_="name")#搜索 class 为 name 的 tag  
	# name.string = "kobi"#修改为新的名字  
	fp.seek(0,os.SEEK_SET)#移动到文件头  
	fp.write(HTMLParser.HTMLParser().unescape(soup.prettify()))#重写整个文件  
	fp.close() 

main()






"""
<li class=" "  data-ranktype='1' data-cid='2' data-rid='48699'>
	<a href="/youyichuiyi" title="衣锦夜行：登顶登顶"  >
	    <span class="imgbox">
            <b></b>
            <i class="black"></i>
	        <img data-original="http://rpic.douyucdn.cn/z1606/28/15/48699_160628154441.jpg" src="http://shark.douyucdn.cn/app/douyu/res/page/list-item-def-thumb.gif" width="283" height="163">
	    </span>

	    <div class="mes">
	        <div class="mes-tit">
	            <h3 class="ellipsis">衣锦夜行：登顶登顶</h3>
	            <span class="tag ellipsis">炉石传说</span>
	        </div>
	        <p>
	            <span class="dy-name ellipsis fl">衣锦夜行</span>
	            <span class="dy-num fr">8.3万</span>
			</p>
	    </div>
	</a>
</li>
"""