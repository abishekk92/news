from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup

def parse(keyword):
	keyword="+".join(keyword.split())
	url= "http://news.google.com/news?hl=en&gl=in&q=%s&um=1&ie=UTF-8&output=rss" %(keyword)
	rss_feed=BeautifulSoup(urlopen(url).read())
	results=[{"title":item.title.string,"link":item.guid.string.split("cluster=",1)[1],"date":item.pubdate.string}for item in rss_feed.findAll('item')] 
	return results
