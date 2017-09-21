# -*- coding:utf-8 -*-

import urllib2
import re
from bs4 import BeautifulSoup

url = 'http://www.baidu.com'

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

print 'Special link '
link_node =soup.find('a',href='https://passport.baidu.com/v2/?login&tpl=mn&u=http%3A%2F%2Fwww.baidu.com%2F')
print link_node.name, link_node['href'], link_node.get_text()

print '正则匹配'
link_node =soup.find('a',href=re.compile(r'ssp'))
print link_node.name, link_node['href'], link_node.get_text()

print 'Get P text'
link_node =soup.find('div', class_='ftCon-Wrapper')
print link_node.name, link_node.get_text()