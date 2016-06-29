#coding=utf-8

import urllib
import urllib2
import cookielib
from lxml import etree

import DataMode



def getLiveList():
	url 		=	'http://www.huya.com/g/hearthstone'
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
		# return [];

		body = etree.HTML(body)
		for ele in body.xpath(u'//*[@class="box-bd"]/div[@class="video-wrap"]/div[@class="video-unit"]/ul[@class="video-list"]/li'):
			liveBean 			= etree.tostring(ele);
			# print (liveBean)
			# return []
			# print '----'*10
			liveData 			=	DataMode.LiveRoomData()
			liveData.platform	=	u'虎牙'
			#地址
			liveData.href		=	etree.HTML(liveBean).xpath(u'//a')[0].attrib['href']
			# 缩略图
			liveData.pic		=	etree.HTML(liveBean).xpath(u'//a/img')[0].attrib['src']
			# 房间名称
			liveData.title 		=	etree.HTML(liveBean).xpath(u'//div[@class="all_live_tit"]/a')[0].text
			# 房间分类
			liveData.category	=	body.xpath(u'//*[@class="box-crumb"]/a[@class="active"]')[0].text
			# 主播
			liveData.name 		=	etree.HTML(liveBean).xpath(u'//i[@class="nick"]')[0].text
			# 人气 
			fansStr				=	etree.HTML(liveBean).xpath(u'//i[@class="js-num"]')[0].text.encode('utf-8')
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
# # liveList.sort(key = lambda x:x.fans,reverse = True)
# for liveBean in liveList:
# 	print liveBean.desc()
# 	print '--'*10




"""
<li class="video-list-item" data-boxDataInfo=''>
   <a target="_blank" href="http://www.huya.com/leialun" class="video-info clickstat" eid="click/gamelist/card/hearthstone" eid_desc="点击/游戏列表页/卡片/炉石传说">
		<img class="pic" src="http://screenshot.dwstatic.com/yysnapshot/587338141ddbe98720458ff1503ad2a40b00760d?imageview/4/0/w/280/h/158/blur/1" alt="炉石雷阿伦" title="炉石雷阿伦" onerror="this.onerror='';this.src='http://assets.dwstatic.com/amkit/p/duya/common/img/default_live.jpg'">
		<div class="item-mask"></div>
    	<em class="btn-play__hover"><i></i></em>
	</a>
   	<div class="all_live_tit">
        <a target="_blank" href="http://www.huya.com/leialun" class="clickstat" eid="click/gamelist/card/hearthstone" eid_desc="点击/游戏列表页/卡片/炉石传说">认真冲天梯排名</a>
   	</div>
    <span class="txt all_live_txt">
        <span class="avatar fl">
            <img src="http://huyaimg.dwstatic.com/avatar/1003/e7/862ab3f78e97927ede8e00522e3b3c_180_135.jpg" alt="炉石雷阿伦" title="炉石雷阿伦" onerror="this.onerror='';this.src='http://assets.dwstatic.com/amkit/p/duya/common/img/default_profile.jpg'">
            <i class="nick" title="炉石雷阿伦">炉石雷阿伦</i>
        </span>      
        <span class="num"><i class="icon-p"></i><i class="js-num">10969</i></span>   
    </span>
</li>

"""
