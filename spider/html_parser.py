# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):
	"""docstring for HtmlParser"""
	def __init__(self):
		super(HtmlParser, self).__init__()
		
	def _get_new_urls(self, page_url, soup):
		new_urls = set()
		# eg: /Problem/show/id/1000.htm
		# eg: /Problem/lists/vol/1.htm
		links = soup.find_all('a', href=re.compile(r'/Problem/(lists|show)/(vol|id)/\d+\.htm'))
		for link in links:
			new_url      = link['href']
			new_full_url = urlparse.urljoin(page_url, new_url)
			new_urls.add(new_full_url)

		return new_urls

	def _get_new_data(self, page_url, soup):
		if re.search(r'/Problem/lists', page_url):
			print 'list url'
			return

		res_data = {}
		res_data['url']         = page_url
		# eg: <div class="slice12">	<h2>1000:A+B Problem</h2> </div>
		title_node              = soup.find('div', class_='slice12').find('h2')
		res_data['title']       = title_node.get_text();
		# eg: <div id="prodes" class="showbox des">	<div class="pro_desc">Calculate a + b.</div> </div>
		description_node        = soup.find(id='prodes')
		res_data['description'] = description_node.get_text()
		#<div id="proinput" class="showbox des"> <div class="pro_desc">The input will consist of a series of pairs of integers a and b,separated by a space, one pair of integers per line.</div> </div>
		input_node        = soup.find(id='proinput')
		res_data['input'] = input_node.get_text()
		#<div id="prooutput" class="showbox des"> <div class="pro_desc">For each pair of input integers a and b you should output the sum of a and b in one line,and with one line of output for each line in input.</div> </div>
		output_node        = soup.find(id='prooutput')
		res_data['output'] = output_node.get_text()
		#<div id="prosampleinput" class="showbox"> <pre>1 5 2 3</pre> </div>
		prosampleinput_node        = soup.find(id='prosampleinput')
		res_data['prosampleinput'] = prosampleinput_node.get_text()
		#<div id="prosampleoutput" class="showbox"> <pre>6 5</pre> </div>
		prosampleoutput_node        = soup.find(id='prosampleoutput')
		res_data['prosampleoutput'] = prosampleoutput_node.get_text()

		return res_data

	def parse(self, page_url, html_cont):
		if page_url is None or html_cont is None:
			return None
		soup     = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url, soup)
		new_data = self._get_new_data(page_url, soup)
		
		return new_urls, new_data