# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

url = 'http://acm.mnnu.edu.cn'

response = urllib2.urlopen(url);

# 获取状态码，如果是200表示获取成功
print response.getcode()

# 读取内容
cont = response.read()

soup = BeautifulSoup(cont, 'html.parser', from_encoding='utf-8')

print 'All links'
links =soup.find_all('a')
for link in links:
	print link.name, link['href'], link.get_text()