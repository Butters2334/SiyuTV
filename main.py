#coding=utf-8

import FuckTheDouyu
import FuckThePanda
import FuckTheQuanmin
import FuckTheHuya


def main():
	liveList  = FuckTheDouyu.getLiveList()
	liveList += FuckThePanda.getLiveList()
	liveList += FuckTheQuanmin.getLiveList()
	liveList += FuckTheHuya.getLiveList()

	liveList.sort(key = lambda x:x.fans,reverse = True)
	for liveBean in liveList:
		print liveBean.desc()
		print '--'*10

main()




