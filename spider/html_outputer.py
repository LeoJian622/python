# -*- coding:utf-8 -*-

class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		super(HtmlOutputer, self).__init__()
		self.datas = []

	def collect_data(self, data):
		if data is None:
			return None
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html', 'w')

		fout.write("<html>")
		fout.write('<head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head>')
		fout.write("<body>")
		fout.write("<table>")
		fout.write("<tr><th>No</th><th>url</th><th>title</th><th>description</th><th>input</th><th>output</th><th>prosampleinput</th><th>prosampleoutput</th></tr>")
		
		# ascii 
		count = 1
		for data in self.datas:
			fout.write("<tr>")
			fout.write("<td>%s</td>" % count)
			count += 1
			fout.write("<td>%s</td>" % data['url'])
			fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['description'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['input'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['output'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['prosampleinput'].encode('utf-8'))
			fout.write("<td>%s</td>" % data['prosampleoutput'].encode('utf-8'))
			fout.write("</tr>")

		fout.write("</table>")
		fout.write("</body>")
		fout.write("</tml>")

		fout.close()

	def output_mysql(self):
		pass
		