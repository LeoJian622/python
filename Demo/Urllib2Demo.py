# -*- coding: utf-8 -*- 
# 改变文本编码

import urllib2,cookielib

# 第一种方法  直接请求

url = 'http://www.baidu.com'

response = urllib2.urlopen(url);

# 获取状态码，如果是200表示获取成功
print response.getcode()

# 读取内容
print response.read()

# 第二种方法 使用request 可以添加数据以及添加header

# import urllib2

# 创建Request对象
request = urllib2.Request(url)

# 添加HTTP的header
request.add_header('User-Agent', 'Mozilla/5.0')

# 添加数据
#request.add_data('a', '1')

# 发送请求获取结果
response2 = urllib2.urlopen(request);

# 获取状态码，如果是200表示获取成功
print response2.getcode()

# 读取内容
print response2.read()

# 第三种方法 添加特殊情景的处理器

# 创建cookie容器
cj = cookielib.CookieJar()

# 创建1个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#给urllib2安装poener
urllib2.install_opener(opener)

#使用带有cookie的urllib2访问网页
response3 = urllib2.urlopen(url);

# 获取状态码，如果是200表示获取成功
print response3.getcode()

# 读取内容
print response3.read()

# 打印cookie
print cj