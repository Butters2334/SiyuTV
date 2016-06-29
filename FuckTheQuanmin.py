#coding=utf-8

import urllib
import urllib2
import cookielib
# from lxml import etree
import json

import DataMode



def getLiveList():
	url 		=	'http://www.quanmin.tv/json/categories/heartstone/list.json'
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
		body = json.loads(body)
		# print body['data']
		for liveModel in body['data']:
			liveData 			=	 DataMode.LiveRoomData()
			liveData.platform	=	u'全民'
			#地址
			liveData.href		=	'http://www.quanmin.tv/v/'+liveModel['uid']
			# 房间名称
			liveData.title		= 	liveModel['title']
			# 缩略图
			liveData.pic		=	liveModel['thumb']
			# 房间分类
			liveData.category	=	liveModel['category_name']
			# 主播
			liveData.name 		=	liveModel['nick']
			# 人气 
			liveData.fans	=	int(liveModel['view'].encode('utf-8'))
			# print liveData.fans

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
 {
    "weight": "3356460",
    "app_shuffling_image": "http://image.quanmin.tv/a73d7f7ce7192327e8cbbe9f95080a54jpg",
    "status": "1",
    "category_id": "3",
    "follow": 124520,
    "default_image": "",
    "thumb": "http://snap.quanmin.tv/2820986-1467185594-862.jpg?imageView2/2/w/390/",
    "intro": "竞技场",
    "title": "不二：竞技场~你们的皇帝又回来了",
    "avatar": "http://image.quanmin.tv/avatar/0da06df7f7d48a32733aa9817b1d5f54gif?imageView2/2/w/300/",
    "category_slug": "heartstone",
    "view": "295857",
    "slug": "",
    "grade": "",
    "nick": "全民丶不二",
    "video_quality": "234",
    "announcement": "每天下午2点到7点群号155714599",
    "category_name": "炉石传说",
    "recommend_image": "http://image.quanmin.tv/5971b4ffe6ceb82ea8706ee04c565c26jpg",
    "level": "0",
    "uid": "2820986",
    "hidden": false
}
"""