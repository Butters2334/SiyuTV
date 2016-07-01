#coding=utf-8

import urllib
import urllib2
import cookielib
from lxml import etree

import DataMode



def getLiveList(url):
	# url 		=	'http://www.panda.tv/cate/hearthstone'
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
		body = etree.HTML(body)
		for ele in body.xpath(u'//*[@id="main-container"]/div/ul/li/a'):
			liveBean 			= etree.tostring(ele);
			# print type(liveBean)
			# print '----'*10
			liveData 			=	 DataMode.LiveRoomData()
			liveData.platform	=	u'熊猫'
			#地址
			liveData.href		=	'http://www.panda.tv'+ele.attrib['href']
			# # 房间名称
			# liveData.title		= 	ele.attrib['title']
			# 缩略图
			liveData.pic		=	etree.HTML(liveBean).xpath(u'//div[@class="video-cover"]/img')[0].attrib['data-original']
			# 房间名称
			liveData.title 		=	etree.HTML(liveBean).xpath(u'//div[@class="video-title"]')[0].text
			# 房间分类
			liveData.category	=	body.xpath(u'//*[@class="main-header"]/h3')[0].text
			# 主播
			liveData.name 		=	etree.HTML(liveBean).xpath(u'//div[@class="video-info"]/span[@class="video-nickname"]')[0].text
			# 人气 
			fansStr				=	etree.HTML(liveBean).xpath(u'//div[@class="video-info"]/span[@class="video-number"]')[0].text.encode('utf-8')
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
<li class="video-list-item video-no-tag video-no-cate" data-id="10003">
	<a href="/10003" class="video-list-item-wrap" data-id="10003">
		<div class="video-cover">
			<img class="video-img video-img-lazy" data-original="http://i6.pdim.gs/45/cc6fe51321186ae2e2c6f551a9fb0541/w338/h190.jpg" alt="星苏：明日月末休息一天">
			<div class="video-overlay"></div>
			<div class="video-play"></div>
		</div>
		<div class="video-title" title="星苏：明日月末休息一天">星苏：明日月末休息一天</div>
		<div class="video-info">
			<span class="video-nickname">Igxingsu</span>
			<span class="video-number">86133</span>
		</div>
	</a>
</li>
"""