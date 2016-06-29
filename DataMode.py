#coding=utf-8



class LiveRoomData:
	def __int__(self):
		pass

	#直播地址
	href	= ''
	#缩略图
	pic		= ''
	# 平台
	platform= ''
	# 主播
	name 	= ''
	# 直播间名称
	title	= ''
	# 观看数量
	fans	= 0
	# 直播分类
	category= ''

	def desc(self):
		return self.title+'\n'+self.name+'\n'+str(self.fans)+'\n'+self.pic+'\n'+self.href+'\n'+self.category+'\n'+self.platform
