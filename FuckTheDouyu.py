#coding=utf-8

import urllib
import urllib2
import cookielib
from lxml import etree

import DataMode



def getLiveList(url):
	# url 		=	'http://www.douyu.com/directory/game/How'
	userAgent	= 	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36'
	headers		=	{
						'User-Agent':userAgent,
						'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
					}
	data		=	urllib.urlencode({})
	request 	=	urllib2.Request(url+'?'+data,headers=headers)

	liveList 	=	[]
	try:
		response 	= 	urllib2.urlopen(request)
		body = response.read().decode('utf-8');
		# print body
		body = etree.HTML(body)
		for ele in body.xpath(u'//*[@id="live-list-content"]/ul/li/a'):
			liveBean 			= etree.tostring(ele);
			# print liveBean
			# print type(liveBean)
			# print '----'*10
			liveData 			=	 DataMode.LiveRoomData()
			liveData.platform	=	u'斗鱼'
			#地址
			liveData.href		=	'http://www.douyu.com'+ele.attrib['href']
			# 房间名称
			liveData.title		= 	ele.attrib['title']
			# 缩略图
			liveData.pic		=	etree.HTML(liveBean).xpath(u'//span/img')[0].attrib['data-original']
			# 房间名称
			# liveData.title=etree.HTML(liveBean).xpath(u'//div/div/h3')[0].text
			# 房间分类
			liveData.category	=	etree.HTML(liveBean).xpath(u'//div/div/span')[0].text
			# 主播
			liveData.name 		=	etree.HTML(liveBean).xpath(u'//div/p/span')[0].text
			# 人气 
			fansStr				=	etree.HTML(liveBean).xpath(u'//div/p/span')[1].text.encode('utf-8')
			# 人气大于万时特殊处理   13.9万
			if fansStr.count('万') >0 :
				fansStr = fansStr.replace('万','')
				fansStr = float(fansStr)*10000
			liveData.fans = int(fansStr)

			liveList += [liveData]
			# liveList.append(liveData)

	except urllib2.URLError, e:
		print 'error - %d' % (e.code)

	return liveList


# liveList  = getLiveList()
# liveList.sort(key = lambda x:x.fans,reverse = True)
# for liveBean in liveList:
# 	print liveBean.desc()
# 	print '--'*10



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